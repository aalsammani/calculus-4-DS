# 2.5 · Optimization in One Variable

Much of applied mathematics reduces to a single imperative: make this quantity as large or as small as possible. A business prices a product to maximize revenue; an engineer shapes a container to minimize material; a statistician chooses the parameter that minimizes error. The derivative was built to detect change, and this section turns that detector into a search tool: at the top of a smooth hill or the bottom of a smooth valley, the tangent line is horizontal, so *the places where $f'$ vanishes are the only interior places worth checking*. That one observation, plus care at endpoints, is the entire method — and it is the one-variable ancestor of the gradient-based optimization that trains every modern statistical model (Section 6.3 tells that story in full).

## 2.5.1 Extrema and critical points

```{prf:definition} Local and absolute extrema
:label: def-extrema-1d
A function $f$ has a **local maximum** at $c$ if $f(c) \ge f(x)$ for all $x$ near $c$ (in some open interval around $c$), and a **local minimum** if $f(c) \le f(x)$ for all $x$ near $c$. It has an **absolute maximum** on a set $D$ at $c$ if $f(c) \ge f(x)$ for *every* $x$ in $D$, and an **absolute minimum** if $f(c) \le f(x)$ for every $x$ in $D$. Maxima and minima together are called **extrema**.
```

The distinction matters: a local extremum wins only against its neighbors, while an absolute extremum wins against the whole domain. A rolling landscape can have many local valleys but only one lowest point — or several tied for lowest, as an example below will show.

Where can extrema hide? If $f$ has a local extremum at an interior point $c$ and $f'(c)$ exists, then the tangent there cannot slope upward (a small step right would climb higher, contradicting a maximum) and cannot slope downward (a small step left would). The only remaining possibility:

```{prf:theorem} Fermat's theorem on extrema
:label: thm-fermat
If $f$ has a local extremum at an interior point $c$ of its domain and $f'(c)$ exists, then $f'(c) = 0$.
```

```{prf:definition} Critical point
:label: def-critical-1d
A **critical point** of $f$ is an interior point $c$ of its domain where $f'(c) = 0$ or $f'(c)$ does not exist.
```

Fermat's theorem is a *search warrant*, not a verdict: it says every interior extremum sits at a critical point, so the critical points are the complete list of suspects. It does **not** say every critical point is an extremum. The standard counterexample is $f(x) = x^3$ at $x = 0$: the derivative $3x^2$ vanishes there, yet the function is increasing on both sides — the graph merely flattens momentarily as it passes through. And the absolute value $|x|$ shows the second kind of critical point: no derivative exists at the corner $x = 0$, and that corner is a genuine minimum. Both suspects must always be rounded up.

## 2.5.2 The first-derivative test

A critical point is classified by what the function is *doing on either side of it*, which is exactly what the sign of $f'$ reports (Section 2.2's increasing/decreasing connection).

If $f'$ changes from positive to negative at a critical point $c$, then $f$ rises into $c$ and falls away from it: a **local maximum**. If $f'$ changes from negative to positive: a **local minimum**. If $f'$ has the *same sign* on both sides, the critical point is neither — the $x^3$ situation.

```{prf:example} A sign chart in action
:label: ex-fdt-cubic
Find and classify the critical points of $f(x) = x^3 - 3x^2$.

Differentiate and factor: $f'(x) = 3x^2 - 6x = 3x(x - 2)$, which vanishes at $x = 0$ and $x = 2$ — the only critical points, since $f'$ exists everywhere. Now chart the sign of $f'$ on the three intervals the critical points create, testing one convenient point in each:

| interval | test point | $3x(x-2)$ | $f$ is |
|---|---|---|---|
| $x < 0$ | $x = -1$ | $(-)(-) = +$ | increasing |
| $0 < x < 2$ | $x = 1$ | $(+)(-) = -$ | decreasing |
| $x > 2$ | $x = 3$ | $(+)(+) = +$ | increasing |

At $x = 0$ the derivative flips from $+$ to $-$: a **local maximum**, with $f(0) = 0$. At $x = 2$ it flips from $-$ to $+$: a **local minimum**, with $f(2) = 8 - 12 = -4$. Neither is absolute on $\mathbb{R}$ — the cubic runs off to $-\infty$ on the left and $+\infty$ on the right, so no global champion exists. Local analysis and global behavior are separate questions, and both were needed to tell the whole story.
```

## 2.5.3 The second-derivative test

There is a faster classifier when the second derivative is easy to compute. At a critical point $c$ with $f'(c) = 0$, the graph is momentarily flat; the second derivative reports which way it *bends* (Section 2.2's concavity). Bending upward from a flat tangent means the point sits at the bottom of a bowl; bending downward, at the top of a dome.

```{prf:theorem} Second-derivative test
:label: thm-second-deriv
Suppose $f'(c) = 0$ and $f''(c)$ exists. If $f''(c) > 0$, then $f$ has a local minimum at $c$. If $f''(c) < 0$, a local maximum. If $f''(c) = 0$, the test is **inconclusive** and the first-derivative test must decide.
```

Rerunning {prf:ref}`ex-fdt-cubic` this way: $f''(x) = 6x - 6$, so $f''(0) = -6 < 0$ (local maximum ✓) and $f''(2) = 6 > 0$ (local minimum ✓) — the same verdicts in two lines. The inconclusive case is real, not a technicality: $x^4$, $-x^4$, and $x^3$ all have $f'(0) = f''(0) = 0$, yet the first has a minimum at the origin, the second a maximum, and the third neither. When the test shrugs, fall back on the sign chart, which never does.

## 2.5.4 Absolute extrema on a closed interval

Many applied problems constrain the variable to a closed interval $[a, b]$ — a budget between $0$ and the maximum, a dosage between $0$ and a safety ceiling. On such intervals a continuous function is guaranteed its champions:

```{prf:theorem} Extreme value theorem
:label: thm-evt
A function continuous on a closed interval $[a, b]$ attains an absolute maximum and an absolute minimum somewhere on $[a, b]$.
```

Both hypotheses earn their keep. On the *open* interval $(0, 1)$ the continuous function $1/x$ has no maximum (it blows up near $0$), and on $[0,1]$ a function with a jump can likewise escape having one. Continuity on a closed interval closes every loophole — and, combined with Fermat's theorem, it yields an algorithm with no judgment calls in it, the **closed-interval method**: the absolute extrema live either at critical points inside $(a,b)$ or at the endpoints, so evaluate $f$ at every critical point and at both endpoints, and read off the largest and smallest values.

```{prf:example} The closed-interval method
:label: ex-closed-interval
Find the absolute extrema of $f(x) = x^3 - 3x^2 + 1$ on $[-1, 4]$.

Critical points: $f'(x) = 3x(x-2) = 0$ at $x = 0$ and $x = 2$, both inside the interval. Evaluate $f$ at the four candidates:

$$
f(-1) = -3, \qquad f(0) = 1, \qquad f(2) = -3, \qquad f(4) = 17.
$$

The **absolute maximum is $17$**, attained at the endpoint $x = 4$, and the **absolute minimum is $-3$**, attained *twice* — at the endpoint $x = -1$ and at the interior critical point $x = 2$. {numref}`fig-extrema-interval` shows the geometry: the local maximum at $x=0$ from {prf:ref}`ex-fdt-cubic` is real but loses the global contest to the right endpoint, and a tie for the minimum is perfectly legal — the *value* $-3$ is unique even though its location is not.
```

```{figure} figures/ch26-extrema.png
:name: fig-extrema-interval
:alt: The cubic x cubed minus 3 x squared plus 1 plotted on the interval from minus 1 to 4, with the two interior critical points and the two endpoints marked, showing the absolute maximum at the right endpoint and a tie for the absolute minimum between the left endpoint and the interior minimum.

The closed-interval method for $f(x) = x^3 - 3x^2 + 1$ on $[-1, 4]$: every absolute extremum is either a critical point (red) or an endpoint (orange). Here the maximum is at an endpoint and the minimum is attained at two different places.
```

## 2.5.5 Applied optimization

Real optimization problems arrive as sentences, not formulas, and the work divides cleanly: *translate*, then *optimize*. The translation step — name the variable, write the target quantity, use the constraint to eliminate all variables but one, and record the meaningful domain — is where most of the difficulty and most of the errors live. The optimization step is then this section's machinery.

```{prf:example} Least material for a box
:label: ex-box-min
An open-topped box with a square base must hold $32$ cubic decimeters. What dimensions use the least material?

*Translate.* Let the base edge be $x$ and the height $h$ (both positive). The constraint is volume: $x^2 h = 32$, so $h = 32/x^2$. The target is surface area (base plus four sides):

$$
S = x^2 + 4xh = x^2 + 4x\cdot\frac{32}{x^2} = x^2 + \frac{128}{x}, \qquad x > 0.
$$

*Optimize.* $S'(x) = 2x - \dfrac{128}{x^2}$, and $S' = 0$ gives $2x^3 = 128$, so $x^3 = 64$ and $x = 4$. The second derivative $S''(x) = 2 + 256/x^3$ is positive for every $x>0$, so $x=4$ is a local minimum — and since $S \to \infty$ both as $x \to 0^+$ (the sides blow up) and as $x \to \infty$ (the base does), it is the absolute minimum on the domain.

*Answer.* Base $4 \times 4$, height $h = 32/16 = 2$, using $S(4) = 16 + 32 = 48$ square decimeters. A box half as tall as it is wide — a proportion worth remembering, because it recurs across open-box problems.
```

```{prf:example} The mean as an optimizer
:label: ex-mean-msq
Three measurements come in: $y_1 = 1$, $y_2 = 3$, $y_3 = 5$. What single number $c$ best summarizes them, if "best" means minimizing the total squared error $g(c) = (1-c)^2 + (3-c)^2 + (5-c)^2$?

Differentiate with respect to $c$ (the chain rule on each square):

$$
g'(c) = -2(1-c) - 2(3-c) - 2(5-c) = -2\bigl[(1+3+5) - 3c\bigr] = 6c - 18,
$$

which vanishes at $c = 3$, and $g''(c) = 6 > 0$ certifies a minimum — the absolute minimum, since $g$ is an upward-opening parabola in $c$. The optimal summary is $c = 3 = \dfrac{1+3+5}{3}$: **the mean**. Nothing about the numbers $1, 3, 5$ was special; the same computation with general data $y_1, \ldots, y_n$ gives $g'(c) = -2\sum_i (y_i - c) = 0$ exactly at $c = \bar y$ (Exercise 14). The arithmetic mean is not a convention — it is the *solution to an optimization problem*, the first least-squares fit in this book and the ancestor of every regression to come.
```

```{admonition} Common Mistakes
:class: warning
**Declaring every critical point an extremum.** $f'(c) = 0$ makes $c$ a *candidate*, nothing more; $x^3$ at $0$ is the standing counterexample. Classification — by sign chart or second derivative — is a separate, mandatory step.

**Forgetting the endpoints.** On a closed interval, the extreme value theorem's champions are frequently *at* the boundary, where $f'$ need not vanish at all. In {prf:ref}`ex-closed-interval`, both the maximum and half of the minimum live at endpoints. Critical points alone are not the whole candidate list.

**Trusting the second-derivative test when it is silent.** $f''(c) = 0$ decides nothing — return to the first-derivative sign chart, which always decides.

**Optimizing before eliminating.** In applied problems, differentiate only after the constraint has reduced the target to *one* variable, and only with respect to that variable. Differentiating $S = x^2 + 4xh$ with $h$ still present treats a dependent quantity as constant and produces nonsense.

**Ignoring the domain that the story implies.** Lengths are positive, probabilities live in $[0,1]$, counts are nonnegative. An algebraic critical point outside the meaningful domain — or a domain endpoint the algebra never sees — can silently invalidate an answer. State the domain when you translate, and check your candidate against it.
```

## 2.5.6 Now do it in Python

SymPy mechanizes the entire pipeline — differentiate, solve, classify — and verifies {prf:ref}`ex-fdt-cubic` and {prf:ref}`ex-box-min` in a few lines.

```python
import sympy as sp

x = sp.Symbol('x', positive=True)

# --- Verify the box example: S(x) = x^2 + 128/x ---
S = x**2 + 128/x
crit = sp.solve(sp.diff(S, x), x)
print(crit)                                  # expect [4]
print(S.subs(x, crit[0]))                    # expect 48
print(sp.diff(S, x, 2).subs(x, crit[0]))     # expect 6  (> 0: minimum)

# --- Verify the sign-chart example: f(x) = x^3 - 3x^2 on all of R ---
t = sp.Symbol('t', real=True)
f = t**3 - 3*t**2
cps = sp.solve(sp.diff(f, t), t)
for c in cps:
    print(c, f.subs(t, c), sp.diff(f, t, 2).subs(t, c))
# expect: 0 -> value 0, f'' = -6 (max);  2 -> value -4, f'' = 6 (min)
```

SciPy attacks the same problems *numerically*, which matters the moment a function has no clean symbolic derivative. `minimize_scalar` needs only the function itself:

```python
from scipy.optimize import minimize_scalar

res = minimize_scalar(lambda x: x**2 + 128/x, bounds=(0.1, 20), method='bounded')
print(res.x, res.fun)        # expect approximately 4.0000 and 48.0000
```

**Interpretation.** The symbolic route returns the *exact* answers $x = 4$, $S = 48$, with a proof attached (the sign of $S''$); the numerical route returns floating-point approximations that agree to many digits but certify nothing beyond "this is the best point my search visited." The two are partners: symbolics for structure and exactness where formulas cooperate, numerics for reach when they do not. Run both and compare — a disagreement means a bug, and finding it is the lesson. A worthwhile experiment: plot $S(x)$ on $(0, 12]$ before optimizing anything, and confirm your eye lands the minimum near $x = 4$ before either library does.

```{admonition} Data Science Connection
:class: tip
Training a model *is* this section, industrialized. A loss function measures error as a function of the parameters; "training" means finding the parameter values that minimize it; and the search proceeds by exactly Fermat's logic — seek the places where derivatives vanish. {prf:ref}`ex-mean-msq` is the one-parameter case in miniature: squared-error loss, differentiate, set to zero, and the optimizer turns out to be the sample mean. With more parameters the derivative becomes Section 6.3's gradient and the second-derivative test becomes an eigenvalue check on Section 6.2's Hessian, but the skeleton — candidates where derivatives vanish, then classify, then respect the domain — never changes.
```

```{admonition} Looking Ahead
:class: seealso
Section 6.3 rebuilds this section in higher dimensions: $f'(c)=0$ becomes $\nabla f = \vb 0$, the second-derivative test becomes the Hessian's eigenvalue signs, and a genuinely new creature appears — the saddle point, uphill one way and downhill another. Newton's method (Section 2.4) joins the story as an *optimizer* by solving $f'(x) = 0$ instead of $f(x)=0$. And the box example's pattern — eliminate the constraint, then optimize — is the hand-sized version of constrained optimization, whose general machinery (Lagrange multipliers) awaits in later courses; Section 6.3's exercises preview it.
```

## 2.5.7 Exercises

### Quick Check

1. Find the critical point of $f(x) = x^2 - 6x$.
2. True or false: if $f'(c) = 0$, then $f$ has a local extremum at $c$.
3. What is the absolute maximum of $f(x) = 4 - x^2$ over all of $\mathbb{R}$, and where is it attained?
4. At a critical point $c$, you compute $f''(c) = 5$. What do you conclude?
5. Why can the absolute minimum of a continuous function on $[a,b]$ fail to be at a critical point?

````{admonition} Answers to Quick Checks
:class: dropdown
1. $f'(x) = 2x - 6 = 0$ at $x = 3$.
2. False — $x^3$ at $c=0$ is the standard counterexample; classification is a separate step.
3. Maximum $4$ at $x = 0$: the parabola opens downward, so its vertex is the global top.
4. $f''(c) > 0$ with $f'(c)=0$: a local minimum at $c$.
5. It may sit at an endpoint, where the derivative need not vanish — endpoints are always candidates alongside critical points.
````

### Basic Practice

6. Find and classify all critical points of $f(x) = x^3 - 12x$ using the second-derivative test, and give the local extreme values.
7. For $f(x) = x^4 - 4x^3$: find both critical points, build the sign chart of $f'$, and explain why one critical point is an extremum while the other is not.
8. Use the closed-interval method on $f(x) = x^2 - 4x + 5$ over $[0, 3]$.
9. Show that $f(x) = x + \dfrac{4}{x}$ has an absolute minimum on $(0,\infty)$, and find it.
10. Find and classify the critical points of $f(x) = \sin x$ on $(0, 2\pi)$ using the second-derivative test.

````{admonition} Solution to Exercise 7
:class: dropdown
$f'(x) = 4x^3 - 12x^2 = 4x^2(x-3)$, giving critical points $x = 0$ and $x = 3$. Sign chart: the factor $4x^2$ is nonnegative everywhere, so the sign of $f'$ is the sign of $(x - 3)$ — negative on $(-\infty, 0)$, still negative on $(0,3)$, positive on $(3,\infty)$.

At $x = 3$ the sign flips $-$ to $+$: a **local minimum**, $f(3) = 81 - 108 = -27$. At $x = 0$ there is **no sign change** — the function decreases into the point and keeps decreasing out of it, pausing flat for an instant — so $x=0$ is a critical point that is *not* an extremum. (The second-derivative test would have shrugged there: $f''(x) = 12x^2 - 24x$ gives $f''(0)=0$, inconclusive, which is why the sign chart is the tool of last resort that always answers.)
````

````{admonition} Solution to Exercise 9
:class: dropdown
$f'(x) = 1 - \dfrac{4}{x^2} = 0$ gives $x^2 = 4$, and on the domain $(0,\infty)$ only $x = 2$ qualifies. Classify: $f''(x) = \dfrac{8}{x^3} > 0$ for all $x>0$, so $x=2$ is a local minimum with $f(2) = 2 + 2 = 4$. It is *absolute* because $f \to \infty$ at both ends of the domain — as $x\to 0^+$ the term $4/x$ blows up, and as $x \to \infty$ the term $x$ does — so the single interior valley is the global one. (No endpoint check applies: the domain is open, and the blow-up analysis replaces it.)
````

### Intermediate Practice

11. Find the absolute maximum of $f(x) = x e^{-x}$ on $[0, \infty)$, classifying the critical point and explaining why the maximum is absolute.
12. Find the minimum value of $f(x) = x^2 \ln x$ on $(0, \infty)$, exactly.
13. A farmer has $200$ meters of fencing for a rectangular field that borders a straight river; the river side needs no fence. Find the dimensions that maximize the enclosed area, and the maximum area.
14. Generalize {prf:ref}`ex-mean-msq`: for data $y_1, \ldots, y_n$, show that $g(c) = \sum_{i=1}^n (y_i - c)^2$ is minimized exactly at the sample mean $c = \bar y = \frac1n\sum_i y_i$, and verify $g''>0$.
15. Find the point on the curve $y = \sqrt{x}$ closest to the point $(3, 0)$. *(Minimize the squared distance — it has the same minimizer as the distance and differentiates more cleanly.)*

````{admonition} Hint for Exercise 13
:class: dropdown
Let $x$ be the length of each of the two sides perpendicular to the river. Then the side parallel to the river uses the remaining $200 - 2x$ meters, the area is $A(x) = x(200 - 2x)$, and the meaningful domain is $0 < x < 100$.
````

````{admonition} Solution to Exercise 15
:class: dropdown
A point on the curve is $(x, \sqrt x)$ with $x \ge 0$, and its squared distance to $(3,0)$ is

$$
D(x) = (x-3)^2 + (\sqrt x)^2 = (x-3)^2 + x .
$$

Then $D'(x) = 2(x-3) + 1 = 2x - 5$, vanishing at $x = \tfrac52$, with $D'' = 2 > 0$: a minimum. The closest point is $\bigl(\tfrac52, \sqrt{5/2}\bigr)$, at squared distance $D(\tfrac52) = \tfrac14 + \tfrac52 = \tfrac{11}{4}$, i.e. distance $\dfrac{\sqrt{11}}{2} \approx 1.658$. Endpoint check: $D(0) = 9 > \tfrac{11}{4}$, and $D \to \infty$ as $x \to\infty$, so the interior candidate wins. (Geometry offers a free verification: the segment from $(3,0)$ to $\bigl(\tfrac52,\sqrt{5/2}\bigr)$ is perpendicular to the curve's tangent there — closest approach always meets a smooth curve at a right angle.)
````

### Conceptual Understanding

16. The extreme value theorem needs both hypotheses. Give one example of a continuous function on an *open* interval with no absolute maximum, and explain in a sentence what goes wrong.
17. Sketch (by hand) a single function on $[-2, 2]$ that has: a critical point that is not an extremum, a local minimum where $f'$ does not exist, and its absolute maximum at an endpoint. Label each feature.
18. Your colleague finds $f'(c) = 0$ and $f''(c) = 0$ and concludes "so $c$ is an inflection point, not an extremum." Refute this with a specific function, and state what can actually be concluded.

### Python Practice

19. Use SymPy to find and classify the critical points in Exercises 11 and 12: solve $f' = 0$, evaluate $f''$ at each solution, and print the exact extreme values.
20. Solve the fence problem (Exercise 13) numerically with `scipy.optimize.minimize_scalar` (minimize $-A(x)$ on a suitable bracket), and confirm the answer matches your hand solution to at least six digits.

### Visualization Practice

21. Plot $f(x) = x^4 - 4x^3$ on $[-1.5, 4.5]$, marking both critical points, and annotate which is an extremum. Confirm visually the "flat pause without a turn" at $x = 0$ from Exercise 7.

### Challenge

22. Among all rectangles with a fixed perimeter $P$, prove that the square encloses the largest area. Then reconcile your calculus proof with the algebraic identity $xy = \left(\frac{x+y}{2}\right)^2 - \left(\frac{x-y}{2}\right)^2$, which proves the same fact without calculus.
23. For the general quadratic $f(x) = ax^2 + bx + c$ with $a > 0$: show that the unique critical point $x = -\dfrac{b}{2a}$ is the absolute minimum, first by the second-derivative test and then by completing the square. Explain why for this function — unlike the cubics of this section — *local* minimum automatically implies *global*, and which property of $f''$ is responsible. *(That property has a name, convexity, and it dominates the modern theory of optimization.)*

## 2.5.8 Summary

Extrema come in two strengths — local (best among neighbors) and absolute (best on the whole domain) — and Fermat's theorem confines every interior extremum of a differentiable function to the critical points, where $f' = 0$ or fails to exist; the warrant identifies suspects but convicts no one, since critical points like $x^3$'s origin are neither peak nor valley. Conviction comes from classification: the first-derivative test reads the sign change of $f'$ across the point (and always reaches a verdict), while the faster second-derivative test reads the bend — $f''(c)>0$ a minimum, $f''(c)<0$ a maximum, $f''(c)=0$ silence. On a closed interval, the extreme value theorem guarantees absolute extrema for continuous functions and the closed-interval method finds them by brute candidate comparison: critical points plus endpoints, evaluate, pick. Applied problems add a translation layer — name the variable, write the target, spend the constraint to reach one variable, state the meaningful domain — after which the machinery is unchanged; the open box yields base $4$, height $2$, and the least-squares summary of data turns out to be the mean, the book's first sighting of the optimization view of statistics. In Python, SymPy runs the exact pipeline (solve $f'=0$, sign of $f''$) and SciPy's `minimize_scalar` runs the numerical one; exactness and reach, verified against each other.

*Parallel reading:* OpenStax *Calculus Volume 1*, Sections 4.3 (Maxima and Minima), 4.5 (Derivatives and the Shape of a Graph), and 4.7 (Applied Optimization Problems) {cite}`openstax_calc1`.
