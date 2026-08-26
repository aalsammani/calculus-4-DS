# Chapter 6 · Multivariable Calculus

Models have many parameters; data has many features; loss surfaces live in thousands of dimensions. This final chapter rebuilds calculus for that world — and in doing so, fuses the two halves of the book. Derivatives meet vectors and become the gradient; second derivatives meet matrices and become the Hessian; integrals meet regions and coordinate changes, and the book ends by deriving the constant in the normal distribution that all of statistics quietly relies on.

**The arc of the chapter.**

- **Section 6.1 — Vector-Valued Functions.** Curves through space: one input, many outputs. Velocity, speed, and arc length — the calculus of trajectories, including the trajectory an optimizer traces through parameter space.
- **Section 6.2 — Functions of Several Variables.** Many inputs, one output: surfaces, contour maps, partial derivatives, and the multivariable chain rule that backpropagation implements at industrial scale.
- **Section 6.3 — Gradients and Directional Derivatives.** The gradient assembled and interpreted: steepest ascent, perpendicularity to level sets, gradient descent with an honest account of learning rates, and the Hessian's eigenvalues classifying critical points — Chapters 2 and 5 shaking hands.
- **Section 6.4 — Double Integrals.** Accumulation over regions of the plane: iterated integrals, Fubini's theorem, order of integration, and the region-sketching skill on which everything turns.
- **Section 6.5 — Polar Coordinates.** The right coordinates for circular problems, the Jacobian determinant as the honest price of changing variables — and the finale: $\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$, the Gaussian integral, evaluated by the most elegant trick in the book.

**How to study this chapter.** Contour maps are the multivariable graph — practice reading them until steepness, valleys, and saddles are visible at a glance, because that is precisely the skill of reading a loss landscape. In Sections 6.4–6.5, *always sketch the region first*; every hard double integral is a region-description problem wearing a disguise. And let the finale land: the $\sqrt{2\pi}$ in the normal density is not a convention but a theorem, and by the last page of Section 6.5 it is *yours*.

**Where it leads.** Directly into the graduate curriculum: gradient descent and its variants (optimization courses), the multivariable Gaussian (statistics and ML), PCA on covariance matrices (Sections 5.6 + 6.4 combined), and the Jacobians of normalizing flows and change-of-variables formulas throughout probabilistic ML.
