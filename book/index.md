# Calculus and Matrix Methods for Data Science

**An Applied Introduction with Python**

This book is written for anyone who needs working fluency in the mathematics beneath quantitative and computational work: undergraduate and graduate students, professionals returning to technical roles, independent learners, and readers preparing for data science, machine learning, statistics, or scientific computing. You may once have taken calculus and forgotten most of it, or you may never have seen linear algebra at all. Either way, the subjects ahead — machine learning, statistical modeling, optimization, simulation — assume fluency with derivatives, integrals, series, vectors, matrices, and partial derivatives. This book rebuilds that fluency from the ground up, carefully and without condescension, assuming only high-school algebra as a starting point (and Appendix A refreshes even that).

Every major concept in the book follows the same cycle:

$$
\boxed{\text{Understand} \;\rightarrow\; \text{Do by Hand} \;\rightarrow\; \text{Implement in Python} \;\rightarrow\; \text{Visualize} \;\rightarrow\; \text{Interpret} \;\rightarrow\; \text{Practice}}
$$

You will first understand where an idea comes from and carry out the essential calculation with pencil and paper. Only then does Python enter, to verify your work, to push past what hand computation can reach, and to draw pictures that make the mathematics visible. Python is a lens here, not a crutch: a library call that produces a number you could not have estimated yourself teaches you nothing.

## How the book is organized

**Chapter 1 — Mathematical Foundations** reviews functions, algebra, exponentials, logarithms, and trigonometry: the raw material of calculus.

**Chapter 2 — Differential Calculus** develops the derivative: limits (just enough of them), differentiation rules, the chain rule, derivatives of the transcendental functions, linear approximation, Newton's method, and optimization in one variable.

**Chapter 3 — Integral Calculus** develops the integral: antiderivatives, the definite integral, the Fundamental Theorem of Calculus, substitution, areas, volumes, integration by parts, trigonometric substitution, and numerical integration.

**Chapter 4 — Series and Approximation** covers summation notation, sequences and series, power series, Taylor polynomials and Taylor series, truncation error, and (optionally) Fourier series.

**Chapter 5 — Vectors and Matrix Fundamentals** covers vectors, the dot and cross products, matrices and their operations, systems of linear equations and Gauss–Jordan elimination, determinants, and eigenvalues and eigenvectors.

**Chapter 6 — Multivariable Calculus** extends calculus to several variables: vector-valued functions, surfaces, partial derivatives, the multivariable chain rule, directional derivatives and gradients, double integrals, and polar coordinates.

The **Appendices** collect reference material: an algebra refresher, formula sheets, Python quick references, selected answers, and a glossary.

## How to use this book

Read with paper beside you. Work every *Do It by Hand* segment before looking at the Python that follows. Attempt the *Quick Check* questions as you meet them; they are diagnostic, and stumbling on one is a signal to reread rather than a failure. Exercises come with hints and, for selected problems, full solutions behind collapsible panels — use them the way you would use office hours: after a genuine attempt.

The next chapter, {doc}`getting-started`, sets up your Python environment and explains the book's visual conventions. The {doc}`notation` guide defines every symbol the book uses; return to it whenever notation is unclear.

```{admonition} Sources and further reading
:class: seealso
This book is self-contained, but it deliberately parallels two freely available references: OpenStax *Calculus* Volumes 1–3 {cite}`openstax_calc1,openstax_calc2,openstax_calc3` for calculus, and the linear algebra chapter of *Deep Learning* {cite}`goodfellow_linalg` for the matrix material. Pointers to these books appear at the end of each section for readers who want a second presentation of the same ideas.
```
