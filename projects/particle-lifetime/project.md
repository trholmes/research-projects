---
title: "Understanding Particle Lifetime"
pi: "trholmes"
goals:
  - "Understand the concept of particle lifetime"
  - "Connect particle lifetime to concepts of distance traveled and special relativity"
  - "Explore applications of this in collider physics, including B mesons and long-lived particles"
  - "Produce a plot of B meson distance traveled as a function of its energy"
  - "Use toy monte carlo to produce a full distribution and compare its mean to the analytical one"
  - "Use the same concepts to simulate LLPs and identify best regions to search for their decays"
  - "Extend this to a muon collider by looking at how quickly muons must be accelerated to be used in collisions"
---

# Research Project: Understanding Particle Lifetime

## Project overview

In this project, you will build up an understanding of what it means for a
particle to have a *lifetime*, and you will turn that understanding into
concrete calculations and plots that connect directly to how experiments at
the Large Hadron Collider (LHC) actually work.

Many fundamental particles are unstable. They exist for a short time and then
decay into other particles. A key idea you will develop is that a particle's
lifetime is *probabilistic*: you can never predict exactly when a single
particle will decay, but for a large collection of identical particles, the
pattern of decays is completely predictable. This is one of the places where
the strangeness of quantum mechanics shows up in a way you can plot.

Your main goal is to understand how this probabilistic lifetime, combined with
special relativity, determines how far a particle travels before it decays in
a real detector. You will apply this to the *b quark* (and the B mesons it
forms), which is central to studying the Higgs boson at the LHC. You will
produce a plot of how far a B meson typically travels as a function of its
energy, and then you will build a small simulation, called a **toy Monte
Carlo**, that reproduces the full distribution of decay distances and lets you
recover the particle's lifetime from the data you generate.

This project is designed for beginning physics students, ideally as a first
project in particle physics. You are not expected to know any particle physics
or special relativity at a research level when you start. By the end, you
should be able to explain what a particle lifetime is, why it is probabilistic,
how relativity stretches it out in the laboratory, and how experiments exploit
all of this to identify b quarks. You will also strengthen your ability to use
Python for scientific calculation, simulation, and plotting.

---

## Core idea

An unstable particle does not have a fixed lifespan. If you prepare a large
number \(N_0\) of identical particles, the number still surviving after a
proper time \(t\) follows

\[
N(t) = N_0 \, e^{-t/\tau},
\]

where \(\tau\) is the **mean lifetime** measured in the particle's own rest
frame. No individual particle "knows" it is about to decay; only the ensemble
behaves predictably.

A particle moving quickly through a detector lives longer in the laboratory
frame, because of relativistic time dilation, and it covers real distance
while it does. The mean distance it travels before decaying is

\[
L = \beta\gamma\, c\tau,
\]

where \(\beta\gamma = p / (Mc)\) for a particle of momentum \(p\) and mass
\(M\). The quantity \(c\tau\) is a fixed property of the particle (a length you
can look up), while \(\beta\gamma\) depends on how energetic the particle is in
your experiment.

Your task is to understand where these equations come from, apply them to B
mesons at the LHC, and then go beyond the average by simulating the full
distribution of decay distances. The point is not to memorize formulas, but to
be able to explain *why* a B meson typically decays a few millimeters from
where it was produced, and what that means for how we find it.

---

## Required products

At the end of the project, you should produce:

- **A plot of B meson decay length versus energy**
  This should show the mean laboratory distance \(L = \beta\gamma c\tau\) that
  a B meson travels before decaying, as a function of its energy (or
  momentum). It should be clearly labeled, and you should be able to point to a
  single hand-calculated value on it and confirm the curve agrees.

- **A toy Monte Carlo of the decay distribution**
  For a chosen B meson energy, this should generate many simulated decays and
  histogram the laboratory decay distances. The mean of your simulated
  distribution should match the analytical value \(\beta\gamma c\tau\), and you
  should fit the distribution to recover the input lifetime.

- **A short written explanation**
  This should explain what your plots show: what a particle lifetime is, why it
  is probabilistic, how the laboratory decay length depends on energy, and how
  experiments use this to identify b quarks. It should also discuss the
  difference between the laboratory frame and the particle's rest frame.

- **A clean Python notebook or script**
  This should generate your calculations, plots, and toy Monte Carlo. The code
  should be readable, well organized, and clearly commented, so that another
  student could understand and reuse it.

---

## Suggested workflow

### Step 1: Get oriented with fundamental particles

Before talking about lifetimes, make sure you have a working picture of which
particles exist and how they are organized.

Spend some time with the recommended reading (see `resources.md`) to get
comfortable with:

- the idea of a *fundamental* particle (quarks, leptons, gauge bosons, the
  Higgs)
- the difference between fundamental particles and *composite* particles such
  as protons, neutrons, and mesons
- where the b quark and the B mesons it forms sit in this picture

It is worth holding this division with a little healthy skepticism. What counts
as "fundamental" has changed repeatedly throughout the history of physics.
Atoms were once thought to be indivisible; protons and neutrons were once
treated as elementary before quarks were proposed; and there are open questions
today about whether the particles we currently call fundamental have any deeper
structure. Treat "fundamental" as "fundamental as far as we can currently
tell," not as a permanent label.

Suggested resources for this step (these belong in `resources.md`):

- OpenStax *University Physics*, the chapter on particle physics, for a gentle
  first pass.
- For students who want more depth, the Introduction and first two chapters of
  Griffiths, *Introduction to Elementary Particles*.
- The Particle Data Group (PDG) Reviews and Summary Tables, which are the
  standard reference for particle properties such as masses and lifetimes.
- A short description of the CMS detector geometry, especially the beam pipe
  and the layers of the pixel/silicon tracker, since you will need approximate
  radii later. (We will collect specific, citable numbers in `resources.md`.)

You do not need to master any of this. The goal is to be able to say, in your
own words, what a b quark is and roughly where it lives in the particle
landscape.

### Step 2: Understand lifetime as a probabilistic quantity

You may already have met the idea of a **half-life** when learning about
radioactive isotopes. A sample of a radioactive isotope does not all decay at
once; instead, after one half-life, half of it remains, after two half-lives a
quarter remains, and so on.

Particle lifetimes work the same way. The relationship between the half-life
\(t_{1/2}\) and the mean lifetime \(\tau\) is

\[
t_{1/2} = \tau \ln 2 .
\]

The crucial conceptual point is this: you cannot predict when a *single*
particle will decay. A given B meson might decay almost immediately, or it
might last much longer than average. What is predictable is the *shape* of the
distribution for a large ensemble: an exponential, governed by the single
number \(\tau\).

This is not a statement about our ignorance or our equipment. It is a
fundamental feature of quantum mechanics. The same probabilistic character
shows up in many other particle properties, not just lifetimes. Quantum
mechanics generally tells you the probabilities of outcomes, not the outcome of
any single measurement.

Check your understanding before moving on:

- If a particle has survived for a time equal to one lifetime already, is it
  any "more likely" to decay in the next instant than a freshly produced one?
  (This is the memoryless property of the exponential distribution. Make sure
  you can explain your answer.)
- What is the difference between the mean lifetime \(\tau\) and the half-life?
- If you measured the decay times of a million identical particles and
  histogrammed them, what shape would you expect, and what sets its scale?
- Why is it meaningful to quote a lifetime for a particle even though you can
  never predict the fate of one individual particle?

### Step 3: Meet the LHC, ATLAS, CMS, and the Higgs

Now connect lifetimes to where they get measured. Read enough about the LHC and
its experiments to be able to describe:

- how the LHC accelerates and collides protons, and roughly what energies are
  involved
- what the ATLAS and CMS experiments are, and the general idea that they are
  large, layered detectors built around the collision point
- that collisions produce sprays of particles, many of which are unstable and
  decay almost immediately

A key player here is the **Higgs boson**. When a Higgs boson is produced and
decays, its single most common decay is into a b quark and an anti-b quark
(\(H \to b\bar{b}\)). That makes the ability to identify b quarks essential for
studying the Higgs.

How do you identify a b quark? You do not see the quark directly. A b quark
*hadronizes*, meaning it combines with other quarks to form a B hadron (such as
a B meson) almost immediately. That B meson is unstable and travels a short but
measurable distance before decaying. Because B mesons live relatively long for
particles of their kind, they travel far enough to produce a **secondary
vertex**: a decay point that is measurably displaced from the original
collision point. Reconstructing that displaced vertex from the tracks of the
decay products is the basis of "b-tagging."

Make sure you can answer:

- Why can't we detect the b quark itself directly?
- What does it mean for a quark to hadronize?
- What is a secondary vertex, and why does the b quark's lifetime make one
  possible?
- Roughly how big do you expect this displacement to be? (You will calculate it
  next.)

### Step 4: Lab frame versus proper frame, and a hand calculation

Before plotting anything, do one calculation by hand so the later code has
something to check against.

Look up (and record in `resources.md`) the B meson's mass \(M \approx
5.28~\mathrm{GeV}\) and its decay length \(c\tau\), which is roughly half a
millimeter (about \(0.5~\mathrm{mm}\); look up the precise value for the
specific B meson you choose, since they differ slightly). Then, for an example
momentum, say \(p = 50~\mathrm{GeV}\), compute:

1. \(\beta\gamma = p / (Mc)\) (in natural units, \(\beta\gamma = p / M\)),
2. the mean laboratory decay length \(L = \beta\gamma\, c\tau\).

You should find a value of a few millimeters. Keep this number; you will mark it
on your plot later.

Now make sure the frames are clear in your head, because this is where students
most often get confused:

- In the B meson's own **rest (proper) frame**, it is not moving. It simply
  exists for a proper time drawn from the exponential distribution with mean
  \(\tau\), and then decays. In this frame, asking "how far did it travel"
  is not meaningful, because in its own frame it does not move. There is no
  sensible notion of a "proper distance traveled."
- In the **laboratory frame**, the meson is moving at speed \(\beta c\), its
  lifetime is dilated by the factor \(\gamma\), and so it covers a real
  distance \(L = \beta\gamma c\tau\) on average.

Check your understanding:

- Why is \(c\tau\) a property of the particle, while \(L\) depends on your
  experiment?
- A colleague says "the B meson travels 0.5 mm in its own frame." What is wrong
  with that statement?
- If you doubled the momentum of the B meson, what would happen to its average
  laboratory decay length, and why?

### Step 5: Plot the average decay length versus energy

Now reproduce, in code, the relationship you just calculated by hand.

Make a plot of the mean laboratory decay length \(L = \beta\gamma c\tau\) as a
function of the B meson's energy (or momentum). Iterate on it until you are
confident it is correct:

- Mark your hand-calculated point from Step 4 on the curve and confirm it lands
  where the formula predicts.
- Check the limiting behavior. At high momentum, how should \(L\) scale with
  \(p\)? Does your curve behave that way?
- Label your axes with units and state clearly which B meson (and which
  \(c\tau\)) you used.

Then connect the plot to the real detector. Using the approximate CMS geometry
(collect specific values in `resources.md`), answer:

- The beam pipe has a radius of roughly \(2\)–\(3~\mathrm{cm}\), and the
  innermost layer of the pixel tracker sits a little outside it (around
  \(4.4~\mathrm{cm}\) for the original CMS pixel detector, and around
  \(2.9~\mathrm{cm}\) for the Phase-1 upgrade installed in 2017). At what B
  meson energies would the *average* decay happen while the particle is still
  inside the beam pipe?
- At what energies would the average decay happen only *after* the first layer
  of the tracker?

You should find something that seems surprising at first: at the energies
typical of LHC collisions, the average B meson decays well inside the beam
pipe, long before reaching the first tracker layer. Reaching the first layer on
average would require very high momenta (hundreds of GeV). This is exactly why
b-tagging does not rely on the B meson reaching a particular detector layer.
Instead, the meson decays in the beam-pipe region, and the precise tracker
measures the charged decay products and extrapolates them back to reconstruct
the displaced secondary vertex.

### Step 6: From the average to the full distribution

The plot in Step 5 shows only the *mean* decay length. But you already know
from Step 2 that decays are spread out exponentially. Two B mesons with the same
energy will travel different distances.

Pick a particular energy and ask a sharper question:

- For a B meson of that energy, what *fraction* of the time will it decay only
  after passing the first layer of the tracker?

You can answer this analytically. The probability of surviving (not yet
decaying) past a laboratory distance \(d\) is

\[
P(L > d) = e^{-d / (\beta\gamma c\tau)} .
\]

Evaluate this for your chosen energy and the first-layer radius. You should find
that the fraction is very small at typical energies, reinforcing the picture
from Step 5. Make sure you can explain in words why this fraction is so small,
and how it depends on energy.

### Step 7: Build a toy Monte Carlo

A **toy Monte Carlo** is a simple simulation that generates pseudo-random
"events" according to a known probability distribution, so you can study the
distribution by sampling from it rather than only by calculating with formulas.
It is one of the most common tools in experimental particle physics, and this
project is a good first place to learn it.

For a chosen B meson energy, build a toy Monte Carlo of the decay distance:

1. Draw a proper decay time \(t_i\) for each simulated particle from an
   exponential distribution with mean \(\tau\). One standard way is to draw a
   uniform random number \(u_i \in (0, 1)\) and set \(t_i = -\tau \ln u_i\).
   Convince yourself this produces an exponential distribution.
2. Convert each proper decay time into a laboratory decay distance using the
   relativistic factor for your chosen energy: \(L_i = \beta\gamma\, c\, t_i\).
3. Histogram the \(L_i\) values for many simulated particles (thousands or
   more).

Then analyze what you generated:

- Compute the **mean** of your simulated decay distances and compare it to the
  analytical expectation \(\beta\gamma c\tau\). They should agree, with better
  agreement as you increase the number of simulated particles.
- **Fit** the histogram with an exponential function and extract the decay
  length. From it, recover the input lifetime \(\tau\) and check that you get
  back the value you put in.

This last step is the heart of the project: you have gone from an abstract,
probabilistic property of a particle all the way to generating realistic
simulated data and measuring the property back out of it, exactly as an
experimentalist does.

Check your understanding:

- Why does the mean of the simulated distribution approach the analytical value
  as you add more particles, and how does the scatter behave?
- If your fit returned a lifetime noticeably different from the input, what are
  the likely causes (statistics, binning, fit range)?
- How would the distribution change if you chose a higher energy?

### Step 8: Write the explanation

Your short written explanation should describe not just what you did, but what
you learned. It should answer questions such as:

- What is a particle lifetime, and in what sense is it probabilistic?
- How are lifetime and half-life related?
- How does the laboratory decay length depend on the particle's energy, and
  why?
- What is the difference between the rest frame and the laboratory frame, and
  why is there no meaningful "proper distance traveled"?
- How do experiments use the b quark's lifetime to identify it?
- What did your toy Monte Carlo teach you that the average value alone did not?

---

## Stretch goal 1: Long-lived particles (LLPs)

The B meson is a relatively long-lived particle by the standards of collider
physics, but many proposed new particles would live far longer, traveling
centimeters or even meters before decaying. These are called **long-lived
particles (LLPs)**, and searching for their displaced decays is an active area
of research.

Using the same machinery you built above, investigate where in a detector such
particles would decay. The probability of decaying within a shell between radii
\(r_1\) and \(r_2\) is

\[
P(r_1 < L < r_2) = e^{-r_1/(\beta\gamma c\tau)} - e^{-r_2/(\beta\gamma c\tau)} .
\]

Your goals for this section:

1. Remake a plot, this time as a function of the particle's lifetime (or
   \(c\tau\)), showing the fraction of decays expected in different detector
   regions (for example, inside the tracker, between the tracker and
   calorimeter, or out in the muon system).
2. Think about what it takes to actually *detect* such a decay, for example
   requiring that one or two of the decay products be reconstructed in a
   particular subdetector.
3. Identify which range of lifetimes is best searched for in each region. There
   is no single best detector region; the optimal place to look depends
   strongly on the particle's lifetime.

### Stretch goal 2: Muons at a muon collider

A muon collider is a proposed future machine that would collide muons instead
of protons or electrons. Muons are attractive because they are fundamental
(unlike protons) and much heavier than electrons (so they radiate far less when
accelerated). The catch is that the muon is unstable, with a mean lifetime of
about \(2.2~\mu\mathrm{s}\) and \(c\tau \approx 659~\mathrm{m}\). If you do not
accelerate them quickly, most of them decay before you can use them.

Using the survival relation \(N(t)/N_0 = e^{-t/(\gamma\tau)}\) in the laboratory
frame, investigate:

- For a target collision energy, what is the relativistic factor \(\gamma\) of
  the muons?
- Given a plausible acceleration scheme (you choose how long the acceleration
  takes, or over what distance), what fraction of the muons survive to reach
  collision energy?
- How does the surviving fraction depend on how quickly you accelerate them?
  What does this tell you about the engineering challenge of a muon collider?

This is the same physics you used for the B meson, applied at a completely
different scale, and it shows why "how fast can we accelerate them" is a central
design question for such a machine.

---

## Final deliverables

Submit the following:

- A plot of B meson mean decay length versus energy
- A toy Monte Carlo of the decay distribution, including the mean check and the
  fitted lifetime
- A clean Python notebook or script
- A short written explanation of the science behind the project

Optional bonus deliverables:

- A plot of LLP decay fractions by detector region as a function of lifetime,
  with a discussion of where to search
- A calculation of muon survival fraction for a muon collider, with a
  discussion of the acceleration requirement

---

## What a successful project should demonstrate

A successful project does not need to be complicated. It should be clear,
correct, and well explained.

By the end, you should be able to say:

- I understand that a particle's lifetime is probabilistic, and I can explain
  what that means.
- I can relate particle lifetime to the more familiar idea of half-life.
- I understand how special relativity turns a fixed rest-frame lifetime into an
  energy-dependent distance in the laboratory, and why there is no "proper
  distance traveled."
- I can compute and plot how far a B meson typically travels, and connect that
  to the real geometry of a detector like CMS.
- I understand why the b quark's lifetime is what makes b-tagging possible.
- I can build a toy Monte Carlo, check its mean against theory, and fit it to
  recover the input lifetime.
- I can use Python to create clear scientific plots and simulations.

The goal is not just to make a plot. The goal is to use these calculations and
simulations to understand how a deeply quantum, probabilistic property of
matter becomes something an experiment can measure.
