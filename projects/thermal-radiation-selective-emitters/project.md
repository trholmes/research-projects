---

title: "Thermal Radiation and Selective Emitters"
pi: "foleylab"
goals:

* "Implement Planck's blackbody law numerically in Python"
* "Verify Wien's displacement law using numerical peak finding"
* "Verify Stefan-Boltzmann scaling using numerical integration"
* "Model wavelength-dependent emissivity functions"
* "Analyze how selective emitters differ from ideal blackbodies"
* "Determine whether a monochromatic thermal emitter obeys Wien's displacement law or Stefan-Boltzmann scaling"

---

# Thermal Radiation and Selective Emitters

## Overview

Thermal radiation is one of the foundational topics connecting statistical mechanics, quantum mechanics, optics, and materials physics. In this project, students will explore how thermal emission depends on temperature, first for ideal blackbody emitters and then for non-ideal selective emitters.

Students will implement numerical models of Planck’s blackbody radiation law in Python and use these models to investigate two major results:

1. **Wien’s displacement law**, which predicts that the peak emission wavelength scales inversely with temperature.
2. **The Stefan-Boltzmann law**, which predicts that the total emitted power scales as (T^4).

After reproducing these classical results numerically, students will extend the model to materials with wavelength-dependent emissivity functions.

The project culminates in an investigation of an extreme selective emitter: a monochromatic emitter modeled using a delta-function emissivity. Students will determine whether such an emitter obeys Wien’s displacement law and Stefan-Boltzmann scaling.

---

# Scientific Background

The spectral radiance of an ideal blackbody is given by Planck’s law:

[
B(\lambda,T)
============

\frac{2hc^2}{\lambda^5}
\frac{1}{e^{hc/(\lambda k_B T)}-1}
]

where:

* (h) is Planck’s constant,
* (c) is the speed of light,
* (k_B) is Boltzmann’s constant,
* (\lambda) is wavelength,
* (T) is temperature.

The total emitted power density of a blackbody obeys the Stefan-Boltzmann law:

[
P = \sigma T^4
]

and the wavelength of maximum emission obeys Wien’s displacement law:

[
\lambda_{\mathrm{max}} T = b
]

where (b) is Wien’s displacement constant.

Real materials are not perfect blackbodies. Their thermal emission depends on a wavelength-dependent emissivity function (\epsilon(\lambda)):

[
P(T)
====

\pi
\int_0^\infty
\epsilon(\lambda)
B(\lambda,T)
d\lambda
]

This project investigates how changing the emissivity function changes the scaling behavior of thermal emission.

---

# What Students Will Do

## Part 1: Implement Planck’s Law

Students will:

* implement Planck’s law in Python,
* generate spectra over a grid of wavelengths and temperatures,
* visualize blackbody emission curves.

Suggested temperatures include:

* 300 K
* 3000 K
* 6000 K
* 40000 K

Students should create plots showing how the spectrum shifts and increases with temperature.

---

## Part 2: Verify Wien’s Displacement Law

Students will numerically determine the wavelength of maximum emission for each temperature.

Possible approaches include:

* direct numerical peak finding,
* interpolation,
* comparison with analytic expectations.

Students should verify that:

[
\lambda_{\max} \propto \frac{1}{T}
]

and compare their numerical results with Wien’s displacement law.

---

## Part 3: Verify Stefan-Boltzmann Scaling

Students will numerically integrate the blackbody spectrum over wavelength to compute total emitted power.

They should then determine how total power depends on temperature and verify that:

[
P \propto T^4
]

Possible numerical methods include:

* trapezoidal integration,
* Simpson’s rule,
* numerical quadrature routines from SciPy.

---

## Part 4: Introduce Selective Emitters

Students will next modify the model to include emissivity functions.

Examples may include:

* constant emissivity,
* Gaussian emitters,
* narrow-band emitters,
* step-function emissivities.

The emitted spectrum becomes:

[
I(\lambda,T)
============

\epsilon(\lambda) B(\lambda,T)
]

Students should investigate how emissivity changes both the shape of the spectrum and the total emitted power.

---

## Part 5: Monochromatic Thermal Emitters

Finally, students will investigate an extreme case:

[
\epsilon(\lambda)
=================

\delta(\lambda-\lambda_0)
]

where the emitter radiates only at a single wavelength.

Students should determine:

1. Does the peak wavelength shift with temperature?
2. Does the total emitted power obey Stefan-Boltzmann scaling?
3. How does the power scale with temperature at fixed wavelength?

Students may investigate this either numerically or analytically.

A useful expression for the emitted power is:

[
P(T)
====

\pi
\frac{2hc^2}{\lambda_0^5}
\frac{1}{e^{hc/(\lambda_0 k_B T)}-1}
]

Students should compare the resulting temperature dependence with the usual (T^4) scaling of blackbodies.

---

# Suggested Deliverables

A successful project may include:

* Python scripts or notebooks implementing the calculations,
* plots of blackbody spectra,
* numerical verification of Wien’s law,
* numerical verification of Stefan-Boltzmann scaling,
* analysis of selective emitters,
* a short written discussion comparing blackbody and monochromatic emitters.

---

# Possible Extensions

Students interested in extending the project could investigate:

* realistic emissivity spectra of materials,
* infrared selective emitters,
* thermophotovoltaic emitters,
* radiative cooling materials,
* photonic crystal thermal emitters,
* numerical stability and integration accuracy,
* dimensional analysis of thermal radiation laws.

