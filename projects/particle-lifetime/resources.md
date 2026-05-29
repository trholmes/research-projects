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

For the specific radii you need in the decay-length steps, the most precise
public reference is **_The CMS Phase-1 Pixel Detector Upgrade_, JINST 16 (2021)
P02027** (linked from the Tracking page above). The key numbers:

- Beam pipe radius: about **22 mm** for the current (Phase-1) layout, reduced
  from about **30 mm** in the original detector.
- Innermost pixel barrel layer: about **29 mm** (Phase-1, installed 2017),
  compared with **44 mm** in the original detector.
- Outer pixel barrel layers (Phase-1): roughly 68, 109, and 160 mm.

These are the values to use when asking whether a B meson typically decays
inside the beam pipe or after the first tracker layer.

## Physics context

**[CERN: "Long-sought decay of Higgs boson observed" (2018)](https://home.cern/news/press-release/physics/long-sought-decay-higgs-boson-observed)**

Background for why identifying b quarks matters. The Standard Model predicts
that roughly 58–60% of Higgs bosons decay to a pair of bottom quarks, making
\(H \to b\bar{b}\) the most common Higgs decay, and b-tagging essential for
studying it. This page also gives a sense of how the ATLAS and CMS experiments
operate and what LHC collisions produce.
