# 1.1 · Functions and Their Graphs

Calculus is the mathematics of change, but before we can ask *how a quantity changes*, we need a precise way to describe *how one quantity depends on another*. That is what a function is. This section rebuilds the idea of a function carefully — its definition, its notation, its graph, and the ways functions combine — because every derivative, integral, and gradient in this book is a statement about functions, and small confusions here compound later. The section also quietly installs three skills the rest of the book leans on constantly: simplifying difference quotients (the on-ramp to derivatives), recognizing symmetry (a labor-saving device for integrals and series), and decomposing functions into simpler pieces (the prerequisite for the chain rule).

## 1.1.1 Why functions

Consider three questions a data scientist meets weekly. How does a server's response time depend on its load? How does a model's prediction error depend on a tuning parameter? How does revenue depend on price? Each asks for a *rule* connecting an input to an output. The mathematical object that captures such a rule, stripped of any particular application, is the function.

The word "rule" is doing careful work. A function is not a formula; formulas are merely one way to specify functions. A function can be given by a table of measurements, a graph, an algorithm, or a sentence, so long as the rule is unambiguous: one input, one output.

```{prf:definition} Function, domain, range
:label: def-function
A **function** $f$ from a set $A$ to a set $B$, written $f : A \to B$, is a rule that assigns to each element $x \in A$ exactly one element $f(x) \in B$.

The set $A$ of allowed inputs is the **domain** of $f$. The set $B$ is the **codomain** — the set outputs are *declared* to live in. The set of outputs actually produced, $\{\, f(x) : x \in A \,\}$, is the **range** of $f$, always a subset of the codomain.
```

The phrase *exactly one* is the entire content of the definition. A rule that sometimes gives two outputs for one input (for instance, "$y$ is a number whose square is $x$", which gives both $2$ and $-2$ when $x = 4$) is not a function. A rule that gives no output for some input in its claimed domain is not a function on that domain either. Note the asymmetry the definition allows: two *different inputs* may perfectly well share an output ($f(2) = f(-2) = 4$ for $f(x) = x^2$); it is only one input producing two outputs that is forbidden.

The codomain/range distinction is mostly bookkeeping in this book, but the vocabulary matters in data work: a model *declared* to output probabilities has codomain $[0, 1]$, and whether its range actually fills that interval — whether it ever predicts values near $0$ or $1$ — is an empirical question about the trained model, not a matter of declaration.

In this book the domain and range are subsets of the real numbers $\mathbb{R}$ unless stated otherwise, and we record sets of real numbers in **interval notation**: square brackets include an endpoint, round parentheses exclude it, and $\infty$ always takes a parenthesis, since infinity is not a number to be included. Thus

$$
[2, 5] = \{x : 2 \le x \le 5\},
\qquad
(2, 5] = \{x : 2 < x \le 5\},
\qquad
[4, \infty) = \{x : x \ge 4\},
$$

and unions glue pieces together: $(-\infty, 3) \cup (3, \infty)$ is "every real number except $3$."

When a function is given only by a formula, its domain is understood to be the **natural domain**: every real input for which the formula produces a real number. Two constraints generate almost every natural-domain problem in practice — denominators must be nonzero, and even-root radicands must be nonnegative — and the discipline is to apply *all* constraints simultaneously.

```{prf:example} Finding natural domains
:label: ex-natural-domain
Find the natural domain of each function.

**(a)** $f(x) = \dfrac{1}{x - 3}$. Division is defined except when the denominator is zero, so the domain is every real number except $3$: in interval notation, $(-\infty, 3) \cup (3, \infty)$.

**(b)** $g(x) = \sqrt{5 - x}$. A real square root requires a nonnegative radicand: $5 - x \ge 0$, so $x \le 5$. The domain is the interval $(-\infty, 5]$.

**(c)** $h(x) = \dfrac{\sqrt{x}}{x - 2}$. Both constraints apply at once: $x \ge 0$ from the square root and $x \neq 2$ from the denominator. The domain is $[0, 2) \cup (2, \infty)$.

Notice the logic of (c): each constraint carves away part of the real line, and the domain is what survives *every* cut. With more elaborate formulas the constraints multiply, but the method never changes — list them all, intersect.
```

## 1.1.2 Function notation, evaluation, and the difference quotient

The notation $f(x)$ reads "$f$ of $x$" and means *the output of $f$ at the input $x$*. It does **not** mean $f$ times $x$. The input slot accepts anything that names a number: $f(2)$, $f(-a)$, $f(x + h)$, even $f(f(x))$.

Evaluation at a compound expression is a purely mechanical substitution, but it is the single most common source of algebra errors in a calculus course, so we practice it deliberately.

```{prf:example} Evaluating at expressions
:label: ex-evaluation
Let $f(x) = x^2 - 4x + 1$. Compute $f(3)$, $f(-2)$, $f(a + 1)$, and $f(x + h)$.

Substituting the entire input into *every* occurrence of $x$:

$$
\begin{aligned}
f(3) &= 3^2 - 4(3) + 1 = 9 - 12 + 1 = -2,\\[2pt]
f(-2) &= (-2)^2 - 4(-2) + 1 = 4 + 8 + 1 = 13,\\[2pt]
f(a+1) &= (a+1)^2 - 4(a+1) + 1 = a^2 + 2a + 1 - 4a - 4 + 1 = a^2 - 2a - 2,\\[2pt]
f(x+h) &= (x+h)^2 - 4(x+h) + 1 = x^2 + 2xh + h^2 - 4x - 4h + 1.
\end{aligned}
$$

Note the parentheses around $-2$ and around $x + h$: the input is substituted as a *unit*. The classic error — writing $f(x+h)$ as $f(x) + h$ or as $x^2 + h^2 - 4x - 4h + 1$ (forgetting the cross term $2xh$) — is an error of substituting piecemeal instead of wholesale.
```

Functions defined by *different formulas on different pieces* of the domain are called **piecewise functions**, and evaluating one adds a single preliminary step: decide which piece the input belongs to, *then* substitute.

```{prf:example} Evaluating a piecewise function
:label: ex-piecewise
Let

$$
f(x) = \begin{cases}
x + 2, & x < 0,\\
x^2, & 0 \le x \le 2,\\
6 - x, & x > 2.
\end{cases}
$$

Compute $f(-1)$, $f(2)$, and $f(3)$, and describe the graph's behavior where the pieces meet.

The input $-1$ satisfies $x < 0$, so the first formula applies: $f(-1) = -1 + 2 = 1$. The input $2$ satisfies $0 \le x \le 2$ (the *middle* condition — note the inequality includes $2$), so $f(2) = 2^2 = 4$. The input $3$ satisfies $x > 2$: $f(3) = 6 - 3 = 3$.

At the seam $x = 2$, the middle piece ends at height $4$ while the right piece begins at $6 - 2 = 4$: the graph joins without a break. At the seam $x = 0$, the left piece approaches height $0 + 2 = 2$ while the middle piece starts at $0^2 = 0$: the graph **jumps**. Section 2.1 will give this distinction its official name — continuity — and piecewise seams are exactly where continuity questions live.
```

The most important compound evaluation in all of calculus is the expression

$$
\frac{f(x+h) - f(x)}{h},
$$

called the **difference quotient**. It measures the average rate of change of $f$ between $x$ and $x + h$ — output change divided by input change, a slope — and Section 2.1 will define the derivative as its limiting value as $h$ shrinks to $0$. Being able to form and simplify difference quotients cleanly *is* the algebraic prerequisite for differential calculus.

```{prf:example} Simplifying a difference quotient
:label: ex-diff-quotient
For $f(x) = x^2 - 4x + 1$, simplify $\dfrac{f(x+h) - f(x)}{h}$ for $h \neq 0$.

Using $f(x+h)$ from {prf:ref}`ex-evaluation`:

$$
\begin{aligned}
\frac{f(x+h) - f(x)}{h}
&= \frac{\bigl(x^2 + 2xh + h^2 - 4x - 4h + 1\bigr) - \bigl(x^2 - 4x + 1\bigr)}{h}\\[4pt]
&= \frac{2xh + h^2 - 4h}{h}
 = \frac{h\,(2x + h - 4)}{h}
 = 2x + h - 4.
\end{aligned}
$$

Every term without an $h$ cancels — it always does, and if it doesn't, an algebra error has occurred. (Why must it? Setting $h = 0$ in the numerator gives $f(x) - f(x) = 0$, so the numerator has no $h$-free part to leave behind.) Keep this result in mind: when $h \to 0$ in Section 2.1, it will become the derivative $2x - 4$.
```

A concrete instance makes the "average rate" reading vivid. Between $x = 1$ and $x = 1.5$ (so $h = 0.5$), the formula gives $2(1) + 0.5 - 4 = -1.5$: on that stretch, $f$ *falls* by $1.5$ output units per input unit on average. Between $x = 3$ and $x = 3.5$, it gives $2(3) + 0.5 - 4 = 2.5$: there $f$ *rises*. One simplified expression answers every such question at once — that economy is why we simplify in general rather than recomputing point by point.

## 1.1.3 Graphs

The **graph** of $f$ is the set of all points $(x, f(x))$ in the plane as $x$ runs over the domain. The graph converts the rule into a picture: the domain is the shadow of the curve on the horizontal axis, the range is its shadow on the vertical axis, and the defining "exactly one output" condition becomes geometric.

```{figure} figures/ch01-function-machine.png
:name: fig-function-machine
:alt: Graph of the parabola f(x) = x squared minus 2x plus 2, with dashed lines tracing the input x equals 3 up to the curve and across to the output f of 3 equals 5.

Reading a graph: the input $x = 3$ is traced vertically to the curve and horizontally to the output $f(3) = 5$. Every question about a function's values can be answered this way from its graph.
```

Because each input has exactly one output, no vertical line can cross the graph of a function more than once. This **vertical line test** instantly classifies curves: a parabola opening upward is a function's graph; a full circle is not (a vertical line through its interior crosses it twice).

A graph is worth interrogating systematically. For the parabola in {numref}`fig-function-machine`, $f(x) = x^2 - 2x + 2$: the domain is all of $\mathbb{R}$ (the curve's horizontal shadow covers the whole axis); the lowest point sits at $(1, 1)$, so the range is $[1, \infty)$; the curve never touches the $x$-axis, so $f(x) = 0$ has no real solutions; and the curve **decreases** on $(-\infty, 1)$ and **increases** on $(1, \infty)$. That last vocabulary deserves its official definition, because Sections 2.1–2.2 will spend serious effort *computing* where functions increase and decrease:

```{prf:definition} Increasing and decreasing
:label: def-increasing
A function $f$ is **increasing** on an interval if larger inputs give larger outputs there — $x_1 < x_2$ implies $f(x_1) < f(x_2)$ — and **decreasing** if larger inputs give smaller outputs. Graphically: the curve rises left-to-right, or falls.
```

Four families of functions supply most of this book's examples, and you should know their shapes on sight.

```{figure} figures/ch01-family-gallery.png
:name: fig-family-gallery
:alt: Four panels showing a straight line for 2x minus 1, an upward parabola for x squared, the square root curve rising and bending rightward, and the reciprocal curve 1 over x decreasing toward zero.

Four basic families. Linear functions $mx+b$ change at a constant rate $m$. Even-power functions like $x^2$ are symmetric about the vertical axis. $\sqrt{x}$ grows but ever more slowly. $1/x$ is undefined at $0$ and approaches $0$ as $x$ grows.
```

Reading the gallery closely repays the effort. The line $2x - 1$ rises by exactly $2$ for every unit step right — the constant rate $m$ is visible as constant steepness, and lines are the *only* functions with this property (a fact the derivative will make precise). The parabola $x^2$ decreases then increases, with its left half the mirror image of its right. The square root $\sqrt{x}$ increases forever but at an ever-slackening pace: from $x = 0$ to $1$ it climbs a full unit, but from $4$ to $9$ — five times the horizontal distance — it climbs only one unit more. The reciprocal $1/x$ decreases on $(0, \infty)$, plunging near $0$ and flattening toward the axis as $x$ grows: two behaviors ("blows up," "dies off") that Section 2.1's limits will make exact.

Beyond these, **polynomials** $p(x) = a_n x^n + \cdots + a_1 x + a_0$ (defined for all real $x$) and **rational functions** (ratios of polynomials, defined wherever the denominator is nonzero) will appear throughout, along with the piecewise functions of §1.1.2. The piecewise example worth memorizing is the absolute value,

$$
|x| = \begin{cases} x, & x \ge 0,\\ -x, & x < 0, \end{cases}
$$

whose V-shaped graph has a corner at the origin — a feature that will matter when we ask where derivatives exist.

### Symmetry: even and odd functions

Some graphs carry a symmetry that, once noticed, halves the work of everything done with them.

```{prf:definition} Even and odd functions
:label: def-even-odd
A function $f$ is **even** if $f(-x) = f(x)$ for every $x$ in its domain — its graph is symmetric across the $y$-axis (the left half mirrors the right). It is **odd** if $f(-x) = -f(x)$ — its graph is symmetric through the origin (rotate the right half $180°$ to get the left).
```

The names come from powers: $x^2, x^4, x^6$ are even; $x, x^3, x^5$ are odd; and sums preserve the pattern, so a polynomial with only even powers is an even function and one with only odd powers is odd. Most functions, of course, are neither. The test is always the same computation: form $f(-x)$, simplify honestly, and compare against $f(x)$ and $-f(x)$.

```{prf:example} Testing for symmetry
:label: ex-even-odd
Classify each function as even, odd, or neither: $f(x) = x^3 - x$, $\ g(x) = x^4 - 2x^2$, $\ h(x) = x^2 + x$.

**$f$:** $\ f(-x) = (-x)^3 - (-x) = -x^3 + x = -(x^3 - x) = -f(x)$. **Odd** — only odd powers appear, and the algebra confirms it.

**$g$:** $\ g(-x) = (-x)^4 - 2(-x)^2 = x^4 - 2x^2 = g(x)$. **Even** — the sign of the input never survives an even power.

**$h$:** $\ h(-x) = x^2 - x$. This equals neither $h(x) = x^2 + x$ nor $-h(x) = -x^2 - x$ (compare at $x = 1$: $h(-1) = 0$, while $h(1) = 2$ and $-h(1) = -2$). **Neither** — mixing even and odd powers generally destroys both symmetries.
```

Why care? Symmetry is a computational discount coupon that this book will redeem repeatedly: the integral of an odd function over a symmetric interval $[-a, a]$ is automatically zero and an even function's integral is twice its right half (Section 3.3); the Taylor series of an even function contains only even powers and an odd function's only odd powers (Section 4.2); and Fourier series drop half their coefficients for symmetric functions (Section 4.3). Learning to *see* symmetry now is stored labor for later.

### Transformations

New graphs come from old ones by shifting, scaling, and reflecting. If the graph of $f$ is known, then:

| New function | Effect on the graph of $f$ |
|---|---|
| $f(x) + c$ | shift **up** by $c$ (down if $c<0$) |
| $f(x - c)$ | shift **right** by $c$ (left if $c<0$) |
| $c\,f(x)$, $c > 1$ | stretch vertically by factor $c$ |
| $c\,f(x)$, $0 < c < 1$ | compress vertically by factor $c$ |
| $-f(x)$ | reflect across the $x$-axis |
| $f(-x)$ | reflect across the $y$-axis |

The organizing principle: operations applied to the *output* (adding after, multiplying after) act **vertically** and behave as expected; operations applied to the *input* (inside the parentheses) act **horizontally** and behave "backwards." The horizontal shift trips everyone at least once: $f(x - 1)$ moves the graph *right*, not left, because the input $x = 1$ now plays the role $0$ used to play — the function receives the value $x - 1$, so it needs $x$ to be one unit larger to see the same input as before.

```{figure} figures/ch01-transformations.png
:name: fig-transformations
:alt: Left panel shows the parabola x squared together with its right-shift (x minus 1) squared and its upward shift x squared plus 2. Right panel shows the same parabola with a vertical stretch 2 x squared and a reflection negative x squared.

Transformations of $y = x^2$. Left: $(x-1)^2$ shifts right by 1 and $x^2 + 2$ shifts up by 2. Right: $2x^2$ stretches vertically and $-x^2$ reflects across the $x$-axis. Notice which operations act on the input (horizontal effects) and which on the output (vertical effects).
```

Transformations compose, and when several apply at once the reliable method is to track a single well-chosen point — usually the vertex, corner, or another landmark — through the operations in order.

```{prf:example} Combining transformations
:label: ex-combined-transform
Describe the graph of $g(x) = -(x + 2)^2 + 4$ as transformations of $y = x^2$, locate its vertex, and find where it crosses the $x$-axis.

Read the formula from the inside out. Start with $x^2$; replacing $x$ by $x + 2 = x - (-2)$ shifts the graph **left by 2**; the leading minus sign then reflects it across the $x$-axis (a downward-opening parabola); adding $4$ shifts it **up by 4**. Tracking the vertex: $(0, 0) \to (-2, 0) \to (-2, 0) \to (-2, 4)$. So $g$ is a downward parabola with vertex $(-2, 4)$ — it increases on $(-\infty, -2)$ and decreases on $(-2, \infty)$, and its range is $(-\infty, 4]$.

$x$-intercepts: $-(x+2)^2 + 4 = 0$ gives $(x + 2)^2 = 4$, so $x + 2 = \pm 2$ and $x = 0$ or $x = -4$. **Check** by direct evaluation: $g(0) = -4 + 4 = 0$ ✓ and $g(-4) = -(-2)^2 + 4 = 0$ ✓ — and the two intercepts sit symmetrically about the vertex line $x = -2$, as a parabola's must, a free consistency test.
```

## 1.1.4 Composition and inverse functions

Real computations chain functions together: standardize the data, then square, then sum. Mathematics calls chaining **composition**.

```{prf:definition} Composition
:label: def-composition
Given functions $f$ and $g$, the **composition** $f \circ g$ is the function defined by

$$(f \circ g)(x) = f\bigl(g(x)\bigr),$$

whose domain consists of every $x$ in the domain of $g$ for which $g(x)$ lies in the domain of $f$. The inner function $g$ acts first.
```

Order matters. With $f(x) = x^2$ and $g(x) = x + 1$,

$$
(f \circ g)(x) = f(x+1) = (x+1)^2, \qquad (g \circ f)(x) = g(x^2) = x^2 + 1,
$$

and these differ at almost every $x$ (try $x = 1$: the first gives $4$, the second $2$).

The domain clause in the definition is not fine print — it has real consequences whenever the outer function is choosy about its inputs.

```{prf:example} The domain of a composition
:label: ex-composition-domain
Let $f(x) = \sqrt{x}$ and $g(x) = 1 - x^2$. Find formulas and domains for $f \circ g$ and $g \circ f$.

**$f \circ g$:** $\ (f\circ g)(x) = \sqrt{1 - x^2}$. The inner function $g$ accepts every real $x$, but the outer $f$ demands a nonnegative input: $1 - x^2 \ge 0$, i.e. $-1 \le x \le 1$. Domain: $[-1, 1]$. (The graph is the upper half of the unit circle — a curve we will meet again in Section 3.3's area computations.)

**$g \circ f$:** $\ (g \circ f)(x) = 1 - (\sqrt x)^2 = 1 - x$. Here is the trap: the *simplified formula* $1 - x$ is defined for all real $x$, but the *composition* is not — the inner $\sqrt x$ already refused every negative input before the simplification happened. Domain: $[0, \infty)$, inherited from the first function in the chain. A composition's domain is determined by the journey, not by the simplified destination.
```

Just as important as *composing* is *decomposing*: seeing $h(x) = \sqrt{3x + 1}$ as "the square root of $(3x+1)$", an outer function $\sqrt{\;\cdot\;}$ wrapped around an inner function $3x + 1$. The chain rule of Section 2.3 — arguably the most-used rule in applied mathematics — is exactly a rule for differentiating compositions, and applying it begins with this decomposition skill. Practice the reading direction now: $e^{-x^2}$ is "$e$ to the (negative square)"; $(2x^3 - 7)^5$ is "the fifth power of $(2x^3 - 7)$"; $\frac{1}{1 + e^{-x}}$ — the sigmoid of logistic regression — is a *three*-layer composition, "reciprocal of ($1$ plus ($e$ to the negative))."

An **inverse function** undoes a function: if $f$ sends $a$ to $b$, then $f^{-1}$ sends $b$ back to $a$, so that

$$
f^{-1}\bigl(f(x)\bigr) = x \quad\text{and}\quad f\bigl(f^{-1}(y)\bigr) = y.
$$

Not every function has an inverse. If two different inputs share an output ($f(2) = f(-2) = 4$ for $f(x) = x^2$ on all of $\mathbb{R}$), then no rule can send that output back to "the" input. A function is invertible precisely when it is **one-to-one**: distinct inputs always give distinct outputs (graphically, every *horizontal* line crosses the graph at most once). We often restore invertibility by restricting the domain — $x^2$ on $[0, \infty)$ is one-to-one, and its inverse is $\sqrt{x}$.

To find an inverse formula, write $y = f(x)$, solve for $x$ in terms of $y$, then swap the letters. For $f(x) = 3x - 5$: from $y = 3x - 5$ we get $x = (y+5)/3$, so $f^{-1}(x) = (x + 5)/3$.

```{prf:example} An inverse on a restricted domain
:label: ex-inverse-restricted
The function $f(x) = x^2 + 1$ is not one-to-one on $\mathbb{R}$. Restrict it to $[0, \infty)$, find the inverse, and state the inverse's domain and range.

On $[0, \infty)$ the function is increasing, hence one-to-one. Solve $y = x^2 + 1$ for $x$: $\ x^2 = y - 1$, and since $x \ge 0$ we take the *nonnegative* root, $x = \sqrt{y - 1}$. Swapping letters:

$$
f^{-1}(x) = \sqrt{x - 1}.
$$

Domains and ranges swap roles under inversion: $f$ has domain $[0, \infty)$ and range $[1, \infty)$ (the outputs of $x^2 + 1$ for $x \ge 0$), so $f^{-1}$ has domain $[1, \infty)$ and range $[0, \infty)$. **Check** with a concrete round trip: $f(3) = 10$, and $f^{-1}(10) = \sqrt 9 = 3$ ✓. The choice of the nonnegative root in the solving step is exactly where the domain restriction did its work — on $(-\infty, 0]$ the same algebra would have selected $-\sqrt{y-1}$ instead.
```

```{figure} figures/ch01-inverse-reflection.png
:name: fig-inverse-reflection
:alt: The curves y equals x squared for nonnegative x and y equals square root of x, shown as mirror images across the dashed line y equals x.

A function and its inverse are reflections of one another across the line $y = x$, because inverting swaps the roles of input and output — that is, swaps the two coordinate axes.
```

The reflection picture also explains a fact used later: where $f$ crosses the line $y = x$, so does $f^{-1}$ — the crossing point is its own mirror image. In {numref}`fig-inverse-reflection`, both curves pass through $(1, 1)$.

```{admonition} Common Mistakes
:class: warning
**$f^{-1}(x)$ is not $\dfrac{1}{f(x)}$.** The superscript $-1$ on a function name means *inverse function*, never reciprocal. For $f(x) = 3x - 5$, the inverse is $(x+5)/3$, while the reciprocal is $1/(3x-5)$ — completely different objects.

**$f(x+h) \neq f(x) + f(h)$ in general.** Check with $f(x) = x^2$: $f(1+1) = 4$ but $f(1) + f(1) = 2$. Substitution means replacing $x$ by the whole input, then expanding honestly.

**$f(x-c)$ shifts right, not left.** Horizontal transformations act "backwards" because they modify the input before the function sees it.

**Losing domain restrictions.** Simplifying $\frac{x^2 - 1}{x - 1}$ to $x + 1$ is valid only for $x \neq 1$; the original function is undefined there, and the restriction travels with the simplified formula. The same trap appears in compositions ({prf:ref}`ex-composition-domain`): the simplified formula's domain can be larger than the composition's true domain.

**Testing symmetry by example instead of algebra.** Checking $f(-2) = f(2)$ at one point does not prove a function even — the identity $f(-x) = f(x)$ must hold for *every* $x$, which requires algebra (or a counterexample to refute it).

**Evaluating the wrong piece.** For piecewise functions, the boundary input belongs to exactly one piece — the one whose inequality includes it. Read the $\le$ versus $<$ carefully before substituting.
```

## 1.1.5 Now do it in Python

In Python, a mathematical function becomes — fittingly — a function definition, and its graph becomes a plot built from many sampled points. The code below reproduces our running example and *verifies the hand computations* of {prf:ref}`ex-evaluation` and {prf:ref}`ex-diff-quotient`.

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """f(x) = x^2 - 4x + 1, accepting a number or a NumPy array."""
    return x**2 - 4*x + 1

# --- Verify the hand evaluations from Example 1.1.2 ---
print(f(3))     # expect -2
print(f(-2))    # expect 13

# --- Verify the simplified difference quotient from Example 1.1.4 ---
# By hand we found (f(x+h) - f(x))/h = 2x + h - 4. Test at x = 5, h = 0.1:
x, h = 5.0, 0.1
print((f(x + h) - f(x)) / h)   # direct computation
print(2*x + h - 4)             # hand-simplified formula: must match
```

Running this prints `-2`, `13`, and then `6.1` twice — the direct difference quotient and the hand-simplified formula agree exactly, which is the point: the algebra was correct. This *verify-by-computer* habit — do it by hand first, then let one line of code certify the hand work — is the working rhythm of this entire book.

SymPy can carry out the *symbolic* algebra itself, which is a useful independent check on longer simplifications:

```python
import sympy as sp

x, h = sp.symbols('x h')
f_expr = x**2 - 4*x + 1
dq = (f_expr.subs(x, x + h) - f_expr) / h
print(sp.simplify(dq))   # expect 2*x + h - 4
```

Piecewise functions vectorize with `np.piecewise` (or `np.where` for two pieces), which lets the piecewise example of {prf:ref}`ex-piecewise` be evaluated on whole arrays at once:

```python
def fpw(x):
    """The three-piece function of Example 1.1.3."""
    return np.piecewise(x,
        [x < 0, (0 <= x) & (x <= 2), x > 2],
        [lambda t: t + 2, lambda t: t**2, lambda t: 6 - t])

print(fpw(np.array([-1.0, 2.0, 3.0])))    # expect [1. 4. 3.]
```

Finally, plotting: sample the domain densely with `np.linspace`, evaluate, and draw.

```python
xs = np.linspace(-1, 5, 200)          # 200 sample points on [-1, 5]
plt.plot(xs, f(xs), label=r"$f(x) = x^2 - 4x + 1$")
plt.axhline(0, color="k", lw=0.6)
plt.xlabel("x"); plt.ylabel("f(x)")
plt.legend(); plt.show()
```

**Interpretation.** The plot shows a parabola with vertex near $x = 2$ — and completing the square, $f(x) = (x-2)^2 - 3$, confirms the vertex is exactly $(2, -3)$. The difference quotient $2x + h - 4$ is negative for $x$ well left of 2 and positive well right of 2, matching the picture: the function falls, bottoms out, then rises. Numbers, symbols, and picture tell one consistent story; when they don't, something is wrong, and finding what is how you learn.

One more experiment worth running: plot `f(xs)`, `f(xs - 1)`, and `-f(xs)` on the same axes and predict, *before* looking, which curve is which. Transformations become permanent knowledge the first time your prediction is tested against a picture you generated yourself.

```{admonition} Data Science Connection
:class: tip
Every predictive model is a function: inputs (features) go in, a prediction comes out. A trained regression model is literally a formula $f(x) = w_1 x_1 + \cdots + w_n x_n + b$; a neural network is a large *composition* of simple functions, and "feature engineering" is largely the art of applying transformations — shifts (centering), scalings (normalization), and nonlinear maps (logs, from the next section) — before the model sees the data. The vocabulary of this section — domain (what inputs are valid), range (what outputs are possible), composition (chained processing), inverse (recovering input from output) — is the working vocabulary of model-building.
```

```{admonition} Looking Ahead
:class: seealso
The difference quotient of §1.1.2 becomes the **derivative** in Section 2.1. Decomposing functions (§1.1.4) becomes the **chain rule** in Section 2.3. Even/odd symmetry (§1.1.3) pays off in integrals (Section 3.3), Taylor series (Section 4.2), and Fourier series (Section 4.3). Inverse functions return when we differentiate $\ln x$ (Section 2.3) and when we change variables in integrals (Section 3.2).
```

## 1.1.6 Exercises

### Quick Check

1. Can a function assign the output $7$ to both inputs $2$ and $5$? Can it assign both outputs $2$ and $5$ to the input $7$?
2. What is the natural domain of $f(x) = \sqrt{x - 4}$?
3. True or false: the graph of $f(x - 3)$ is the graph of $f$ shifted left by 3.
4. If $f(x) = 2x + 1$, what is $f(f(0))$?
5. Is $f(x) = x^4 + 3x^2$ even, odd, or neither?
6. For the piecewise function of {prf:ref}`ex-piecewise`, what is $f(0)$?

````{admonition} Answers to Quick Checks
:class: dropdown
1. Yes to the first (two inputs may share an output); no to the second (one input, one output — that is the definition).
2. $[4, \infty)$, since we need $x - 4 \ge 0$.
3. False — it shifts *right* by 3.
4. $f(0) = 1$, then $f(1) = 3$.
5. Even — only even powers, and $f(-x) = x^4 + 3x^2 = f(x)$.
6. The middle piece applies ($0 \le 0 \le 2$): $f(0) = 0^2 = 0$.
````

### Basic Practice

7. For $g(x) = 3x^2 - x$, compute $g(0)$, $g(-1)$, $g(2a)$, and $g(x+h)$.
8. Find the natural domain of each function, in interval notation: (a) $\dfrac{x}{x^2 - 9}$;  (b) $\sqrt{2x + 6}$;  (c) $\dfrac{1}{\sqrt{x - 1}}$;  (d) $\dfrac{\sqrt{x+2}}{x^2 - 4}$.
9. Let $f(x) = x^2 + 1$ and $g(x) = \sqrt{x}$. Find formulas and domains for $(f \circ g)(x)$ and $(g \circ f)(x)$.
10. Find the inverse of $f(x) = \dfrac{x - 2}{5}$ and verify that $f^{-1}(f(x)) = x$.
11. Classify each as even, odd, or neither, showing the $f(-x)$ computation: (a) $f(x) = 5x^3 - 2x$;  (b) $g(x) = \dfrac{1}{x^2 + 1}$;  (c) $h(x) = x^3 + 1$;  (d) $k(x) = |x|$.
12. For the piecewise function $f(x) = \begin{cases} 2x + 3, & x \le 1,\\ x^2 + 4, & x > 1,\end{cases}$ compute $f(-2)$, $f(1)$, and $f(2)$, and determine whether the graph jumps at $x = 1$.
13. Describe $g(x) = 2\,|x - 3| - 1$ as a sequence of transformations of $|x|$, and give the coordinates of the corner point.

````{admonition} Solution to Exercise 8
:class: dropdown
**(a)** The denominator factors as $(x-3)(x+3)$ and must be nonzero, so the domain is all reals except $\pm 3$: $(-\infty,-3)\cup(-3,3)\cup(3,\infty)$.

**(b)** Require $2x + 6 \ge 0$, i.e. $x \ge -3$: domain $[-3, \infty)$.

**(c)** The radicand must be nonnegative *and* the denominator nonzero, so $x - 1 > 0$ strictly: domain $(1, \infty)$. Note how the strict inequality arises from combining the two constraints.

**(d)** Two constraints: $x + 2 \ge 0$ (so $x \ge -2$) and $x^2 - 4 \ne 0$ (so $x \ne \pm 2$). Intersecting: $x \ge -2$ but $x \ne -2$ and $x \ne 2$, giving $(-2, 2) \cup (2, \infty)$ — note that the root constraint's endpoint $-2$ is *also* excluded by the denominator, so the bracket at $-2$ becomes a parenthesis.
````

````{admonition} Solution to Exercise 10
:class: dropdown
Set $y = \dfrac{x-2}{5}$ and solve for $x$: $5y = x - 2$, so $x = 5y + 2$. Swapping letters, $f^{-1}(x) = 5x + 2$. Verification:

$$
f^{-1}(f(x)) = 5\cdot\frac{x-2}{5} + 2 = (x - 2) + 2 = x. \checkmark
$$
````

````{admonition} Solution to Exercise 12
:class: dropdown
$f(-2)$: the input satisfies $x \le 1$, so $f(-2) = 2(-2) + 3 = -1$. $\ f(1)$: the boundary input belongs to the *first* piece (its inequality is $\le$): $f(1) = 2(1) + 3 = 5$. $\ f(2)$: second piece, $f(2) = 4 + 4 = 8$.

At the seam: the first piece ends at height $5$, while the second piece approaches $1^2 + 4 = 5$ as $x$ nears $1$ from the right. The two agree — the graph joins without a jump. (Section 2.1 will certify this as continuity at $x = 1$.)
````

### Intermediate Practice

14. Simplify the difference quotient $\dfrac{f(x+h)-f(x)}{h}$ completely (the $h$ in the denominator must cancel) for: (a) $f(x) = 3x^2 + 2x$;  (b) $f(x) = \dfrac{1}{x}$;  (c) $f(x) = \sqrt{x}$ *(hint: multiply by the conjugate)*;  (d) $f(x) = x^3$.
15. Write $h(x) = (2x^3 - 7)^5$ as a composition $f \circ g$ of two simpler functions, in two different ways. Then write the sigmoid $\sigma(x) = \dfrac{1}{1 + e^{-x}}$ as a composition of *three* functions.
16. The function $f(x) = x^2 - 6x + 5$ is not one-to-one on $\mathbb{R}$. Find the largest interval of the form $[c, \infty)$ on which it *is* one-to-one, and find the inverse on that interval.
17. Prove that the product of two odd functions is even, and that the product of an even function and an odd function is odd. Verify each claim with a concrete pair from Exercise 11.
18. A function satisfies $f(1) = 4$ and is known to be odd. Find $f(-1)$, and explain why $f(0)$ must equal $0$ for any odd function whose domain contains $0$.

````{admonition} Hint for Exercise 14(b)
:class: dropdown
Combine $\frac{1}{x+h} - \frac{1}{x}$ over the common denominator $x(x+h)$ before dividing by $h$.
````

````{admonition} Solution to Exercise 14(b)
:class: dropdown
$$
\frac{1}{h}\left(\frac{1}{x+h} - \frac{1}{x}\right)
= \frac{1}{h}\cdot\frac{x - (x+h)}{x(x+h)}
= \frac{1}{h}\cdot\frac{-h}{x(x+h)}
= \frac{-1}{x(x+h)}.
$$

As a preview of Section 2.1: letting $h \to 0$ gives $-1/x^2$, which will be the derivative of $1/x$.
````

````{admonition} Solution to Exercise 18
:class: dropdown
Oddness says $f(-x) = -f(x)$, so $f(-1) = -f(1) = -4$. At zero the identity reads $f(-0) = -f(0)$, i.e. $f(0) = -f(0)$, forcing $2f(0) = 0$ and $f(0) = 0$: every odd function defined at the origin passes through it.
````

### Conceptual Understanding

19. Explain, using the definition of a function, why the vertical line test works.
20. Your colleague claims that because $(f\circ g)(x)$ and $(g \circ f)(x)$ are both "just $f$ and $g$ combined," they must be equal. Refute the claim with a concrete example and one sentence of explanation.
21. A dataset records daily temperature at noon for one year. Explain in what sense this table *is* a function, and identify its domain and a reasonable codomain.
22. The horizontal line test detects one-to-one functions, and the vertical line test detects functions. Explain why the *horizontal* test on $f$ is exactly the *vertical* test on the reflected curve that would be $f^{-1}$'s graph — and what this says about when the reflection is a function at all.

### Python Practice

23. Define `f(x) = x**3 - 2*x` in Python and verify numerically, at three different points, that your hand-simplified difference quotient from Exercise 14(d)'s pattern is correct for $h = 0.01$.
24. Use SymPy's `simplify` to check your answers to Exercise 14(a) and 14(c).
25. Implement the piecewise function of Exercise 12 with `np.piecewise`, evaluate it on `np.linspace(-3, 4, 8)`, and confirm the three hand-computed values.
26. Write a function `is_even_numeric(f, n=1000)` that samples $n$ random points $x$ and reports the maximum of $|f(-x) - f(x)|$; run it on the four functions of Exercise 11 and reconcile the outputs with your hand classifications. Explain in a comment why a tiny-but-nonzero maximum still means "even" in floating-point arithmetic, and why this numerical test can *suggest* but never *prove* evenness.

### Visualization Practice

27. Plot $f(x) = |x - 2| + 1$ on $[-2, 6]$. Identify the corner point from the plot and explain algebraically why it occurs there.
28. On one set of axes, plot $\sqrt{x}$, $\sqrt{x - 2}$, and $\sqrt{x} - 2$ on suitable domains, with a legend. Write one sentence explaining how the three graphs are related.
29. Plot the piecewise function of {prf:ref}`ex-piecewise` on $[-2, 4]$, using a dense grid, and mark the two seam points. Which seam shows a jump, and does the picture agree with the example's analysis?
30. Plot $f(x) = x^3 - x$ and $g(x) = x^4 - 2x^2$ from {prf:ref}`ex-even-odd` on $[-2, 2]$, one per panel, and annotate each with its symmetry type. Describe in one sentence how each symmetry is visible.

### Challenge

31. Suppose $f$ is one-to-one and $g(x) = f(x - 3) + 4$. Express $g^{-1}$ in terms of $f^{-1}$, and verify your formula on the concrete case $f(x) = x^3$.
32. Show that $f(x) = \dfrac{x}{1 + |x|}$ is one-to-one on all of $\mathbb{R}$, find its range, and find a formula for $f^{-1}$ on that range. *(This function compresses the whole real line into $(-1, 1)$ — a "squashing" map in the same family as machine learning's activation functions.)*
33. Every function $f$ defined on all of $\mathbb{R}$ splits uniquely into an even part plus an odd part:

    $$
    f(x) = \underbrace{\frac{f(x) + f(-x)}{2}}_{\text{even}} + \underbrace{\frac{f(x) - f(-x)}{2}}_{\text{odd}}.
    $$

    Verify that the two pieces have the claimed symmetries, and compute the decomposition explicitly for $f(x) = x^2 + x$ and for $f(x) = e^x$. *(The second answer defines the hyperbolic functions $\cosh$ and $\sinh$ — see Section 1.2's Challenge exercises, where they reappear.)*

## 1.1.7 Summary

A function is a rule assigning exactly one output to each input; its domain is the set of legal inputs (recorded in interval notation), its range the set of realized outputs inside a declared codomain. Function notation is substitution of the *entire* input — piecewise functions add only the preliminary step of choosing the right piece — and mastery of the difference quotient $\frac{f(x+h)-f(x)}{h}$, the average rate of change, is the direct on-ramp to derivatives. Graphs turn rules into curves (vertical line test), read off domain, range, and increasing/decreasing behavior, and reveal even/odd symmetry ($f(-x) = \pm f(x)$), a discount coupon redeemed repeatedly in later sections. Standard transformations — shifts, stretches, reflections, with input-side operations acting horizontally and "backwards" — generate families of graphs from a few memorized shapes, trackable through landmark points when combined. Composition chains functions with order mattering and with domains inherited from the journey rather than the simplified formula; decomposition is the skill the chain rule will require. Inverses undo one-to-one functions (restoring one-to-one-ness by domain restriction when needed), swap domain with range, and mirror graphs across $y = x$. In Python, functions become `def` (piecewise ones `np.piecewise`), graphs become `plt.plot` over `np.linspace` samples, and NumPy verifies values while SymPy verifies algebra — the do-by-hand-then-confirm rhythm of the whole book.

*Parallel reading:* OpenStax *Calculus Volume 1*, Chapter 1 (Functions and Graphs) {cite}`openstax_calc1`.
