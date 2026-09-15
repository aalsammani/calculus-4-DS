# Calculus and Matrix Methods for Data Science
### An Applied Introduction with Python — Abdallah Alsammani

A self-contained textbook covering the mathematics beneath quantitative and
computational work: functions and precalculus, differential and integral
calculus, series and Taylor approximation, Fourier series, linear algebra and
matrix methods, and multivariable calculus — each developed by hand first and
then implemented, verified, and visualized in Python (NumPy, SymPy, Matplotlib,
SciPy).

Every concept follows one cycle:

**Understand → Do by Hand → Implement in Python → Visualize → Interpret → Practice**

## Structure

| Chapter | Sections |
|---|---|
| 1. Mathematical Foundations | functions and graphs; exponentials, logarithms, trigonometry |
| 2. Differential Calculus | limits and the derivative; rules; chain rule and transcendentals; linearization and Newton's method; optimization |
| 3. Integral Calculus | antiderivatives and the FTC; substitution; areas and volumes; parts and trig substitution; numerical integration |
| 4. Series and Approximation | summation, sequences, series; power and Taylor series; Fourier series |
| 5. Vectors and Matrix Fundamentals | vectors; dot and cross products; matrices; linear systems and elimination; determinants; eigenvalues and eigenvectors |
| 6. Multivariable Calculus | vector-valued functions; several variables; gradients; double integrals; polar coordinates |

Appendices: algebra refresher, formula sheet, Python quick reference, selected
answers, glossary, bibliography.

## Building the book locally

```bash
pip install -r requirements.txt
jupyter-book build book/
# open book/_build/html/index.html
```

A clean build produces zero warnings. All figures are pre-rendered
(regenerate with `python make_all_figures.py`); all numerical claims in the
text were verified computationally before publication.

## Deployment

Pushes to `main` trigger `.github/workflows/deploy.yml`, which builds the book
and publishes `book/_build/html` to GitHub Pages. To host elsewhere, serve the
same directory — the site is fully static.

## Repository layout

```
book/            the book source (Markdown + MyST), _config.yml, _toc.yml
book/partN/      chapter directories with their figures/
book/appendices/ appendices and references.bib
requirements.txt build dependencies
make_all_figures.py  regenerates every figure deterministically
```


## Copyright and Citations

**Copyright © 2026 Abdallah Alsammani. All rights reserved.**

Third-party materials are used and cited under their respective licenses. See the [Bibliography](book/appendices/bibliography.md) and [`references.bib`](book/references.bib) for sources and attribution.
