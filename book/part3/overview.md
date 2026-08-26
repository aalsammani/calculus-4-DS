# Chapter 4 · Series and Approximation

Computers cannot evaluate $e^x$, $\sin x$, or $\ln x$ exactly — yet they do it billions of times per second. The resolution of that paradox is this chapter: complicated functions can be *rebuilt* from infinitely many simple pieces, and truncating the rebuild after a few terms gives approximations of astonishing quality. Series are how mathematics trades the infinite for the computable.

**The arc of the chapter.**

- **Section 4.1 — Summation, Sequences, and Series.** The grammar: sigma notation, convergence of sequences, the geometric series (the one series whose sum is *known exactly*, and the engine under everything from present value to PageRank), and the basic convergence tests.
- **Section 4.2 — Power Series and Taylor Series.** The centerpiece: representing functions as "infinite polynomials," with coefficients read off from derivatives at a single point. Radius of convergence marks where the representation is trustworthy; the truncation error is measured, not guessed.
- **Section 4.3 — Fourier Series.** The other great decomposition: periodic functions rebuilt from sines and cosines, with coefficients read off by *integration* rather than differentiation. An enrichment section that plants the orthogonality idea Chapter 5 will grow into the dot product.

**How to study this chapter.** Taylor series reward hand computation: derive the big five expansions ($e^x$, $\sin$, $\cos$, $\frac{1}{1-x}$, $\ln(1+x)$) yourself, once each, and they become permanent property. Then use Python to *watch* partial sums converge — and to watch them fail outside the radius of convergence, which teaches more than any theorem statement. The contrast between the two decompositions — Taylor's derivatives-at-a-point versus Fourier's integrals-over-a-period — is a recurring exam and interview question; the section exercises rehearse it deliberately.

**Where it leads.** The multivariable Taylor expansion (quadratic form, Hessian) is the lens through which Section 6.3 classifies critical points and explains optimizer behavior; Fourier's orthogonality becomes literal perpendicularity in Chapter 5; and every "approximation error" bound in numerical work descends from Taylor's theorem.
