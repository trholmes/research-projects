# Recommended resources

These are the recommended readings and references for the
*Understanding Particle Lifetime* project. They support the physics
background you will need for the calculations, the simulation, and the
written explanation. You do not need to read all of them; pick the level
that matches your background and use the rest as references.

## Primary resource (start here)

**[OpenStax, _University Physics Volume 3_, Chapter 11: Particle Physics and Cosmology](https://openstax.org/books/university-physics-volume-3/pages/11-introduction)**

This is the gentlest starting point and is freely available online. Focus on
the early sections, especially
[11.1 Introduction to Particle Physics](https://openstax.org/books/university-physics-volume-3/pages/11-1-introduction-to-particle-physics),
which introduce:

- fundamental particles (quarks, leptons, gauge bosons) and how they are
  classified
- the four fundamental forces
- the idea that what counts as "fundamental" has changed over time, and is
  still an open question
- where quarks such as the b quark fit into the picture

## Special relativity background

**[OpenStax, _University Physics Volume 3_, Chapter 5: Relativity](https://openstax.org/books/university-physics-volume-3/pages/5-introduction)**

If you have not encountered special relativity before — or if you have seen it
but are not yet comfortable with time dilation and the Lorentz factor — start
here before Step 5. This chapter is freely available online and covers
everything you need:

- [5.3 Time Dilation](https://openstax.org/books/university-physics-volume-3/pages/5-3-time-dilation):
  why a moving clock runs slow, the Lorentz factor \(\gamma = 1/\sqrt{1-\beta^2}\),
  and what "proper time" means
- [5.4 Length Contraction](https://openstax.org/books/university-physics-volume-3/pages/5-4-length-contraction):
  useful context, though less central to this project than time dilation
- [5.6 Relativistic Velocity Transformation](https://openstax.org/books/university-physics-volume-3/pages/5-6-relativistic-velocity-transformation)
  and the momentum/energy relations in 5.8–5.9, for background on \(\beta\gamma = p/(Mc)\)

The key concept you need for this project is time dilation: a clock moving at
speed \(\beta c\) relative to you appears to tick slowly by a factor of
\(\gamma\). A particle with a rest-frame lifetime \(\tau\) therefore lives for
a time \(\gamma\tau\) in your lab frame, and travels a mean distance
\(\beta\gamma c\tau\) before decaying. If that sentence already makes sense to
you, you may not need this chapter at all.

## Going deeper

**David Griffiths, _Introduction to Elementary Particles_**

If you want a more rigorous treatment, read the **Introduction** and the
**first two chapters**. These cover the historical development of the field,
the Standard Model, and how particles decay. Pay particular attention to the
discussion of decay rates and lifetimes, which is the core of this project.

## Particle properties (Particle Data Group)

**[The Review of Particle Physics, Particle Data Group (pdg.lbl.gov)](https://pdg.lbl.gov/)**

The PDG is the standard reference for measured particle properties, and it is
where you should look up every number you use. The current edition is
*S. Navas et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024)*.
Useful pieces for this project:

- **Meson Listings / Summary Tables, Bottom mesons (B⁺, B⁰, Bₛ, ...).**
  Look up each B meson's mass and lifetime. You will find B⁰ and B⁺ lifetimes
  of roughly 1.5–1.6 ps and decay lengths \(c\tau\) of about 0.46–0.49 mm.
  Record the exact value for whichever B meson you choose.
- **Lepton Listings, the muon.** For the muon-collider stretch goal: mean
  lifetime \(\tau \approx 2.2~\mu\mathrm{s}\), \(c\tau \approx 659~\mathrm{m}\).
- **The "Kinematics" review.** For the relativistic relations you will use,
  including \(\beta\gamma = p/(Mc)\) and the decay length \(L = \beta\gamma c\tau\).
- **The "Monte Carlo Techniques" and "Statistics" reviews.** Helpful background
  for the toy Monte Carlo and for fitting the simulated distribution.

The interactive **pdgLive** interface is the quickest way to navigate to a
specific particle.

## The detector (CMS geometry)

**[CMS Detector Overview (cms.cern)](https://cms.cern/news/detector-overview)** and
**[CMS Tracking page](https://cms.cern/detector/identifying-tracks)**

Use these for the overall layered structure of CMS: the silicon tracker
(pixels and microstrips) nearest the beam, then the electromagnetic and
hadron calorimeters, the solenoid, and the muon system in the return yoke.

For the precise inner radii you need in the B-meson decay-length steps (Steps 6
and 7), the most precise public reference is **_The CMS Phase-1 Pixel Detector
Upgrade_, JINST 16 (2021) P02027** (linked from the Tracking page above). The
key numbers:

- Beam pipe radius: about **22 mm** for the current (Phase-1) layout, reduced
  from about **30 mm** in the original detector.
- Innermost pixel barrel layer: about **29 mm** (Phase-1, installed 2017),
  compared with **44 mm** in the original detector.
- Outer pixel barrel layers (Phase-1): roughly 68, 109, and 160 mm.

These are the values to use when asking whether a B meson typically decays
inside the beam pipe or after the first tracker layer.

For the LLP step (Step 9) you need the *outer* boundaries of the major
subdetectors as well. The CMS detector is roughly cylindrical, and the
following approximate barrel radii are good enough for this project (see the
[CMS Detector Overview](https://cms.cern/news/detector-overview) for the full
layout):

| Region (outer edge)           | Approx. radius |
|-------------------------------|----------------|
| Silicon tracker (outer edge)  | ~1.1 m         |
| Electromagnetic calorimeter   | ~1.5 m         |
| Hadron calorimeter            | ~2.9 m         |
| Superconducting solenoid      | ~3.8 m         |
| Muon system (outer edge)      | ~7.4 m         |

These are approximate, round numbers chosen for an order-of-magnitude exercise,
not precise survey values. State the radii you adopt in your write-up. (ATLAS
is larger — its muon system extends to about 11 m — but the qualitative picture
is the same; pick one detector and be consistent.)

## A note on natural units

Particle physicists almost always work in **natural units**, where the speed of
light is set to \(c = 1\). In this convention, mass, momentum, and energy are
all measured in the same units (electron-volts, usually GeV), and you can write
things like "a B meson of momentum \(p = 50~\mathrm{GeV}\)" without carrying
factors of \(c\) around. This is why \(\beta\gamma = p/(Mc)\) simplifies to
\(\beta\gamma = p/M\): with \(c = 1\), the formula is just a ratio of two
numbers both quoted in GeV.

If you have only ever seen SI units, this can look like a mistake the first
time ("isn't momentum in kg·m/s?"). It is not — it is a deliberate, standard
convention, and the PDG "Kinematics" review explains it. For this project you
can take the shortcut rule: **in natural units, \(\beta\gamma = p/M\) with \(p\)
and \(M\) both in GeV**, and lengths follow from \(L = \beta\gamma\, c\tau\)
where \(c\tau\) is the tabulated decay length (already a length, e.g. 0.46 mm).

## Computational tools

You will do the calculations, plots, and simulation in Python. If you are new
to scientific Python, you only need three libraries:

- **NumPy** for arrays and random sampling (`numpy.random` for the toy Monte
  Carlo).
- **Matplotlib** (`matplotlib.pyplot`) for the plots.
- **SciPy** (`scipy.optimize.curve_fit`) for fitting the simulated
  distribution in Step 8.

The [SciPy Lecture Notes](https://scipy-lectures.org/) and the
[Matplotlib pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
are good, free starting points if any of these are unfamiliar. A Jupyter
notebook is a convenient place to work, since it lets you interleave code,
plots, and explanation, but a plain script is equally acceptable.

## Physics context

**[CERN: "Long-sought decay of Higgs boson observed" (2018)](https://home.cern/news/press-release/physics/long-sought-decay-higgs-boson-observed)**

Background for why identifying b quarks matters. The Standard Model predicts
that roughly 58–60% of Higgs bosons decay to a pair of bottom quarks, making
\(H \to b\bar{b}\) the most common Higgs decay, and b-tagging essential for
studying it. This page also gives a sense of how the ATLAS and CMS experiments
operate and what LHC collisions produce.
