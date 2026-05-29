---
title: "Understanding Particle Lifetime"
pi: "trholmes"
goals:
  - "Understand what it means for a particle to have a lifetime and why it is probabilistic"
  - "Distinguish between detecting particles directly and inferring them from decay products"
  - "Connect particle lifetime to laboratory decay distance through special relativity"
  - "Understand why b-quark lifetime makes b-tagging possible, and why that matters for the Higgs"
  - "Produce a plot of B meson decay length as a function of energy"
  - "Use toy Monte Carlo to produce a full decay distribution and recover the lifetime from it"
  - "Apply the same physics to long-lived particle (LLP) searches and identify optimal search strategies as a function of lifetime"
---

# Research Project: Understanding Particle Lifetime

## Project overview

In this project, you will build up an understanding of what it means for a
particle to have a *lifetime*, and you will turn that understanding into
concrete calculations and plots that connect directly to how experiments at
the Large Hadron Collider (LHC) actually work.

The organizing question of this project is simple but deep: when a particle is
produced in a collision, how does an experiment know it was there? For some
particles — stable ones like electrons or photons — the answer is direct: they
travel through the detector and leave signals. For unstable particles, the
answer is more subtle. You cannot see them directly; you have to infer their
existence from the particles they decay into. And a particle's **lifetime** is
what determines which of these two strategies applies — and whether an
experiment can detect the particle at all.

You will follow this idea from its most basic form through to research-level
applications. Starting with the LHC and its detectors, you will develop a
working understanding of particle lifetime as a probabilistic quantity, connect
it to laboratory decay distance through special relativity, and apply it to the
b quark — whose lifetime is why the Higgs decay \(H \to b\bar{b}\) can be
studied at all. You will produce a plot of how far a B meson typically travels
as a function of its energy, build a **toy Monte Carlo** to simulate the full
distribution of decay distances, and then apply the same physics framework to
searches for hypothetical long-lived particles (LLPs) beyond the Standard
Model, reasoning about which search strategy makes sense for which lifetime.

This project is designed for beginning physics students as a first project in
particle physics. You are not expected to know any particle physics or special
relativity at a research level when you start. By the end, you should be able
to explain what a particle lifetime is, why it is probabilistic, how relativity
stretches it out in the laboratory, why the b quark's lifetime makes it
detectable, and how the same reasoning applies to BSM searches. You will also
strengthen your ability to use Python for scientific calculation, simulation,
and plotting.

### Working at different levels

Students arrive at this project with very different backgrounds, and that is
expected. Two prerequisites do most of the work here: a little **special
relativity** (just time dilation) and a little **scientific Python** (NumPy,
Matplotlib, and one curve fit). You do not need either in advance — both have
on-ramps built into the project:

- Step 5 begins with a self-check on special relativity and points you to a
  single section of reading if you need it.
- Step 8 (the simulation) is where the most Python is required; `resources.md`
  lists the three libraries you need and beginner-friendly tutorials for each.

If a concept is already familiar, move through that step quickly — the "check
your understanding" questions are a fast way to confirm you can skip ahead. If
a concept is new, slow down and use the linked resource before continuing; the
steps are ordered so that nothing later depends on something you skipped. The
core physics path runs through Step 8. Steps 9–11 and the stretch goal go
further into real research questions, and are the natural place for stronger
students to spend extra time.

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

### Step 1: The LHC, particle collisions, and detectors

Before anything else, build a working picture of the experimental setting this
project lives in.

Read enough about the LHC and its experiments (see `resources.md`) to be able
to describe:

- what the LHC is: a circular accelerator that brings two beams of protons to
  very high energies and causes them to collide
- roughly what energies are involved (the LHC currently runs at 13–14 TeV
  center-of-mass energy), and what a "collision event" means
- what the ATLAS and CMS detectors are: large, layered instruments built
  concentrically around the collision point, designed to reconstruct the
  particles produced in each collision

A detector like CMS has several distinct layers, moving outward from the
collision point: a silicon pixel tracker, a silicon strip tracker, an
electromagnetic calorimeter, a hadronic calorimeter, and muon chambers
embedded in an iron return yoke. Each layer is sensitive to different kinds of
particles and serves a different role in reconstructing what happened in the
collision.

Now comes the central question of this whole project. When particles are
produced in a collision, there are two fundamentally different ways a detector
can learn about them:

1. **Direct detection:** a stable (or very long-lived) particle travels through
   the detector and deposits energy directly. Photons, electrons, muons, and
   hadrons can all be detected this way.

2. **Inference from decay products:** an unstable particle does not live long
   enough to reach the sensitive parts of the detector. Instead, it decays, and
   what the detector actually sees are the daughter particles from that decay.
   You infer that the parent particle existed by reconstructing the decay.

This distinction is not a technical detail. It shapes every analysis strategy
in experimental particle physics. Notice that in the second case, the
particle's **lifetime** is what determines whether the decay happens inside the
detector, outside it, or somewhere interesting in between.

Check your understanding before moving on:

- Name one particle that can be detected directly and one that must be inferred
  from its decay products. Why does each fall into its category?
- A particle is produced at the collision point. It is unstable, but its
  lifetime is so short that it decays before traveling even a fraction of a
  millimeter. Can its daughter particles still be detected? How?
- A particle's lifetime is so long that it almost always escapes the entire
  detector before decaying. How does the experiment know it was there at all?
- What is it about "intermediate" lifetimes that makes them the most
  interesting case for experimental reconstruction?

### Step 2: Understand lifetime as a probabilistic quantity

With the experimental setting established, you are ready to think carefully
about what "lifetime" means for a particle.

You may already have met the idea of a **half-life** when learning about
radioactive isotopes. A sample of a radioactive isotope does not all decay at
once; instead, after one half-life, half of it remains, after two half-lives a
quarter remains, and so on. Particle lifetimes work the same way: if you
prepare a large number \(N_0\) of identical particles, the number still
surviving after a proper time \(t\) follows

\[
N(t) = N_0 \, e^{-t/\tau},
\]

where \(\tau\) is the **mean lifetime** measured in the particle's own rest
frame. The relationship between the mean lifetime and the half-life is

\[
t_{1/2} = \tau \ln 2.
\]

The crucial conceptual point is this: you cannot predict when a *single*
particle will decay. A given particle might decay almost immediately, or it
might last much longer than average. What is predictable is the *shape* of the
distribution for a large ensemble: an exponential, governed by the single
number \(\tau\).

This is not a statement about our ignorance or our equipment. It is a
fundamental feature of quantum mechanics. Quantum mechanics generally tells you
the probabilities of outcomes, not the outcome of any single measurement.

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
- Returning to Step 1: if a particle has a very short lifetime (much less than
  a nanosecond), does it fall into the "direct detection" or "inference from
  decay products" category? What about a particle with a lifetime of microseconds?

### Step 3: Get oriented with fundamental particles

Now that you have the experimental context and a grasp of what lifetime means,
build up a picture of the particle landscape you will be working in.

Spend some time with the recommended reading (see `resources.md`) to get
comfortable with:

- the idea of a *fundamental* particle (quarks, leptons, gauge bosons, the
  Higgs)
- the difference between fundamental particles and *composite* particles such
  as protons, neutrons, and mesons
- the Particle Data Group (PDG) as the standard reference for particle
  properties such as masses and lifetimes — you will use it repeatedly

It is worth holding the label "fundamental" with a little healthy skepticism.
What counts as fundamental has changed repeatedly throughout the history of
physics. Treat it as "fundamental as far as we can currently tell."

You do not need to master any of this. The goal is to have enough vocabulary to
proceed to the next step.

### Step 4: B quarks, B mesons, and why they matter for the Higgs

Now you are ready to meet the particle that is the main character of this
project, but for a specific reason: it is essential for studying the Higgs
boson.

The **Higgs boson** is the most recently discovered fundamental particle in the
Standard Model, observed at the LHC in 2012. Its most common decay is into a b
quark and an anti-b quark (\(H \to b\bar{b}\)), occurring about 58% of the
time. That means the ability to identify b quarks is essential for studying the
Higgs. This is the physics motivation for everything that follows.

But here is the complication: you do not detect the b quark directly. A b
quark *hadronizes*, meaning it quickly combines with other quarks to form a B
hadron (such as a B meson) almost immediately after being produced. That B
meson is unstable and eventually decays into lighter particles.

Now recall the two detection strategies from Step 1: direct detection versus
inference from decay products. Which one applies to the B meson?

The answer is: B mesons fall into a particularly fortunate intermediate case.
Their lifetime (\(\tau \sim 1.5 \times 10^{-12}~\mathrm{s}\), i.e. about 1.5
picoseconds) is short enough that they decay inside the detector, but long
enough that they travel a small but **measurable** distance before decaying.
This distance is typically a few millimeters — just large enough for a
precision silicon tracker to resolve. The decay point is then displaced from
the original collision point, forming a **secondary vertex**.

Reconstructing that secondary vertex from the tracks of the decay products is
the basis of **b-tagging**: the technique by which LHC experiments identify
jets that contain a b quark, and the reason the Higgs decay \(H \to b\bar{b}\)
can be studied at all.

Make sure you can answer:

- Why can't we detect the b quark itself directly?
- What does it mean for a quark to hadronize?
- What is a secondary vertex, and why does the b quark's lifetime make one
  possible?
- Why would b-tagging be impossible if the B meson lifetime were a thousand
  times shorter? What if it were a thousand times longer?
- Why does finding \(H \to b\bar{b}\) decays require b-tagging?

### Step 5: Lab frame versus proper frame, and a hand calculation

Before diving in, a quick check: this step requires special relativity —
specifically time dilation and the Lorentz factor \(\gamma\). Have you seen
these before?

- **If yes** and you are comfortable with \(\gamma = 1/\sqrt{1-\beta^2}\) and
  why a moving particle's clock runs slow, proceed directly.
- **If no**, or if you have seen it but it feels shaky, read
  [OpenStax University Physics Vol. 3, Section 5.3 (Time Dilation)](https://openstax.org/books/university-physics-volume-3/pages/5-3-time-dilation)
  before continuing. The key idea is in that one section; the rest of Chapter 5
  is useful context but not required for this step.

The minimum you need: a particle moving at speed \(\beta c\) has its internal
clock slowed by a factor \(\gamma\), so a rest-frame lifetime \(\tau\) becomes
a lab-frame lifetime \(\gamma\tau\). That is all the relativity this step uses.

Now, before plotting anything, do one calculation by hand so the later code has
something to check against.

One convention to settle first: particle physicists work in **natural units**,
where \(c = 1\) and mass, momentum, and energy are all quoted in GeV. That is
why we can write "a B meson of momentum \(p = 50~\mathrm{GeV}\)" and why
\(\beta\gamma = p/(Mc)\) simplifies to \(\beta\gamma = p/M\), just a ratio of
two numbers in GeV. If that looks odd to you (momentum in energy units?), it is
a deliberate, standard convention — see the short "natural units" note in
`resources.md` before proceeding.

Look up (and record in `resources.md`) the B meson's mass \(M \approx
5.28~\mathrm{GeV}\) and its decay length \(c\tau\), which is roughly half a
millimeter (about \(0.5~\mathrm{mm}\); look up the precise value for the
specific B meson you choose, since they differ slightly). Then, for an example
momentum, say \(p = 50~\mathrm{GeV}\), compute:

1. \(\beta\gamma = p / (Mc) = p / M\) in natural units,
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

### Step 6: Plot the average decay length versus energy

Now reproduce, in code, the relationship you just calculated by hand.

Make a plot of the mean laboratory decay length \(L = \beta\gamma c\tau\) as a
function of the B meson's energy (or momentum). Iterate on it until you are
confident it is correct:

- Mark your hand-calculated point from Step 5 on the curve and confirm it lands
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

### Step 7: From the average to the full distribution

The plot in Step 6 shows only the *mean* decay length. But you already know
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
from Step 6. Make sure you can explain in words why this fraction is so small,
and how it depends on energy.

### Step 8: Build a toy Monte Carlo

A **toy Monte Carlo** is a simple simulation that generates pseudo-random
"events" according to a known probability distribution, so you can study the
distribution by sampling from it rather than only by calculating with formulas.
It is one of the most common tools in experimental particle physics, and this
project is a good first place to learn it.

This is the step that uses the most Python: random sampling, histogramming, and
a curve fit. If you are comfortable with NumPy and `scipy.optimize.curve_fit`,
proceed directly. If any of those are new, see the "Computational tools" note
in `resources.md` for the three libraries you need and short tutorials for
each — it is worth a few minutes there before you start coding.

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

### Step 9: Long-lived particles and BSM searches

So far you have studied the B meson, a particle we already know exists. But
particle physicists also search for hypothetical particles predicted by theories
that go beyond the Standard Model (BSM theories). Many such theories predict
new particles with lifetimes far longer than the B meson's — particles that
could travel centimeters, meters, or even further before decaying. These are
called **long-lived particles (LLPs)**.

Return to the framing from Step 1. The same two detection strategies apply here:

- **Direct detection:** if an LLP is stable enough to reach the calorimeters or
  muon systems, it may deposit energy directly, much like a known stable
  particle would.
- **Inference from decay products:** if an LLP decays inside the tracking
  volume, you cannot see the LLP itself — you reconstruct it from its
  displaced decay products, exactly as with the B meson but potentially with
  a much larger displacement.

And there is a third regime unique to very long lifetimes: the particle escapes
the detector entirely without decaying, leaving only **missing transverse
energy** (MET) as evidence. This is how we search for particles that interact
only weakly with matter (like dark matter candidates).

The challenge for LLP searches is that the optimal detection strategy depends
strongly on where the LLP actually decays, which depends on its lifetime. Using
the probability formula from Step 7, investigate this quantitatively.

The probability of decaying within a detector shell between radii \(r_1\) and
\(r_2\) is

\[
P(r_1 < L < r_2) = e^{-r_1/(\beta\gamma c\tau)} - e^{-r_2/(\beta\gamma c\tau)} .
\]

To make this a well-defined question, fix the LLP's kinematics and vary only
its lifetime. Choose a representative mass and momentum for X (state your
choice), which fixes \(\beta\gamma = p/M\), and then sweep \(c\tau\) over a wide
range — from well below a millimeter to well above the size of the detector
(many orders of magnitude, so use a logarithmic axis).

Make a plot showing, as a function of the LLP's \(c\tau\) (or lifetime), what
fraction of decays fall in different detector regions: inside the tracker,
between the tracker and calorimeter, in the calorimeter, and outside the
detector entirely (i.e., the "escaping" fraction). Use the approximate
subdetector outer radii tabulated in `resources.md`.

Check your understanding:

- For a very short \(c\tau\) (much less than a millimeter), where do most
  decays happen? Does the "direct detection vs. decay products" framing still
  apply, or does a new regime emerge?
- For a very long \(c\tau\) (many meters), what does the detector mostly "see"?
- At what \(c\tau\) range is the tracker the most useful subdetector for
  finding LLP decays?
- At what \(c\tau\) range does the calorimeter or muon system become the best
  place to look?

### Step 10: Which search strategy makes sense when?

You now have all the pieces to think about LLP search design as a physicist
would. The same question that structured the whole project — direct measurement
versus inference from decay products — now becomes a practical question about
where to spend your analysis effort.

Consider an experiment that discovers a new signal with an unknown particle X
at an unknown mass and lifetime. Think through the following scenarios:

- **Scenario A:** X has \(c\tau \sim 1~\mathrm{mm}\). Where does it decay? Can
  you reconstruct a secondary vertex? Is direct detection relevant? What search
  strategy would you design?

- **Scenario B:** X has \(c\tau \sim 1~\mathrm{m}\). Now where does it mostly
  decay? How does your strategy change? What subdetectors become important?

- **Scenario C:** X has \(c\tau \gg 100~\mathrm{m}\). What does the detector
  see? How do you search for X if it almost never decays inside the detector?

- **Scenario D:** You do not know X's lifetime ahead of time. You need to
  design a search that is sensitive across a wide range. What challenges does
  this pose? What could you do?

For each scenario, explain which detection strategy you would use and why, and
connect your reasoning to the calculations you made in Steps 6–9. There is no
single right answer to the design question; the goal is to reason carefully
from the physics.

### Step 11: Write the explanation

Your short written explanation should describe not just what you did, but what
you learned. It should answer questions such as:

- What is a particle lifetime, and in what sense is it probabilistic?
- How are lifetime and half-life related?
- How does the laboratory decay length depend on the particle's energy, and
  why?
- What is the difference between the rest frame and the laboratory frame, and
  why is there no meaningful "proper distance traveled"?
- How do experiments use the b quark's lifetime to identify it, and why is this
  essential for studying the Higgs boson?
- What did your toy Monte Carlo teach you that the average value alone did not?
- How does the LLP search strategy depend on the particle's lifetime, and which
  subdetector is most useful in which regime?

---

## Stretch goal: Muons at a muon collider

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
- A plot of LLP decay fractions by detector region as a function of lifetime
- A written discussion of LLP search strategies in each lifetime regime
- A clean Python notebook or script
- A short written explanation of the science behind the project

Optional bonus deliverable:

- A calculation of muon survival fraction for a muon collider, with a
  discussion of the acceleration requirement (see the stretch goal above)

---

## What a successful project should demonstrate

A successful project does not need to be complicated. It should be clear,
correct, and well explained.

By the end, you should be able to say:

- I understand that a particle's lifetime is probabilistic, and I can explain
  what that means.
- I can relate particle lifetime to the more familiar idea of half-life.
- I understand the difference between detecting a particle directly and
  inferring its existence from its decay products, and I can explain which
  strategy applies in which situation.
- I understand how special relativity turns a fixed rest-frame lifetime into an
  energy-dependent distance in the laboratory, and why there is no "proper
  distance traveled."
- I can compute and plot how far a B meson typically travels, and connect that
  to the real geometry of a detector like CMS.
- I understand why the b quark's lifetime is what makes b-tagging possible, and
  why b-tagging matters for studying the Higgs boson.
- I can build a toy Monte Carlo, check its mean against theory, and fit it to
  recover the input lifetime.
- I can explain why the optimal LLP search strategy depends on the particle's
  lifetime, and identify which detector region is most useful in which regime.
- I can use Python to create clear scientific plots and simulations.

The goal is not just to make a plot. The goal is to use these calculations and
simulations to understand how a deeply quantum, probabilistic property of
matter becomes something an experiment can measure — and to see how the same
physics reasoning applies across a wide range of experimental questions, from
Standard Model measurements to searches for new physics.
