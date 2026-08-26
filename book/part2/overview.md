# Chapter 3 · Integral Calculus

If the derivative asks *how fast*, the integral asks *how much*: total distance from a speed record, total probability from a density, total revenue from a rate. This chapter builds the integral, connects it to the derivative through one of the great theorems of mathematics, and develops the toolbox — exact and numerical — for actually computing it.

**The arc of the chapter.**

- **Section 3.1 — Antiderivatives and the Fundamental Theorem.** Integration is defined by accumulation and *computed* by antidifferentiation; the Fundamental Theorem of Calculus is the bridge, and the reason the same symbol serves both.
- **Section 3.2 — Substitution.** The chain rule read backwards: the workhorse technique that converts a vast family of integrals into table lookups.
- **Section 3.3 — Areas and Volumes.** Slicing: area between curves, volumes by cross-sections, disks, and shells. The section where integrals first *build geometry*.
- **Section 3.4 — Integration by Parts and Trigonometric Substitution.** The product rule read backwards, and the Pythagorean identities deployed to dissolve square roots — the two techniques that finish the exact-integration toolkit this book needs.
- **Section 3.5 — Numerical Integration.** What to do when no formula exists (which, in practice, is most of the time): trapezoid and Simpson's rules, with an honest error theory that predicts *exactly* how fast each converges.

**How to study this chapter.** Integration is pattern recognition, and the patterns only install through volume: do more exercises than feel necessary. When a technique choice is unclear, that confusion is the lesson — Section 3.4 closes with a decision guide, and the exercises deliberately mix techniques so the choosing itself gets practiced. Section 3.5's error laws should be *tested* in Python: halve the step, watch the error fall fourfold (trapezoid) or sixteenfold (Simpson), and the theory becomes personal experience.

**Where it leads.** Series (Chapter 4) will integrate term-by-term; probability lives on integrals of densities, with the normal distribution's $\sqrt{2\pi}$ finally *derived* in Section 6.5; and the double integrals of Chapter 6 are this chapter's slicing idea promoted to the plane.
