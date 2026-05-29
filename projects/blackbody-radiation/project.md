---
title: "Understanding Blackbody Radiation with the Cosmic Microwave Background"
pi: "darcybarron"
goals:
  - "Learn to read in data files and interpret and visualize them"
  - "Simulate a blackbody spectrum and understand its shape and how it changes with temperature"
  - "Understand units and conversions needed to go from observed flux to an object's physical temperature"
  - "Fit a measured cosmic microwave background spectrum from the COBE FIRAS instrument to an ideal blackbody with a single free parameter, temperature"
---

# Research Project: Understanding Blackbody Radiation with the Cosmic Microwave Background

## Project overview

In this project, you will investigate one of the most famous data sets in the history of cosmology: the measurement of the Cosmic Microwave Background (CMB) by the Far-Infrared Absolute Spectrophotometer (FIRAS) instrument aboard NASA's Cosmic Background Explorer (COBE) satellite.

In the early 1990s, COBE FIRAS measured the spectrum of the relic radiation left over from the Big Bang. The result was stunning—an almost flawless match to an ideal thermal radiator, or blackbody. This discovery confirmed a core prediction of the Big Bang theory and earned the investigators a Nobel Prize.

Your main goal is to write a Python program that reads the original COBE FIRAS data file, models the theoretical spectrum of a blackbody using Planck's Law, and performs a single-parameter fit to determine the precise temperature of the universe. This project combines data analysis, scientific programming, and fundamental thermodynamics.

This project is designed for beginning physics, astronomy, or astrophysics students. You are not expected to be an expert in statistical fitting or observational cosmology at the start. By the end, you will understand how to connect raw, real-world spacecraft observations to fundamental physical constants and parameters.

## Core idea

An ideal blackbody emits electromagnetic radiation with a spectral radiance determined entirely by its temperature. This relationship is governed by Planck's Law.

Your task is to acquire the historical COBE FIRAS data spectrum, explore how the shape of a blackbody curve scales with temperature, and write an optimization routine to find the exact temperature $T$ that minimizes the differences between theory and observation.

The FIRAS data points are so precise that their error bars are smaller than the thickness of the line on a standard plot. Your analysis will verify this precision by evaluating the fit residuals and examining the statistical "goodness of fit."

## Required products

At the end of the project, you should produce:

- **A static plot of the CMB spectrum with the best-fit model**
This should display the raw COBE FIRAS data points (with error bars) overlaid with your best-fit theoretical Planck curve. The final calculated temperature should be clearly displayed in the plot's legend or title with appropriate units.
- **A static plot of the fit residuals**
This should plot the difference between the observed data and your theoretical model ($\text{Data} - \text{Model}$) as a function of frequency or wavenumber. This plot is essential for visualizing whether systemic deviations exist or if the noise is purely statistical.
- **A parameter space or $\chi^2$ plot**
This plot should show the value of your fit metric (such as the sum of squared residuals or $\chi^2$) as a function of the trial temperature $T$. This helps visualize how the optimization algorithm finds the true minimum.
- **A short written explanation**
This should explain what your code and plots show. It should describe the physical meaning of a blackbody spectrum, explain why the CMB exhibits this shape, and interpret the scale of the residuals you discovered.
- **A clean Python notebook or script**
This should handle the data ingestion, unit conversions, model evaluation, optimization, and plotting. The code must be clean, readable, well-commented, and easily reusable by another peer.

## Suggested workflow

### Step 1: Learn the basic vocabulary

Before diving into code, ensure you are comfortable with the following terms:

- Blackbody radiation
- Thermal equilibrium
- Planck's Law
- Spectral radiance / intensity
- Wavenumber ($\tilde{\nu}$) vs. Frequency ($\nu$)
- COBE FIRAS
- Monopole temperature
- Residuals
- Chi-squared ($\chi^2$) minimization

You do not need to memorize every statistical proof, but you should understand how these concepts fit together to let you extract physical truths from experimental noise.

### Step 2: Master the physics and unit conversions

Look up Planck's Law for spectral radiance. Note that experimental data from FIRAS is typically provided in terms of **wavenumber** $\tilde{\nu}$ (expressed in units of $\text{cm}^{-1}$) and intensity in units of MegaJy per steradian ($\text{MJy/sr}$).

Planck's Law expressed in terms of frequency $\nu$ is:

$$B_\nu(\nu, T) = \frac{2h\nu^3}{c^2} \frac{1}{e^{\frac{h\nu}{k_B T}} - 1}$$

You will need to adapt this formula to use wavenumber $\tilde{\nu}$ (where $\nu = c\tilde{\nu}$) and convert your theoretical output units to match the $\text{MJy/sr}$ of the data file. Track your physical constants ($h, c, k_B$) carefully; a single unit or exponent error will shift your temperature by orders of magnitude.

### Step 3: Read and visualize the COBE FIRAS data

Locate and download the official public COBE FIRAS monopole spectrum data file. Use Python libraries like `numpy` or `pandas` to read the columns. Typically, the file will include columns for:

1. Wavenumber
2. Monopole flux (or intensity)
3. Residual galaxy spectrum (or uncertainties)
4. Standard deviation (error bars)

Make an initial scatter plot of the raw data points to understand the frequency range and shape of the spectrum before trying to fit it.

### Step 4: Construct the theoretical blackbody function

Write a clean Python function `planck_wavenumber(wavenumber, T)` that returns the theoretical intensity for a given array of wavenumbers and a target temperature $T$.

Test your function by plotting a few trial temperatures (e.g., $2.0\text{ K}$, $3.0\text{ K}$, $4.0\text{ K}$) on top of your raw data to see how the curve shifts its peak and amplitude as temperature changes.

### Step 5: Implement the single-parameter fit

To find the exact temperature, you need to minimize the differences between the experimental data points and your Planck model. Define a metric for the goodness of the fit, such as the chi-squared statistic:

$$\chi^2 = \sum \left( \frac{\text{Data}_i - \text{Model}_i(T)}{\sigma_i} \right)^2$$

Where $\sigma_i$ is the experimental uncertainty for each data point. Write a loop or use an optimization routine (like `scipy.optimize.minimize` or `curve_fit`) to find the exact value of $T$ that yields the lowest possible value for this metric.

### Step 6: Create the final diagnostic plots

Generate your final publication-ready figures. Make sure your plots feature:

- Clear axis labels with explicit units (e.g., Wavenumber [$\text{cm}^{-1}$], Intensity [$\text{MJy/sr}$]).
- A residual plot positioned beneath or alongside the primary spectrum plot to clearly display the scale of the deviations.
- Consistent, high-contrast color choices.

### Step 7: Write the explanation

Your written summary should document your findings and interpret the underlying physics. Address questions such as:

- What temperature did your code calculate for the CMB? How close is it to the accepted literature value?
- Why does the cosmic microwave background possess such a perfect blackbody spectrum? What does this tell us about the early universe?
- What did you notice about the scale of the residuals compared to the absolute intensity of the spectrum?
- What was the most challenging unit conversion or programming hurdle you faced, and how did you resolve it?

## Stretch goal 1: Formal uncertainty estimation

In the core project, you find the single best-fit temperature value. For an added challenge, determine the *uncertainty* ($\pm \sigma$) of your fitted temperature.

You can achieve this by mapping out the $\chi^2$ curve precisely around your minimum value. In a single-parameter fit, the formal $1\sigma$ standard error corresponds to the change in temperature required to increase the $\chi^2$ value by exactly $1$ from its minimum ($\Delta\chi^2 = 1$).

Alternatively, extract the covariance matrix from your numerical fitting software. State clearly how you calculated your error bounds and express your final temperature with its formal experimental uncertainty (e.g., $T \pm \Delta T$).

## Stretch goal 2: Cosmological redshift and scaling

The temperature you calculated is the temperature of the CMB *today*. Because the universe is expanding, the wavelength of this radiation stretches over time, cooling the blackbody spectrum.

Investigate how the temperature of the CMB scales as a function of cosmological redshift ($z$).

1. Write down the analytical relationship between temperature $T$ and redshift $z$.
2. Calculate what the temperature of the universe was at the epoch of recombination/decoupling ($z \approx 1100$), when the CMB photons first broke free.
3. Use your code to simulate and plot what the CMB blackbody curve would look like to an observer living at $z = 2$, $z = 5$, and $z = 10$.

## Final deliverables

Submit the following:

- Combined static plot showing the data, best-fit blackbody curve, and fit residuals.
- Static plot of the optimization landscape ($\chi^2$ vs. $T$).
- Clean, well-commented Python notebook or script that executes entirely without errors.
- Short written report addressing the physical interpretation and analysis questions.

Optional bonus deliverables:

- Error estimation analysis displaying your calculated $\pm \sigma$ uncertainties.
- A plot showing the calculated historical evolution of the CMB spectrum at higher redshifts.

## What a successful project should demonstrate

A successful project should show technical accuracy, computational clarity, and analytical depth. By the conclusion, you should be able to confidently state:

- I can parse, process, and clean real archival astrophysics data files within a Python environment.
- I understand the mathematical and physical structure of Planck's Law and how its shape reacts to temperature variations.
- I can confidently execute unit conversions across frequencies, wavelengths, wavenumbers, Jy, and SI energy units.
- I understand how an optimization algorithm uses a loss function ($\chi^2$) to locate a physical parameter value.
- I can interpret fit residuals to judge the quality and validity of an experimental model.
- I can explain the profound historical and physical significance of the COBE FIRAS measurement to another student.

