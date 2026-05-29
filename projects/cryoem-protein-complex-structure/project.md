---
title: "Determining the Atomic Structure of a Protein Complex by Cryo-EM"
pi: "dani-fera"
goals:
  - "Explain in plain terms what a protein complex is and what an atomic-resolution structure tells us"
  - "Explain the cryo-EM workflow from micrographs to a 3D density map at a working level"
  - "Process a single-particle cryo-EM dataset in cryoSPARC through to a refined 3D reconstruction"
  - "Build and refine an atomic model into the density map using Coot and Phenix"
  - "Validate the final model against standard quality metrics and report them honestly"
  - "Produce publication-quality figures of the structure in PyMOL"
  - "Write a short report describing the structure, the workflow, and what the model reveals"
---

# Research Project: Determining the Atomic Structure of a Protein Complex by Cryo-EM

## Project overview

Proteins are the molecular machines of the cell, and most of them do their
jobs by assembling into **complexes** — several protein chains that fit
together into a larger structure. To understand how a complex works, it
helps enormously to know its **three-dimensional structure at atomic
resolution**: where every chain sits, how the pieces interface, and where
the chemically important atoms are.

In this project, you will determine such a structure using
**cryo-electron microscopy (cryo-EM)**. In single-particle cryo-EM, a
sample of purified complex is flash-frozen in a thin layer of ice and
imaged in an electron microscope. Each image (a *micrograph*) contains many
copies of the complex frozen in random orientations. Software combines
hundreds of thousands of these noisy 2D views into a single 3D map of the
molecule's electron density. You then build an atomic model that fits that
map.

This is a hands-on computational structural-biology project. You are **not**
expected to be an expert in cryo-EM at the start. By the end, you should be
able to explain the workflow, run it yourself on a real dataset, and produce
a validated atomic model and figures that communicate the structure clearly.

---

## The scientific question

The driving question is concrete: **what does this protein complex look
like at atomic resolution, and what does that structure tell us about how it
works?** A good final model lets you ask follow-up questions — how the
subunits interface, where a binding site or active site sits, and how the
overall architecture supports the complex's function.

Getting there means turning a large, noisy set of microscope images into a
single high-quality 3D map, and then building an atomic model that is both a
good fit to the map and chemically sensible.

---

## What you will actually do

You will run the standard single-particle cryo-EM pipeline end to end, using
the field's standard software:

1. **Process the data in cryoSPARC.** Starting from a cryo-EM dataset, work
   through the core steps: motion correction and CTF estimation, particle
   picking, 2D classification to clean up the particle set, *ab initio*
   reconstruction, 3D classification, and 3D refinement to produce a
   high-resolution density map. Track the resolution as it improves and
   understand what each step does and why.

2. **Build and refine an atomic model in Coot and Phenix.** Fit protein
   chains into the density map. Use **Coot** for interactive model building
   and manual adjustments, and **Phenix** for automated real-space
   refinement against the map. Iterate between the two: refine, inspect,
   fix, refine again.

3. **Validate the model.** Check the model against standard quality metrics
   — map-to-model fit/correlation, Ramachandran statistics, clashscore,
   rotamer outliers, and the reported resolution. Report these honestly,
   including any weaknesses.

4. **Make figures in PyMOL.** Render clear, publication-quality images of
   the final structure — overall architecture, subunit interfaces, and any
   functionally important region.

5. **Write it up.** Summarize the complex, the workflow you ran, the final
   resolution and validation numbers, and what the structure reveals.

---

## Required products

At the end of the project, you should produce:

- **A refined 3D density map** from cryoSPARC, with the reported resolution
  and the key processing statistics.

- **A validated atomic model** of the complex (a coordinate file, e.g. a
  PDB/mmCIF file) built in Coot and refined in Phenix.

- **A validation summary** reporting the standard metrics (map-to-model
  fit, Ramachandran, clashscore, rotamer outliers, resolution) and a brief
  honest assessment of model quality.

- **Publication-quality figures** made in PyMOL showing the overall
  structure and the features you want to highlight.

- **A short written report** describing the complex, the cryo-EM workflow,
  the final model and its validation, and what the structure tells you about
  how the complex works.

---

## Suggested workflow

### Step 1: Build the conceptual picture first

Before touching the software, make sure you can explain:

- what single-particle cryo-EM is and why freezing the sample matters
- what a micrograph contains and why the views are in random orientations
- what a 3D density map is, and the difference between a *map* and a *model*
- what "resolution" means for a cryo-EM map and why higher is harder

### Step 2: Process the dataset in cryoSPARC

Work through the pipeline one stage at a time. After each major step
(2D classification, *ab initio*, refinement), pause and check that the
result makes sense before moving on. Keep notes on the particle counts and
resolution at each stage.

### Step 3: Get an initial model into the map

Once you have a good map, place starting chains and use Coot to fit them
into the density. Expect this to be iterative — build a region, inspect the
fit, adjust, and move on.

### Step 4: Refine and validate in a loop

Alternate between Phenix real-space refinement and manual fixes in Coot.
After each round, look at the validation metrics. Stop when the model is a
good fit to the map and the metrics are clean, not when you run out of
patience.

### Step 5: Make figures and write the report

Render the final figures in PyMOL, then write the report. A good report
explains not just *what* the structure is but *what it means* — what the
architecture and interfaces suggest about the complex's function.

---

## Getting started with the software

Before you begin, confirm access with the PI and review these resources:

### cryoSPARC setup & first steps
- **Installation & access:** Confirm which compute environment you'll use (local cluster, cloud, etc.) and which version of cryoSPARC is installed.
- **Tutorial:** Follow the [cryoSPARC Quick Start guide](https://guide.cryosparc.com/start) to get comfortable with the interface.
- **Example dataset:** Ideally, work through a small public dataset first (available in [cryoSPARC tutorials](https://guide.cryosparc.com/tutorials)) before processing your own data.

### What to expect at each pipeline stage

**Motion Correction & CTF Estimation**
- *Goal:* Correct for stage drift in the microscope and estimate the contrast transfer function.
- *How:* In cryoSPARC, see the "Motion Correction" and "CTF Estimation" sections of the [guide](https://guide.cryosparc.com/).
- *Success looks like:* CTF plots showing clear oscillations; motion correction improves micrograph quality visually.

**Particle Picking**
- *Goal:* Automatically (or manually) identify particle locations in micrographs.
- *How:* [cryoSPARC particle picking guide](https://guide.cryosparc.com/processing/tutorials/picking).
- *Success looks like:* Pick statistics showing reasonable particle density; spot-check by overlaying picks on a few micrographs.

**2D Classification**
- *Goal:* Sort particles into classes; clean ones keep good signal, bad ones get discarded.
- *How:* [cryoSPARC 2D classification guide](https://guide.cryosparc.com/processing/tutorials/2d-classification).
- *Success looks like:* Classes show clear, recognizable views of your complex; class averages improve with more particles.

**Ab Initio Reconstruction & 3D Classification**
- *Goal:* Build an initial 3D map; refine it by sorting particles into 3D classes.
- *How:* [Ab initio guide](https://guide.cryosparc.com/) and [3D classification guide](https://guide.cryosparc.com/).
- *Success looks like:* Map shows secondary structure (helices, sheets); resolution improves with each refinement round.

**3D Refinement**
- *Goal:* Refine particle alignments to maximize map resolution.
- *How:* [3D refinement guide](https://guide.cryosparc.com/processing/tutorials/3d-refinement).
- *Success looks like:* Resolution and FSC improving; map quality visually sharper than ab initio.

### Coot & Phenix: model building and refinement
- **Coot tutorial:** Start with the [Coot documentation](https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/); the "Getting Started" section has worked examples of fitting a chain into a density map.
- **Phenix tutorial:** See [Phenix real-space refinement guide](https://phenix-online.org/documentation/reference/real_space_refine.html).
- **Workflow:** Fit in Coot → refine in Phenix → inspect → adjust in Coot → refine again. Iterate 3–5 times.

### PyMOL: visualization and figures
- **Getting started:** [PyMOL wiki](https://pymolwiki.org/); focus on loading structures, basic coloring, and rendering.
- **Making publication figures:** Look for "publication" or "ray-tracing" sections in the wiki; save as high-resolution PNG/PDF.

---
---

## Stretch goals

- **Local resolution analysis.** Estimate and visualize local resolution
  across the map, and discuss which regions are well resolved and which are
  flexible.
- **Interface analysis.** Characterize the subunit–subunit interfaces — the
  residues involved and the kinds of contacts.
- **Compare to a predicted model.** Compare your experimental structure to a
  computational prediction (e.g. an AlphaFold model) and discuss where they
  agree and differ.

---

## What a successful project should demonstrate

A successful project does not require solving a brand-new structure to the
highest possible resolution. It should be a correct, validated model built
through a workflow you understand and can explain. By the end, you should be
able to say:

- I can explain the single-particle cryo-EM workflow from images to a 3D map.
- I processed a real dataset in cryoSPARC to a refined reconstruction.
- I built and refined an atomic model using Coot and Phenix.
- I validated the model against standard metrics and can interpret them.
- I produced clear figures of the structure in PyMOL.
- I can explain what the structure reveals about how the complex works.
