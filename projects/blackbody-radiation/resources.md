# Recommended resources

These are the recommended readings and references for the  
*Understanding Blackbody Radiation with the Cosmic Microwave Background* project. They support the physics and analysis background you will need for the calculations and the written explanation.

## Primary resources

- **NASA LAMBDA (Legacy Archive for Microwave Background Data Analysis)**
  - *Resource Link:* [lambda.gsfc.nasa.gov](https://lambda.gsfc.nasa.gov/)
    - This is the official repository for CMB measurements and so hosts the historical data files for COBE FIRAS.  The specific dataset needed is the *FIRAS Monopole Spectrum* (typically available as a clean ASCII text file or FITS table), which includes columns for wavenumber, monopole intensity, and $1\sigma$ uncertainty bars.
- **NASA COBE Mission Science Page**
  - *Resource Link:* [science.nasa.gov/mission/cobe](https://science.nasa.gov/mission/cobe/)
    - Reading the mission overview gives students vital historical and operational context. It explains the design of the Michelson interferometer used by FIRAS, and how the instrument calibrated itself against an internal blackbody simulator.
- *Measuring the Universe: A Multiwavelength Perspective* by George H. Rieke
  - This textbook includes fundamentals of astronomical instrumentation and the physical concepts of measurement, sensitivity and noise.

## Additional useful resources

### Astropy Documentation

Astropy is essential for handling the domain-specific nuances of astronomical units and constants without hardcoding fragile conversion metrics.

- `astropy.units` **and** `astropy.constants`
  - *Documentation:* [docs.astropy.org/en/stable/units/](https://docs.astropy.org/en/stable/units/)
  - *Why it helps:* Planck's law requires physical constants ($h, c, k_B$). Importing `astropy.constants.h` ensures maximum scientific precision. Furthermore, the `astropy.units` package handles the conversion from the data's arbitrary intensity units ($\text{MJy/sr}$) back into standard SI or CGS energy distributions seamlessly.
- **Astropy Unit Equivalencies (Spectral Equivalencies)**
  - *Documentation:* [docs.astropy.org/en/stable/units/equivalencies.html](https://docs.astropy.org/en/stable/units/equivalencies.html)
  - *Why it helps:* FIRAS data maps intensity against *wavenumber* ($\text{cm}^{-1}$), but standard physics equations often expect *frequency* ($\text{Hz}$) or *wavelength* ($\text{m}$). Astropy provides a built-in `spectral()` equivalency system that permits effortless conversion between these axes without manually tracking speed-of-light arithmetic errors.
- `astropy.io.fits` **or** `astropy.table`
  - *Documentation:* [docs.astropy.org/en/stable/table/](https://docs.astropy.org/en/stable/table/)
  - *Why it helps:* If the data downloaded from LAMBDA is formatted as a FITS table, `astropy.table.Table.read()` allows students to ingest the file instantly into a structured array, automatically reading table headers and preserving unit metadata.

### Core Python & SciPy Documentation

- **NumPy Arrays and Vectorization (`numpy`)**
  - *Documentation:* [numpy.org/doc/](https://numpy.org/doc/)
  - *Why it helps:* Students will need to evaluate Planck's Law across hundreds of data channels simultaneously. Utilizing NumPy's vectorized operations (`np.exp`, `np.power`) allows them to compute the entire theoretical model array instantly without relying on slow Python `for` loops.
- **SciPy Optimization Routine (`scipy.optimize.minimize` or `curve_fit`)**
  - *Documentation:* [docs.scipy.org/doc/scipy/reference/optimize.html](https://docs.scipy.org/doc/scipy/reference/optimize.html)
  - *Why it helps:* Step 5 of the workflow requires finding a temperature that minimizes $\chi^2$. Students can write a custom chi-squared objective function and pass it directly to `scipy.optimize.minimize`, or use `scipy.optimize.curve_fit` to handle both parameter optimization and automatically extract the parameter covariance matrix (which directly answers **Stretch Goal 1** regarding formal uncertainty estimation).
- **Matplotlib Subplots and Error Bars (`matplotlib.pyplot`)**
  - *Documentation:* [matplotlib.org/stable/api/pyplot_summary.html](https://matplotlib.org/stable/api/pyplot_summary.html)
  - *Why it helps:* To produce professional diagnostic plots, students should study the documentation for `plt.errorbar()` to accurately overlay the FIRAS uncertainties. To implement the residual plot directly beneath the spectrum plot cleanly, reviewing `plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]})` will give them precise control over the layout geometry.
