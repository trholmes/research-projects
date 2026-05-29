---
title: "Surveying the Ring Chemistry of ansa-Sandwich Complexes"
pi: "kjdonald"
goals:
  - "Explain what a sandwich complex is and what the ansa bridge adds to one"
  - "Assemble a survey of known ansa-type sandwich complexes from the literature into a structured dataset"
  - "Classify the organic ring systems that serve as the sandwich decks in each complex"
  - "Produce a bar chart of the frequency of each organic ring type across the surveyed complexes"
  - "Write clean, readable Python that another scientist could understand and reuse"
  - "Summarize, in writing, what the distribution of ring types reveals about ansa-sandwich chemistry"
---

# Research Project: Surveying the Ring Chemistry of ansa-Sandwich Complexes

## Project overview

A **sandwich complex** is a molecule in which a metal atom sits between two
flat, ring-shaped organic molecules — like a slice of metal between two
slices of bread. The classic example is *ferrocene*, in which an iron atom
is sandwiched between two five-membered carbon rings (cyclopentadienyl
rings). Sandwich complexes are a cornerstone of organometallic chemistry.

An **ansa-sandwich complex** is a sandwich complex with one extra feature: a
small chemical "strap" — the *ansa bridge* — that ties the two rings
together. The word *ansa* comes from the Latin for "handle." That bridge
locks the two decks at a fixed tilt and distance, which changes how the
molecule behaves and what it can do as a catalyst or material.

In this project, you will build a **survey of known ansa-type sandwich
complexes** and ask a simple but revealing question: **which kinds of
organic rings actually show up as the decks of these sandwiches?** Are they
almost always five-membered cyclopentadienyl rings, or do six-membered
(arene), seven-membered, or heteroatom-containing rings appear too? Your
main deliverable is a **bar chart of the organic ring types** found across
the complexes you survey.

This project is designed for a student who is comfortable with introductory
chemistry and curious about organometallic compounds. You are **not**
expected to be an expert in organometallic chemistry at the start. By the
end, you should be able to explain what these complexes are, recognize the
ring systems involved, and have practiced turning a chemistry literature
survey into a clean dataset and a clear figure.

---

## The scientific question

ansa-Sandwich complexes are usually drawn with two cyclopentadienyl rings,
but the family is broader than that. The decks can be:

- **Carbocyclic** rings (rings made only of carbon), such as
  cyclopentadienyl (5-membered) or arene/benzene-type (6-membered) rings.
- **Heterocyclic** rings (rings containing an atom other than carbon, such
  as boron, nitrogen, or phosphorus), such as phospholyl or boratabenzene
  decks.
- Rings of **different sizes**, including four-, five-, six-, seven-, and
  eight-membered rings.

The question you will answer with data is: **across the known ansa-sandwich
complexes, how often does each type of organic ring appear?** A bar chart
makes the answer immediately visible — tall bars for common ring types,
short bars for rare ones.

---

## What you will actually do

1. **Learn the vocabulary.** Make sure you can explain, in your own words,
   what a sandwich complex is, what the ansa bridge does, and what
   distinguishes the different ring systems (ring size, carbocyclic vs.
   heterocyclic).

2. **Survey the literature.** Using the recommended resources (see
   `resources.md`) plus review articles and databases, compile a list of
   known ansa-sandwich complexes. For each one, record the two rings that
   serve as the decks.

3. **Build a structured dataset.** Turn your survey into a tidy table (for
   example a CSV) with one row per complex. Useful columns include: the
   complex name or formula, the metal center, the identity of each of the
   two rings, the ring size, and whether each ring is carbocyclic or
   heterocyclic. Decide on a consistent naming scheme for ring types and
   document it.

4. **Classify the ring types.** Group the rings into a set of categories
   (for example: cyclopentadienyl, arene, cycloheptatrienyl, phospholyl,
   boratabenzene, etc.). Be explicit about how you define each category and
   how you handle edge cases.

5. **Make the bar chart.** Produce a bar chart showing the frequency of each
   organic ring type across all the complexes in your survey. Each ring
   counts toward its type (so a complex with two cyclopentadienyl rings
   contributes two counts to that bar — state clearly whether you count per
   ring or per complex).

6. **Write up what you found.** In a short report, describe your survey,
   how big your sample is, which ring types dominate, which are rare, and
   what that pattern suggests about the chemistry.

---

## Required products

At the end of the project, you should produce:

- **A bar chart of organic ring types**
  The central deliverable. It should clearly show how frequently each type
  of organic ring appears across the surveyed ansa-sandwich complexes, with
  labeled axes, readable category names, and a title.

- **A structured dataset**
  A tidy table (e.g. a CSV) listing the complexes you surveyed and the ring
  systems in each, with the columns you used to make the chart. This is the
  evidence behind your figure and should be reusable by someone else.

- **A clean Python notebook or script**
  Code that reads your dataset, performs the classification and counting,
  and generates the bar chart. The code should be readable, well organized,
  and clearly commented.

- **A short written summary**
  A few paragraphs explaining what an ansa-sandwich complex is, how you
  built the survey, what the bar chart shows, and what the distribution of
  ring types tells you about this class of molecules. Note any limitations
  (for example, biases in which complexes are well documented).

---

## Suggested workflow

### Step 1: Build your mental model

Before collecting any data, make sure you can sketch and explain:

- a generic sandwich complex (e.g. ferrocene)
- what changes when you add an ansa bridge
- the difference between a five-membered cyclopentadienyl ring and a
  six-membered arene ring
- what makes a ring "heterocyclic"

### Step 2: Define your scope and categories up front

Decide what counts as an "ansa-sandwich complex" for your survey, and write
down your ring-type categories before you start collecting. It is fine to
revise these as you learn more — just keep the definitions documented so the
final dataset is internally consistent.

### Step 3: Collect the data

Work through review articles and databases to find complexes. For each,
record the two decks and their properties in your table. Aim for a sample
large enough to make the bar chart meaningful, and keep track of where each
entry came from.

### Step 4: Classify and count

Map each ring onto one of your categories, then count how many times each
category appears. Double-check ambiguous cases and note how you resolved
them.

### Step 5: Plot and iterate

Make a first version of the bar chart, then refine it: sort the bars in a
sensible order, fix labels, and make sure the message is readable at a
glance.

### Step 6: Write the summary

Explain what the chart shows and what it means. Good summaries go beyond
"cyclopentadienyl is most common" to discuss *why* that might be and what
the rarer ring types represent.

---

## Stretch goals

- **Split carbocyclic vs. heterocyclic.** Add a second chart (or color the
  bars) to show how much of the family is carbocyclic versus heterocyclic.
- **Break down by metal.** Group the survey by the metal center and see
  whether different metals favor different ring types.
- **Ring size distribution.** Make a companion chart of ring *sizes*
  (4-, 5-, 6-, 7-, 8-membered) in addition to ring *types*.

---

## What a successful project should demonstrate

A successful project does not need to be exhaustive. It should be clear,
internally consistent, and well explained. By the end, you should be able
to say:

- I can explain what an ansa-sandwich complex is and what the bridge does.
- I built a structured survey of these complexes from the literature.
- I defined a clear, documented set of organic ring categories.
- I produced a bar chart that makes the distribution of ring types obvious.
- I can use Python to turn a dataset into a clear scientific figure.
- I can explain what the distribution of ring types reveals about this class
  of molecules.
