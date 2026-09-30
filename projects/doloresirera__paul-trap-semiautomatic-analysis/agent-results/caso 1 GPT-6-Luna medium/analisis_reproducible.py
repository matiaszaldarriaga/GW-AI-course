from pathlib import Path
import cv2, numpy as np, json, math
from scipy.optimize import least_squares
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
OUT=ROOT
VIDEOS=sorted(ROOT.glob('*.mp4'))
NFRAMES=40
THRESH=40

def skeleton(mask):
    img=mask.copy(); sk=np.zeros_like(img); kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    while cv2.countNonZero(img):
        er=cv2.erode(img,kernel); op=cv2.dilate(er,kernel); sk=cv2.bitwise_or(sk,cv2.subtract(img,op)); img=er
    return sk

def trace_length(mask):
    sk=skeleton(mask); yy,xx=np.where(sk>0)
    if len(xx)<2: return 0., (float(xx[0]),float(yy[0])) if len(xx) else (0.,0.)
    # Count each 8-neighbor edge once; diagonals weigh sqrt(2).
    s=sk>0; length=0.
    for dy,dx,w in [(0,1,1.),(1,-1,math.sqrt(2)),(1,0,1.),(1,1,math.sqrt(2))]:
        a=s[max(0,dy):s.shape[0]+min(0,dy),max(0,dx):s.shape[1]+min(0,dx)]
        b=s[max(0,-dy):s.shape[0]+min(0,-dy),max(0,-dx):s.shape[1]+min(0,-dx)]
        length += np.count_nonzero(a & b)*w
    return float(length), (float(np.mean(xx)),float(np.mean(yy)))

def collect(video,threshold=40):
    cap=cv2.VideoCapture(str(video)); n=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); rec=[]; used=0
    for frame_no in np.linspace(0,max(0,n-1),NFRAMES,dtype=int):
        cap.set(cv2.CAP_PROP_POS_FRAMES,int(frame_no)); ok,frame=cap.read()
        if not ok: continue
        used+=1; red=frame[:,:,2]; _,binary=cv2.threshold(red,threshold,255,cv2.THRESH_BINARY)
        count, labels, stats, _=cv2.connectedComponentsWithStats(binary,8)
        for k in range(1,count):
            x,y,w,h,area=stats[k]
            if area<150 or area>8000 or max(w,h)/max(1,min(w,h))<2.5: continue
            roi=(labels[y:y+h,x:x+w]==k).astype(np.uint8)*255
            L,(mx,my)=trace_length(roi)
            if L<5: continue
            rec.append((x+mx,y+my,L,int(frame_no)))
    cap.release()
    return np.array(rec,float).reshape((-1,4)),used

def fit(points):
    xy=points[:,:2]; L=points[:,2]
    if len(L)<6: return None
    def resid(p): return L-p[2]*np.hypot(xy[:,0]-p[0],xy[:,1]-p[1])
    # initialize center below the visible fan, multistart for local minima
    starts=[(320,100),(320,180),(280,100),(360,100),(320,240)]
    fits=[]
    for x,y in starts:
        q=least_squares(resid,[x,y,.5],bounds=([-500,-500,0],[1100,1000,5]),loss='soft_l1',f_scale=5,max_nfev=3000)
        fits.append(q)
    q=min(fits,key=lambda z:np.sum(resid(z.x)**2)); xc,yc,c=q.x
    pred=c*np.hypot(xy[:,0]-xc,xy[:,1]-yc); r2=1-np.sum((L-pred)**2)/np.sum((L-L.mean())**2) if np.var(L)>0 else float('nan')
    ang=np.degrees(np.arctan2(xy[:,1]-yc,xy[:,0]-xc))%360; s=np.sort(ang); gaps=np.diff(np.r_[s,s[0]+360]); coverage=360-float(gaps.max())
    centers=[]; cs=[]; rng=np.random.default_rng(716)
    for _ in range(80):
        inds=rng.integers(0,len(points),len(points)); pp=points[inds]
        if len(pp)<6: continue
        def rr(p): return pp[:,2]-p[2]*np.hypot(pp[:,0]-p[0],pp[:,1]-p[1])
        z=least_squares(rr,[xc,yc,c],bounds=([-500,-500,0],[1100,1000,5]),loss='soft_l1',f_scale=5,max_nfev=1000).x
        centers.append(z[:2]); cs.append(z[2])
    center_sd=float(np.median(np.linalg.norm(np.array(centers)-[xc,yc],axis=1))) if centers else float('nan')
    c_sd=float(np.std(cs,ddof=1)) if len(cs)>1 else float('nan')
    return dict(n=len(L),xc=xc,yc=yc,c=c,r2=r2,coverage=coverage,center_sd=center_sd,c_boot_sd=c_sd,
                lengths=L,xy=xy,pred=pred,angles=ang)

rows=[]; allfits=[]
for vi,v in enumerate(VIDEOS):
    pts,nf=collect(v,THRESH); f=fit(pts)
    for t in (35,45):
        pp,_=collect(v,t); ff=fit(pp)
        if f and ff: f['threshold_cs']=f.get('threshold_cs',[])+[ff['c']]
    valid=bool(f and f['n']>=12 and f['coverage']>=25 and f['center_sd']<=20 and f['r2']>=0.5 and f['c']<0.908)
    row=dict(video=v.name,frames=nf,traces=int(f['n']) if f else len(pts),valid=valid)
    if f:
        row.update({k:float(f[k]) for k in ['xc','yc','c','r2','coverage','center_sd','c_boot_sd']})
        tcs=f.get('threshold_cs',[f['c']]); threshold_sd=float(np.std(tcs,ddof=1)) if len(tcs)>1 else 0.
        # Report-like length uncertainty proxy from 1 px per centerline endpoint-scale and bootstrap center term.
        skeleton_sd=f['c']*0.03
        center_term=f['c']*f['center_sd']/max(1.,np.median(np.hypot(f['xy'][:,0]-f['xc'],f['xy'][:,1]-f['yc'])))
        c_err=math.sqrt(threshold_sd**2+skeleton_sd**2+center_term**2)
        row.update(c_error=c_err,threshold_sd=threshold_sd,skeleton_sd=skeleton_sd,center_term=center_term)
        # Conditional SI conversion, explicitly using report's r0, V and inferred mains frequency.
        r0=.00890; dr0=.00050; V=1175.; dV=24.; freq=50.; om=2*math.pi*freq
        qm=f['c']*r0*r0*om*om/(4*V)
        qmerr=qm*math.sqrt((c_err/f['c'])**2+(2*dr0/r0)**2+(dV/V)**2)
        row.update(qm=qm,qm_error=qmerr)
        allfits.append((v.name,pts,f,valid))
    rows.append(row)

# Per-video diagnostic plots, fit and angular map where fit exists.
for name,pts,f,valid in allfits:
    slug=Path(name).stem.replace('WhatsApp Video 2026-09-26 at ','').replace(' ','_').replace(':','-')
    fig,ax=plt.subplots(1,2,figsize=(10,4.5))
    xy=f['xy']; ax[0].scatter(xy[:,0],xy[:,1],s=12,c=f['lengths'],cmap='inferno'); ax[0].scatter([f['xc']],[f['yc']],marker='+',s=100,c='cyan'); ax[0].invert_yaxis(); ax[0].set(xlim=(0,640),ylim=(480,0),xlabel='x (px)',ylabel='y (px)',title=f"Trazas y centro ({f['n']} trazas)")
    R=np.hypot(xy[:,0]-f['xc'],xy[:,1]-f['yc']); ax[1].scatter(R,f['lengths'],s=13,alpha=.7); order=np.argsort(R); ax[1].plot(R[order],f['c']*R[order],color='crimson',label=f"c={f['c']:.3f}"); ax[1].set(xlabel='R (px)',ylabel='L (px)',title=f"L=cR; R²={f['r2']:.2f}"); ax[1].legend(); fig.tight_layout(); fig.savefig(OUT/f'fig_{slug}.png',dpi=150); plt.close(fig)

# Combined table graphic
fig,ax=plt.subplots(figsize=(12,5)); names=[Path(r['video']).stem.replace('WhatsApp Video 2026-09-26 at ','') for r in rows]; vals=[r.get('c',np.nan) for r in rows]; errs=[r.get('c_error',np.nan) for r in rows]; cols=['#27864a' if r['valid'] else '#ba7b20' for r in rows]; ax.bar(range(len(rows)),vals,yerr=errs,color=cols,capsize=3); ax.set_xticks(range(len(rows)),names,rotation=50,ha='right'); ax.set_ylabel('c'); ax.set_title('Estimaciones automáticas por video (verde: validación mínima; ocre: exploratoria)'); fig.tight_layout(); fig.savefig(OUT/'fig_resumen_c.png',dpi=160); plt.close(fig)
(ROOT/'resultados_videos.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps([{k:r.get(k) for k in ['video','traces','valid','c','c_error','qm','qm_error','coverage','center_sd','r2']} for r in rows],ensure_ascii=False,indent=2))




