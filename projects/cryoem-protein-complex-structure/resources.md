# Recommended resources

These readings, tools, and tutorials support the *Determining the Atomic
Structure of a Protein Complex by Cryo-EM* project. They cover the
conceptual background you need plus the documentation for each piece of
software in the workflow.

## Background on single-particle cryo-EM

- **Overview review:** a modern introductory review of single-particle
  cryo-EM (for example, articles in *Nature Methods* "Primer" or review
  series, or the cryo-EM chapters of a structural biology textbook). Focus
  on the path from frozen sample → micrographs → 2D classes → 3D map →
  atomic model.
- **[Wikipedia: Cryogenic electron microscopy](https://en.wikipedia.org/wiki/Cryogenic_electron_microscopy)**
  — a quick orientation to the vocabulary before you read the primary
  literature.

## Software documentation and tutorials

- **cryoSPARC** — data processing (motion correction, CTF, particle
  picking, 2D/3D classification, refinement).
  [cryoSPARC guide & tutorials](https://guide.cryosparc.com/)
- **Coot** — interactive model building and real-space fitting.
  [Coot documentation](https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/)
- **Phenix** — automated refinement and validation
  (`phenix.real_space_refine`, validation tools).
  [Phenix documentation](https://phenix-online.org/documentation/)
- **PyMOL** — molecular visualization and figure making.
  [PyMOL documentation & wiki](https://pymolwiki.org/)

> Note on naming: the refinement/validation suite is **Phenix** (sometimes
> mis-typed "Phoenix"). The other tools are **cryoSPARC**, **Coot**, and
> **PyMOL**.

## Data and reference structures

- **[EMDB — Electron Microscopy Data Bank](https://www.ebi.ac.uk/emdb/)** —
  deposited cryo-EM maps; useful for finding example maps and comparing
  reported resolutions.
- **[RCSB Protein Data Bank (PDB)](https://www.rcsb.org/)** — deposited
  atomic models; a source of starting models and a reference for what a
  well-built, validated structure looks like.
- **[EMPIAR](https://www.ebi.ac.uk/empiar/)** — raw cryo-EM image datasets,
  if you need a public dataset to process.

## Validation references

- Familiarize yourself with the standard model-quality metrics: map-to-model
  correlation/FSC, Ramachandran statistics, clashscore, and rotamer
  outliers. The Phenix documentation and the PDB validation report
  guidelines both explain what good values look like.

## A note on access

cryoSPARC, Coot, Phenix, and PyMOL each require installation and (for some)
licensing. Confirm with the PI which compute environment and dataset you
will use before starting, and which versions are installed.
