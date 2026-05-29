---
title: "Model the effects of dust on astrophysical spectra"
pi: "eblur"
goals:
  - "Understand the properties of dust extinction curves and the underlying assumptions"
  - "Understand how dust attenuates astrophysical light sources like stars and galaxies"
  - "Understand how to modify model spectra to include extinction effects from dust"
---

# Project description

This undergraduate research project introduces students to computational astrophysics by modeling how interstellar dust attenuates light from stars and galaxies. Students will use Python to apply dust extinction curves to theoretical and observed spectra, gaining hands-on experience with fundamental concepts in observational astronomy and scientific computing.

By completing this project, students will:
- Understand dust attenuation physics – Learn how interstellar dust absorbs and scatters astrophysical light, modifying the observed spectral energy distribution of stars and galaxies.
- Apply extinction corrections – Gain practical skills in modifying model spectra to include dust extinction effects using standard extinction laws.
- Analyze extinction curve properties – Explore the wavelength-dependent nature of dust extinction, compare different extinction curves (e.g., Milky Way, LMC, SMC), and understand the physical assumptions underlying each model.

## Background Theory

### Dust Extinction Fundamentals

Interstellar dust consists of small solid particles (silicates, carbonaceous grains, icy grains) that interact with electromagnetic radiation through absorption and scattering. The effect is wavelength-dependent, typically strongest and UV and optical wavelengths, causing:
- Dimming – Overall reduction in flux
- Reddening – Preferential attenuation of blue light relative to red light

### Extinction Curves

An extinction curve describes the ratio of extinction at wavelength λ to extinction in the V-band (A_λ/A_V). The extinction at a given wavelength is typically expressed as:

A(λ) = A_V × k(λ)

where k(λ) is the normalized extinction curve and A_V is the visual extinction.

## Methodology

**Phase 1: Setup and Data Acquisition**
- Install Python environment (NumPy, SciPy, Matplotlib, Astropy)
- Download or generate template stellar/galaxy spectra using psynphot or using astroquery to get real spectra from the SDSS SkyServer

**Phase 2: Implementing Extinction Models**
- Load extinction curve models using the Python package dust_extinction
- Plot A(λ) for different extinction laws
- Apply extinction to model spectra: F_observed(λ) = F_intrinsic(λ) × 10^(-0.4 × A(λ))
- Create visualization tools to compare extincted vs. intrinsic spectra

**Phase 3: Analysis and Exploration**
- Vary extinction parameters (A_V, R_V) and observe effects
- Compare different extinction curves on the same spectrum
- Investigate how dust affects derived quantities (colors, star formation rates, metallicities)

## Deliverables

- Working Python code – Well-documented scripts/functions implementing extinction models
- Visualization figures – Plots showing extinction effects across wavelength ranges
- Short report (3–5 pages) covering:
   - Methods implemented
   - Results and interpretation
   - Comparison of extinction curve behaviors
   - Limitations and assumptions identified

**Assessment Criteria**
- Code quality and documentation (25%)
- Correct implementation of extinction physics (30%)
- Quality of visualizations (20%)
- Analysis depth and critical thinking (25%)

## Pedagogical Notes

This project is designed to develop:
- Computational literacy – Python programming, numerical methods, data visualization
- Scientific reasoning – Understanding model assumptions, interpreting physical effects
- Research skills – Literature review, reproducibility, documentation

