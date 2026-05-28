
Software
- Python 3.x with scientific stack (NumPy, SciPy, Matplotlib, Astropy)
- Jupyter Notebook for interactive development
- Python packages: dust_extinction, astroquery, pysynphot
- pysynphot (STScI) - Accessing standard stellar libraries and performing synthetic photometry. Developed by the Space Telescope Science Institute, this library provides access to standard stellar spectral libraries (like Pickles, Kurucz, and BaSeL) and allows you to convolve them with filter responses. It is ideal for generating clean, standard templates without needing to run complex population synthesis codes. Includes built-in extinction curves (Milky Way, LMC, SMC) which aligns perfectly with your project goals. Installation: pip install pysynphot (Note: It relies on older dependencies; you may need to use a specific conda environment or the newer synphot fork).

Data Sources
- Template spectra from SDSS or synthetic stellar population models
- SDSS SkyServer (via astroquery) - Downloading real observed spectra. Using the astroquery library, students can query the Sloan Digital Sky Survey (SDSS) database to download real galaxy and star spectra. Comparing a theoretical template (from python-fsps) with a real observed spectrum (from SDSS) highlights the necessity of dust correction and noise handling. Installation: pip install astroquery

Extinction Curves Resources
- Cardelli, Clayton & Mathis (1989) https://ui.adsabs.harvard.edu/abs/1989ApJ...345..245C/abstract -- Standard Milky Way curve, depends on R_V
- Fitzpatrick (1999) https://ui.adsabs.harvard.edu/abs/1999PASP..111...63F/abstract -- Describes dereddening process
- Fitzpatrick & Massa (1999) https://ui.adsabs.harvard.edu/abs/1990ApJS...72..163F/abstract -- a more detailed treatment of UV extinction
- Calzetti et al. (2000) https://ui.adsabs.harvard.edu/abs/2000ApJ...533..682C/abstract -- Starburst galaxy attenuation laws and dust properties
- Gordon et al. (2003) https://ui.adsabs.harvard.edu/abs/2003ApJ...594..279G/abstract -- Magellanic Cloud variations (SMC/LMC)
- dust_extinction Python package
- Draine, B. T. (2011). Physics of the Interstellar and Interplanetary Medium (text book)
- MPei, Y. C. (1992). https://ui.adsabs.harvard.edu/abs/1992ApJ...395..130P/abstract -- "Interstellar Extinction Law toward the SMC, LMC, and the Milky Way"

Methodology
- https://dust-extinction.readthedocs.io/en/latest/
- https://dust-extinction.readthedocs.io/en/latest/dust_extinction/extinguish.html
