# Chapter 2 · Differential Calculus

Differential calculus answers one question with total precision: *how fast is a quantity changing, right now?* The answer — the derivative — is the single most-used mathematical object in data science. Training a neural network is an exercise in derivatives; so is a sensitivity analysis, an elasticity estimate, and every optimizer that has ever minimized a loss function.

**The arc of the chapter.** The four sections form one continuous story:

- **Section 2.1 — Limits and the Derivative.** The limit makes "instantaneous" meaningful, continuity makes graphs trustworthy, and the derivative is *defined* as the limiting difference quotient. Everything else in the chapter is technique for computing it faster.
- **Section 2.2 — Differentiation Rules.** The power, product, and quotient rules convert differentiation from a limit computation into algebra. Higher derivatives appear, with the second derivative reading a graph's bend.
- **Section 2.3 — The Chain Rule and Transcendental Functions.** The most-used rule in applied mathematics: how to differentiate compositions. With it come the derivatives of $e^x$, $\ln x$, and the trig functions — the promised payoffs of Section 1.2.
- **Section 2.4 — Linearization and Newton's Method.** The derivative's two superpowers: replacing a curve by its tangent line (the idea behind every first-order approximation in science) and solving equations by repeated tangent-line steps (the ancestor of modern iterative algorithms).
- **Section 2.5 — Optimization in One Variable.** The derivative as a search tool: critical points, the first- and second-derivative tests, absolute extrema on closed intervals, and applied problems — including the first least-squares computation in the book, where the humble mean turns out to be the solution to an optimization problem.

**How to study this chapter.** The rules of Sections 2.2–2.3 must become reflexes, and only repetition does that: the exercise sets are deliberately generous, and the Python sections show how to let SymPy *grade* your hand differentiation instantly. Newton's method in Section 2.4 is the first genuine *algorithm* of the book — implement it yourself before reading the provided code.

**Where it leads.** Chapter 3 runs the machine in reverse (integration). Chapter 4 pushes linearization to higher order (Taylor series). Chapter 6 rebuilds every idea here in higher dimensions, where the derivative becomes the gradient — the object machine learning actually descends — and Section 2.5's critical-point logic becomes the classification of bowls and saddles.
