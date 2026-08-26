# Appendix E · Glossary

Concise definitions of the book's technical vocabulary, with the chapter where each term is introduced.

**Antiderivative** (§3.1) — a function $F$ with $F' = f$; unique up to an added constant.

**Arc length** (§3.3, §6.1) — the length of a curve; $\int\|\vb r'(t)\|\,dt$ for a parametrized curve.

**Augmented matrix** (§5.4) — coefficient matrix with the right-hand side appended, $[\mathit A\mid\vb b]$, for bookkeeping elimination.

**Basis** (§5.4) — an independent set that spans a space; every basis of a space has the same number of vectors, the space's dimension.

**Chain rule** (§2.3, §6.2) — derivative of a composition: outer derivative at the inner value times inner derivative; in several variables, one such product per dependency path, summed.

**Characteristic polynomial** (§5.6) — $\det(\mathit A - \lambda\mathit I)$; its roots are the eigenvalues.

**Concavity** (§2.2) — the direction a graph bends; the sign of $f''$.

**Condition number** (§5.4, §6.3) — sensitivity measure of a matrix/problem; for symmetric positive definite matrices, $\lambda_{\max}/\lambda_{\min}$; governs gradient descent's difficulty.

**Continuous** (§2.1, §6.2) — limit equals value; in several variables, along every approach path.

**Contour map / level curve** (§6.2) — the sets $f(x,y) = c$ drawn in the domain; spacing encodes steepness.

**Convergence** (§4.1) — a sequence or series approaching a finite limit; for series, convergence of the partial-sum sequence.

**Critical point** (§2.2, §2.5, §6.3) — where the derivative (gradient) vanishes; candidate for extremum, classified by second-order information.

**Cross product** (§5.2) — $\vb u\times\vb v$ in $\mathbb{R}^3$: vector orthogonal to both factors, magnitude the spanned parallelogram's area.

**Determinant** (§5.5) — signed volume-scaling factor of a square matrix's transformation; zero exactly for singular matrices.

**Diagonalization** (§5.6) — factoring $\mathit A = \mathit P\mathit D\mathit P^{-1}$ with eigenvectors in $\mathit P$, eigenvalues in diagonal $\mathit D$.

**Directional derivative** (§6.3) — rate of change of $f$ along a unit direction: $D_{\vb u}f = \nabla f\cdot\vb u$.

**Dot product** (§5.2) — $\sum u_iv_i = \|\vb u\|\|\vb v\|\cos\theta$; encodes length and angle; zero means orthogonal.

**Double integral** (§6.4) — Riemann limit of box volumes over a plane region; computed as iterated single integrals (Fubini).

**Eigenvalue / eigenvector** (§5.6) — a scaling factor and invariant direction of a matrix: $\mathit A\vb v = \lambda\vb v$, $\vb v \ne \vb 0$.

**Fourier series** (§4.3) — expansion of a periodic function in sines and cosines, coefficients by orthogonality integrals.

**Fundamental Theorem of Calculus** (§3.1) — differentiation and integration are inverse: $\int_a^b f = F(b) - F(a)$, and the accumulation function's derivative is the integrand.

**Gaussian integral** (§6.5) — $\int_{-\infty}^\infty e^{-x^2}dx = \sqrt\pi$; evaluated by squaring and converting to polar coordinates.

**Gradient** (§6.3) — $\nabla f$, the vector of partial derivatives; points in the direction of steepest ascent, perpendicular to level sets.

**Gradient descent** (§6.3) — iterative minimization $\vb x \leftarrow \vb x - \eta\nabla f(\vb x)$; the training algorithm of machine learning.

**Hessian** (§6.2–§6.3) — the symmetric matrix of second partials; its eigenvalues classify critical points and set optimization difficulty.

**Improper integral** (§3.1) — integral with an infinite limit or unbounded integrand, defined as a limit of proper ones.

**Integration by parts** (§3.4) — $\int u\,dv = uv - \int v\,du$; the product rule integrated.

**Jacobian** (§6.2, §6.5) — matrix of partial derivatives of a transformation; its determinant is the local area/volume scaling used in change of variables.

**Learning rate** (§6.3) — the step-size multiplier $\eta$ in gradient descent.

**Limit** (§2.1) — the value a function approaches as its input approaches a point; the foundation beneath derivative and integral.

**Linear combination** (§5.1) — $c_1\vb v_1 + \cdots + c_k\vb v_k$; the master construction of linear algebra.

**Linear independence** (§5.4) — a set of vectors admits only the trivial combination equal to zero; operationally, the columns are independent exactly when elimination gives each a pivot.

**Linearization / tangent plane** (§2.4, §6.2) — best linear approximation at a point: $f(a) + f'(a)(x-a)$, or with one correction term per variable.

**Magnitude / norm** (§5.1) — vector length $\sqrt{\sum v_i^2}$.

**Matrix** (§5.3) — rectangular number array; equivalently a linear transformation whose columns are the images of the basis vectors.

**Monte Carlo integration** (§6.4) — estimating integrals by averaging over random samples; error $\sim 1/\sqrt N$ in any dimension.

**Newton's method** (§2.4, §5.4, §6.3) — root-finding (and, applied to $f'$, optimization) by repeatedly solving the linearized problem.

**Orthogonal** (§5.2) — perpendicular; dot product zero.

**Partial derivative** (§6.2) — derivative in one variable with the others held fixed.

**Pivot** (§5.4) — leading nonzero entry of a row in elimination; the pivot count is the rank.

**Polar coordinates** (§6.5) — $(r,\theta)$: distance and direction; area element $r\,dr\,d\theta$.

**Power series / Taylor series** (§4.2) — infinite polynomial $\sum c_k(x-a)^k$; Taylor's coefficients come from derivatives at the center.

**Projection** (§5.2) — component of one vector along another: $\frac{\vb a\cdot\vb b}{\vb a\cdot\vb a}\vb a$; the seed of least squares.

**Radius of convergence** (§4.2) — half-width of the interval where a power series converges.

**Rank** (§5.4) — number of pivots; the independent information in a matrix's rows/columns.

**Riemann sum** (§3.1) — sample-value × piece-size, summed; its refinement limit defines the integral.

**RREF** (§5.4) — reduced row echelon form; the terminus of Gauss–Jordan elimination where solutions are read off.

**Saddle point** (§6.2–§6.3) — critical point rising in one direction and falling in another; mixed-sign Hessian eigenvalues.

**Singular matrix** (§5.4–§5.5) — square matrix with no inverse; determinant zero; collapses some direction.

**Span** (§5.4) — the set of all linear combinations of a collection of vectors; the pivot columns of a matrix form a basis for the span of its columns.

**Spectral theorem** (§5.6) — symmetric matrices have real eigenvalues and orthonormal eigenvectors.

**Substitution** (§3.2) — the chain rule integrated; change of variable with $dx$ converted.

**Transpose** (§5.3) — rows-for-columns flip $\mathit A^{\mathsf T}$; reverses products.

**Unit vector** (§5.1) — vector of magnitude 1; pure direction, produced by normalization $\vb v/\|\vb v\|$.

**Vector** (§5.1) — ordered list of numbers; equivalently an arrow with direction and length.

**Vector-valued function** (§6.1) — a curve: scalar input, vector output; differentiates componentwise into velocity and acceleration.
