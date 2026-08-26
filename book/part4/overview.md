# Chapter 5 · Vectors and Matrix Fundamentals

Data is rectangular. A dataset is a matrix; an observation is a vector; a model's parameters are a vector; training is matrix arithmetic performed at scale. This chapter builds linear algebra from geometric first principles — arrows, lengths, angles — and ends with the eigen-decomposition, the theorem under principal component analysis, spectral methods, and the stability analysis of every iterative algorithm.

**The arc of the chapter.**

- **Section 5.1 — Vectors.** Arrows and coordinate lists unified: addition, scaling, length, unit vectors, and the geometry of $\mathbb{R}^n$ when $n$ is too large to draw.
- **Section 5.2 — The Dot and Cross Products.** The dot product measures alignment — the source of angles, projections, and cosine similarity. The cross product (special to $\mathbb{R}^3$) measures spanned area and handedness.
- **Section 5.3 — Matrices and Matrix Operations.** Matrices as *transformations*, not spreadsheets: what multiplication really composes, why order matters, and what transpose, identity, and inverse mean geometrically.
- **Section 5.4 — Linear Systems and Gauss–Jordan Elimination.** Solving $\mathit A\vb x = \vb b$ three ways of seeing (rows, columns, transformation), one algorithm (elimination), and a complete account of when solutions exist and how many.
- **Section 5.5 — Determinants.** One number that measures how a matrix scales volume — and thereby decides invertibility, orientation, and (in Section 6.5) the change-of-variables factor in integrals.
- **Section 5.6 — Eigenvalues and Eigenvectors.** Directions a matrix does not turn. The chapter's summit: diagonalization, matrix powers, and the spectral view that makes PCA, Markov chains, and stability analysis one subject.

**How to study this chapter.** Small cases by hand, always: every concept here is learnable on $2\times 2$ and $3\times 3$ matrices, and NumPy exists to confirm the hand result and then scale it. Draw relentlessly in Sections 5.1–5.2 — the geometry is the meaning. From Section 5.3 on, keep asking of every fact: *what does this say about the transformation?* That habit converts symbol-pushing into understanding.

**Where it leads.** Chapter 6 fuses this chapter with calculus: the gradient is a vector, the Hessian is a matrix, its eigenvalues classify optima and set the speed limit of gradient descent, and the determinant prices coordinate changes inside integrals. Nearly every algorithm in a machine-learning course is an application of Sections 5.4–5.6.
