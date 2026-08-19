# The papers

Five, in the order the day uses them. **Read the third one.**

- `phinney-2001-practical-theorem.pdf` — Phinney, *A practical theorem on
  gravitational wave backgrounds* (2001). Three pages of argument that the whole day
  rests on: the gravitational-wave energy density equals the comoving density of event
  *remnants* times the energy each radiated, independent of cosmology and only weakly
  dependent on the merger history. Read §1 and the circular-binary case. The remark worth
  the whole paper is his own: to derive the inspiral spectrum *"one need know nothing
  about gravitational radiation except that it has twice the orbital frequency, and that
  the orbital binding energy is removed by the gravitational radiation."* No quadrupole
  formula. We check that in sympy in `reproductions/gwb-from-a-population`.

- `roebber-holder-2017-harmonic-hd.pdf` — Roebber & Holder, *Harmonic space analysis of
  pulsar timing array redshift maps* (2017). Hellings–Downs done as a power spectrum
  rather than as a two-point function, which is what makes it derivable in an afternoon.
  Every figure in it is reproduced in `reproductions/harmonic-hd-maps`, so you can check
  ours against theirs by eye. Note what it does **not** do: it derives the multipole
  *shape* from scratch and then fixes the overall constant by matching to the 1983 curve.
  We derive the constant instead — which is the only reason we can use Hellings–Downs as
  a test.

- `2312.06756-where-are-the-big-black-holes.pdf` — Sato-Polito, Quataert & Zaldarriaga,
  *Where are NANOGrav's big black holes?* (2023). **This is the one to read.** Short, and
  it is the day's spine: a prediction of the nanohertz background from a local black-hole
  census with no free parameters, the factor by which it falls short, and the proof that
  no merger history can make up the difference. Read it for the *structure of the
  argument* — what is assumed, what is derived, and what is left as a hole.

- `2406.17010-gwb-distribution.pdf` — Sato-Polito & Zaldarriaga, *The distribution of the
  gravitational-wave background from supermassive black holes* (2024). The observable is
  not the mean. Because the background is a finite sum of discrete binaries, what a PTA
  measures in one frequency bin is a draw from a skewed distribution, and this paper
  computes it. It also reaches the opposite conclusion to the previous one about how
  heavy the black holes can be — same data, one extra piece of information.

- `2509.08041-abundance-uncertainties.pdf` — Sato-Polito, *Uncertainties in the SMBH
  abundance* (2025). How little it takes to move the prediction: a **relative** systematic
  offset of 0.03 dex between the black-hole catalogue and the galaxy catalogue shifts
  $h_c$ by the entire width of the NANOGrav interval.

---

## Read the third one

It is thirteen pages, its central claim is a number you can check, and two of its authors
are in the building. After the session, open the first one at Phinney's theorem and see
how much of it you can now read without stopping — that is the honest measure of what the
day was worth.

## What we do and do not reproduce

`reproductions/gwb-from-a-population` reproduces 2312.06756 section by section, and finds
one erratum: **Eq. 16 carries a spurious $c^2$** relative to Eq. 14, because the
efficiency $\epsilon$ already contains $1/c^2$. Transcribe it literally and you are low by
a factor of $9\times10^{16}$. That is in `run.log` with the check that measures it.

We reproduce **all six figures** of Roebber & Holder in `reproductions/harmonic-hd-maps`,
and the derivation itself independently in `reproductions/hellings-downs` — one in pixel
space with healpy, one symbolically in sympy, sharing no code. They agree to $7\times10^{-5}$.

We do **not** reproduce 2509.08041 or 2406.17010 in full. From the first we take the
0.03 dex sensitivity; from the second, the $P(D)$ construction in
`reproductions/gwb-strain-distribution`.

## Where these came from

All five are **rebuilt from the arXiv TeX source** in this repository's top-level
`papers/`, not downloaded as published PDFs — so what you have is the authors' source,
typeset here. Two consequences worth knowing:

- Phinney 2001 used `mn2e.cls`, the old MNRAS class, which has been retired from TeX Live
  and cannot be installed. It is rebuilt with a substituted `article` class and stub
  macros. **The content is the author's; the typesetting is not the published one**, and
  page numbers will not match citations to the journal version.
- Roebber & Holder is downsampled to keep it under a megabyte. If you want the full-
  resolution sky maps, they are the individual PDFs in `papers/roebber-holder-harmonic-pta/`.

One paper is deliberately absent. Goncharov et al. 2606.18241 is catalogued in the wiki
and is genuinely relevant, but it analyses **simulated** NANOGrav data throughout — every
number in it is a forecast — and the safest way not to have a forecast read as a
measurement was to keep it off the reading list.
