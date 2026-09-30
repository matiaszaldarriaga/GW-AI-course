"""Alternative Q/m analysis for the licopodium Paul-trap videos.

Method: threshold the red channel, identify bright connected objects, and
measure each trace from its intensity-weighted second moment.  For a uniform
line of end-to-end length L, Var(along-line)=L^2/12, hence L=sqrt(12*lambda1).
No skeletonization or arc-length traversal is used.  The common centre and c
are obtained by a robust simultaneous fit L=c*distance((x,y),(xc,yc)).
"""
from pathlib import Path
import cv2, numpy as np, pandas as pd
from scipy.optimize import least_squares
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
VIDDIR = next(ROOT.glob('drive-download-*'))
OUT = ROOT/'alternative_results'; OUT.mkdir(exist_ok=True)
THRESH=30; NFRAMES=40; MINAREA=100; MAXAREA=8000; MIN_ELONG=2.0
r0=8.90e-3; sr0=0.50e-3; V=1175.; sV=24.; f=50.; omega=2*np.pi*f

def detections(video):
    cap=cv2.VideoCapture(str(video)); n=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    inds=np.linspace(0,max(n-1,0),min(NFRAMES,n),dtype=int); rows=[]
    for fi in inds:
        cap.set(cv2.CAP_PROP_POS_FRAMES,int(fi)); ok,fr=cap.read()
        if not ok: continue
        red=fr[:,:,2].astype(float); labn,lab,stats,_=cv2.connectedComponentsWithStats((red>THRESH).astype('uint8'),8)
        for k,s in enumerate(stats[1:],1):
            area=int(s[4])
            if not MINAREA<=area<=MAXAREA: continue
            yy,xx=np.where(lab==k); w=red[yy,xx]-THRESH+1.0
            x=float(np.average(xx,weights=w)); y=float(np.average(yy,weights=w))
            X=np.column_stack((xx-x,yy-y)); cov=(X*w[:,None]).T@X/w.sum()
            ev=np.linalg.eigvalsh(cov); elong=np.sqrt(max(ev[1],1e-12)/max(ev[0],1e-12))
            if elong<MIN_ELONG: continue
            # PCA-equivalent end-to-end length; second moment, not skeleton.
            L=float(np.sqrt(12*ev[1]))
            if L<3 or L>250: continue
            rows.append((fi,x,y,L,area,elong))
    cap.release()
    return pd.DataFrame(rows,columns=['frame','x','y','L','area','elong'])

def fit(df):
    x=df[['x','y']].to_numpy(); L=df.L.to_numpy()
    c0=np.clip(np.median(L/np.maximum(np.linalg.norm(x-[281,80],axis=1),1)),0.005,2); p0=[281,80,c0]
    def fun(p): return (p[2]*np.linalg.norm(x-p[:2],axis=1)-L)
    res=least_squares(fun,p0,bounds=([0,0,0],[640,480,10]),loss='soft_l1',f_scale=max(np.median(np.abs(fun(p0))),1))
    xc,yc,c=res.x; R=np.linalg.norm(x-[xc,yc],axis=1); ci=L/R
    # bootstrap whole detections: uncertainty of common fit, not standard error of all pixels
    rng=np.random.default_rng(12345); bs=[]
    for _ in range(300):
        ix=rng.integers(0,len(df),len(df)); xb=x[ix]; lb=L[ix]
        def fb(p): return (p[2]*np.linalg.norm(xb-p[:2],axis=1)-lb)
        q=least_squares(fb,res.x,bounds=([0,0,0],[640,480,10]),loss='soft_l1',f_scale=max(np.median(np.abs(fb(res.x))),1))
        bs.append(q.x)
    bs=np.asarray(bs)
    return res.x, ci, bs

def q_over_m(c): return c*r0*r0*omega*omega/(4*V)

def main():
    summaries=[]; allrows=[]
    for video in sorted(VIDDIR.glob('*.mp4')):
        df=detections(video)
        if len(df)<20: continue
        p,ci,bs=fit(df); c=p[2]; sc=float(np.std(bs[:,2],ddof=1)); qm=q_over_m(c)
        sqm=qm*np.sqrt((sc/max(c,1e-9))**2+(2*sr0/r0)**2+(sV/V)**2)
        name=video.stem; df['video']=name; df['ci']=ci; allrows.append(df)
        summaries.append(dict(video=name,n=len(df),xc=p[0],yc=p[1],c=c,sc_boot=sc,qm=qm,sqm=sqm,
                             c_sd=np.std(ci,ddof=1),median_elong=np.median(df.elong)))
        fig,ax=plt.subplots(1,2,figsize=(11,4.5))
        ax[0].scatter(df.x,df.y,c=ci,s=12,cmap='viridis'); ax[0].scatter([p[0]],[p[1]],c='r',marker='x',s=70)
        ax[0].invert_yaxis(); ax[0].set(xlabel='x [px]',ylabel='y [px]',title=name+' detections / fitted centre'); ax[0].set_aspect('equal')
        R=np.linalg.norm(df[['x','y']].to_numpy()-p[:2],axis=1); ax[1].scatter(R,df.L,s=10,alpha=.55); rr=np.linspace(0,max(R)*1.05,100); ax[1].plot(rr,c*rr,'r'); ax[1].set(xlabel='R [px]',ylabel='PCA length L [px]',title=f'c={c:.3f} ± {sc:.3f}')
        fig.tight_layout(); fig.savefig(OUT/(name+'.png'),dpi=160); plt.close(fig)
    if allrows: pd.concat(allrows,ignore_index=True).to_csv(OUT/'detections.csv',index=False)
    s=pd.DataFrame(summaries).sort_values('n',ascending=False); s.to_csv(OUT/'summary.csv',index=False)
    print(s.to_string(index=False))
    print('\nweighted median by detections:',np.average(s.qm,weights=s.n) if len(s) else 'none')
    print('conversion qm/c =',q_over_m(1.0))

if __name__=='__main__': main()
