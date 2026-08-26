# 1.2 · Exponentials, Logarithms, and Trigonometry

Three families of functions appear so often in calculus and data science that they deserve a chapter of their own before the calculus begins: exponential functions, their inverses the logarithms, and the trigonometric functions. Each will be differentiated in Section 2.3 and integrated in Chapter 3; here we make sure their algebra and their graphs are second nature. The section's through-line is a single question asked three times: *what kind of change does each family describe?* Exponentials describe proportional change (growth and decay by a fixed factor), logarithms describe the inverse question (how long, how many doublings), and sines and cosines describe periodic change (anything that cycles). Between them, these three cover a remarkable share of the quantitative world.

## 1.2.1 Exponential functions

Linear growth adds a fixed *amount* per step; exponential growth multiplies by a fixed *factor* per step. A quantity that doubles daily, a population growing 3% per year, an investment compounding, an epidemic in its early phase, the loss decay of a training run — all are exponential.

```{prf:definition} Exponential function
:label: def-exponential
For a base $b > 0$ with $b \neq 1$, the **exponential function with base $b$** is

$$f(x) = b^x, \qquad x \in \mathbb{R},$$

with domain all of $\mathbb{R}$ and range $(0, \infty)$. It is increasing when $b > 1$ (**growth**) and decreasing when $0 < b < 1$ (**decay**).
```

The laws of exponents govern all algebra with these functions. For $b > 0$ and all real $x, y$:

$$
b^x b^y = b^{x+y}, \qquad \frac{b^x}{b^y} = b^{x-y}, \qquad (b^x)^y = b^{xy}, \qquad b^0 = 1, \qquad b^{-x} = \frac{1}{b^x}.
$$

Growth and decay are two faces of the same definition, because $\left(\tfrac12\right)^x = 2^{-x}$: a base below $1$ is just a base above $1$ run backwards. The standard modeling templates are worth naming now, since they recur throughout science and data work:

$$
\underbrace{Q(t) = Q_0\, b^{t}}_{\text{growth by factor } b \text{ per unit time}},
\qquad
\underbrace{Q(t) = Q_0 \left(\tfrac{1}{2}\right)^{t/T}}_{\text{decay with \textbf{half-life} } T},
\qquad
\underbrace{Q(t) = Q_0\, 2^{\,t/T}}_{\text{growth with \textbf{doubling time} } T}.
$$

```{prf:example} Exponential decay: how much caffeine is left?
:label: ex-caffeine-decay
Caffeine leaves the body with a half-life of roughly $5$ hours. If a cup of coffee delivers $Q_0 = 100$ mg at 8 AM, how much remains at 8 PM?

Twelve hours is $12/5 = 2.4$ half-lives, so

$$
Q(12) = 100\left(\tfrac12\right)^{12/5} = 100 \cdot 2^{-2.4} \approx 18.9 \text{ mg}.
$$

**Interpretation.** After two half-lives (10 hours) a quarter remains — $25$ mg — and the extra $0.4$ of a half-life trims that to about $19$ mg. Notice what the half-life template buys: no calculus, no rate constants, just *counting half-lives*, possibly fractionally. The same arithmetic governs radioactive dating, drug dosing schedules, and the decay of a cache's hit rate — anything that loses a fixed *fraction* per unit time.
```

### The number $e$

Among all bases, one is special, and the classic route to it runs through compound interest. Invest \$1 at 100% annual interest. Compounded once, it becomes \$2. Compounded twice (50% each half-year), it becomes $\left(1 + \tfrac12\right)^2 = \$2.25$. Compounded $n$ times, it becomes $\left(1 + \tfrac1n\right)^n$ — and as $n$ grows, this quantity does not blow up but *settles*:

$$
\left(1 + \tfrac{1}{1}\right)^1 = 2, \quad
\left(1 + \tfrac{1}{10}\right)^{10} \approx 2.5937, \quad
\left(1 + \tfrac{1}{100}\right)^{100} \approx 2.7048, \quad
\left(1 + \tfrac{1}{10^6}\right)^{10^6} \approx 2.71828.
$$

The limiting value is the number

$$
e = 2.718281828\ldots,
$$

the yield of *continuous* compounding — interest computed at every instant. More generally, principal $P$ compounded continuously at rate $r$ for $t$ years grows to $P e^{rt}$, while $n$-times-per-year compounding gives $P\left(1 + \tfrac rn\right)^{nt}$.

```{prf:example} Compounding frequencies compared
:label: ex-compounding
\$1000 is invested at 5% annual interest for 10 years. Compare annual, monthly, and continuous compounding.

$$
\text{Annual: } 1000(1.05)^{10} = \$1628.89,
\qquad
\text{Monthly: } 1000\left(1 + \tfrac{0.05}{12}\right)^{120} = \$1647.01,
$$

$$
\text{Continuous: } 1000\,e^{0.05 \times 10} = 1000\,e^{0.5} = \$1648.72.
$$

**Interpretation.** More frequent compounding earns more — interest starts earning interest sooner — but with rapidly diminishing returns: going from annual to monthly gains \$18, while going from monthly to *every instant* gains only \$1.71 more. Continuous compounding is the ceiling, and $e$ is its base. This is why $e^{rt}$, not $b^t$, is the default template in the sciences: continuous processes (populations, reactions, heat, charge) compound continuously by nature.
```

Beyond this story, $e$ has a second claim to fame that is really the same fact in disguise: it is the base for which the exponential curve's *slope* at any point equals its *height* at that point — a property we will prove in Section 2.3 and which makes $e^x$ the native exponential of calculus. Any exponential converts to base $e$, since $b^x = e^{x \ln b}$, so no generality is lost by favoring it.

```{figure} figures/ch02-exp-log.png
:name: fig-exp-log
:alt: Left panel shows the increasing curves of 2 to the x, e to the x, and 5 to the x, all passing through the point zero comma one. Right panel shows natural log, log base 2, and log base 10, all passing through one comma zero and rising slowly.

Left: exponentials $b^x$ for $b = 2, e, 5$. All pass through $(0,1)$ since $b^0 = 1$; larger bases climb faster. Right: logarithms, their inverses, all pass through $(1, 0)$ and grow without bound but ever more slowly.
```

Exponential growth is *qualitatively* faster than polynomial growth: for any base $b>1$ and any power $n$, the ratio $b^x / x^n$ eventually grows without bound. The figure below makes the point concretely for $2^x$ versus $x^3$; the curves cross for the last time near $x \approx 9.94$, and beyond that the exponential wins by an ever-widening margin.

```{figure} figures/ch02-exp-vs-poly.png
:name: fig-exp-vs-poly
:alt: The cubic x cubed initially lies above 2 to the x, but the exponential curve overtakes it near x equals ten and then rises far more steeply.

$x^3$ versus $2^x$. The polynomial leads at first, but past their final crossing near $x \approx 9.94$ the exponential dominates permanently. This "eventually exponentials win" behavior is why algorithmic running times of $2^n$ are catastrophic while $n^3$ is merely slow.
```

## 1.2.2 Logarithms

The logarithm answers the question the exponential poses in reverse. The exponential asks: *given the exponent, what is the value?* The logarithm asks: *given the value, what was the exponent?*

```{prf:definition} Logarithm
:label: def-logarithm
For $b > 0$, $b \neq 1$, the **logarithm base $b$** is the inverse of $b^x$:

$$\log_b x = y \quad\Longleftrightarrow\quad b^y = x.$$

Its domain is $(0, \infty)$ and its range is all of $\mathbb{R}$. The **natural logarithm** is $\ln x = \log_e x$.
```

Every statement about logarithms is a statement about exponents read backwards. $\log_2 8 = 3$ *because* $2^3 = 8$; $\ln 1 = 0$ *because* $e^0 = 1$; $\log_{10} 0.01 = -2$ *because* $10^{-2} = 0.01$. The inverse relationship in function form:

$$
\ln(e^x) = x \ \text{ for all } x, \qquad e^{\ln x} = x \ \text{ for all } x > 0.
$$

The exponent laws translate into the **logarithm laws**. For $x, y > 0$ and any real $r$:

$$
\ln(xy) = \ln x + \ln y, \qquad
\ln\!\frac{x}{y} = \ln x - \ln y, \qquad
\ln(x^r) = r \ln x,
$$

and any base converts to any other by the **change of base formula** $\log_b x = \dfrac{\ln x}{\ln b}$. Each law is an exponent law read through the inverse: for instance, $b^{s}b^{t} = b^{s+t}$ says "multiplying values adds exponents," and since logarithms *are* the exponents, $\log_b(xy) = \log_b x + \log_b y$. Deriving one law this way yourself (Exercise 14) converts the list from memorized to inevitable.

Logarithms turn multiplication into addition and powers into multiplication — historically the reason they were invented, and currently the reason they pervade data science: they compress huge dynamic ranges (log-scale plots), stabilize products of many small probabilities (log-likelihoods), and linearize power laws. They are also how humans already measure many things without noticing: pH ($-\log_{10}$ of hydrogen ion concentration), decibels, and earthquake magnitudes are logarithmic scales, which is why "pH 2 versus pH 5" means *a thousand times* more acidic — three steps of $\log_{10}$ is a factor of $10^3$.

```{prf:example} Solving exponential equations
:label: ex-solve-exponential
Solve $5 \cdot 3^{2t} = 40$ for $t$.

Isolate the exponential, then take a logarithm of both sides:

$$
3^{2t} = 8 \;\Longrightarrow\; \ln\bigl(3^{2t}\bigr) = \ln 8 \;\Longrightarrow\; 2t \ln 3 = \ln 8 \;\Longrightarrow\; t = \frac{\ln 8}{2 \ln 3}.
$$

Numerically $t = \frac{2.0794}{2(1.0986)} \approx 0.9464$. Check: $3^{2(0.9464)} = 3^{1.8928} \approx 8.0$. ✓

The three-step pattern — *isolate, take logs, pull the exponent down with the power law* — solves every equation with the unknown in an exponent, and it is worth rehearsing until automatic.
```

```{prf:example} Doubling time
:label: ex-doubling
A dataset grows by 15% per month, so its size after $t$ months is $S(t) = S_0 (1.15)^t$. How long until it doubles?

We need $(1.15)^t = 2$:

$$
t \ln 1.15 = \ln 2 \;\Longrightarrow\; t = \frac{\ln 2}{\ln 1.15} = \frac{0.6931}{0.1398} \approx 4.96 \text{ months}.
$$

**Interpretation.** About five months per doubling — so in a year (about 2.4 doublings) storage needs grow by a factor of $(1.15)^{12} \approx 5.35$. Percent-per-period growth compounds much faster than intuition suggests, which is exactly why one computes rather than guesses. (A back-of-envelope shortcut falls out of the same formula: since $\ln 2 \approx 0.69$ and $\ln(1 + r) \approx r$ for small rates, doubling time $\approx 0.69/r$ — the financier's "rule of 70": about $70/(\text{percent rate})$ periods per doubling. Here $70/15 \approx 4.7$, close to the exact $4.96$.)
```

```{prf:example} Extracting a power law from logs
:label: ex-power-law
Measurements suggest a relationship $y = C x^p$. Taking logarithms of both sides,

$$
\ln y = \ln C + p \ln x,
$$

which is a *linear* equation in the variables $(\ln x, \ln y)$ with slope $p$ and intercept $\ln C$. If two measured points are $(x, y) = (2, 12)$ and $(8, 96)$, then

$$
p = \frac{\ln 96 - \ln 12}{\ln 8 - \ln 2} = \frac{\ln(96/12)}{\ln(8/2)} = \frac{\ln 8}{\ln 4} = \frac{3\ln 2}{2 \ln 2} = \frac{3}{2},
$$

and $C = y/x^p = 12/2^{3/2} = 12/(2\sqrt 2) = 3\sqrt{2} \approx 4.243$. This log-log linearization is a standard first move in exploratory data analysis.
```

## 1.2.3 Trigonometric functions

Calculus measures angles in **radians**: the radian measure of an angle is the length of the arc it cuts from a circle of radius 1. A full revolution is the full circumference, $2\pi$; a straight angle is $\pi$; a right angle is $\pi/2$. Degrees convert by $180° = \pi$ radians. Radians are not a stylistic preference — the clean derivative formulas of Section 2.3 ($\sin' = \cos$) are *only true in radians*.

Because a radian is *defined* by arc length, two geometric formulas come for free, both scaling linearly from the unit circle to a circle of radius $r$: an angle $\theta$ (in radians) subtends an arc of length

$$
s = r\theta,
$$

and sweeps out a pie-slice (**sector**) of area

$$
A = \tfrac12 r^2\theta
$$

(the fraction $\theta/2\pi$ of the full disk's $\pi r^2$). Neither formula survives in degrees without ugly conversion factors — a first concrete payoff of the radian convention, and formulas Section 6.5 will rebuild into polar-coordinate integration.

```{prf:example} Arc length and sector area
:label: ex-arc-sector
A wiper blade of length $r = 6$ (decimeters) sweeps through an angle of $120° $. How far does its tip travel, and how much area does it wipe?

First convert: $120° = \tfrac{2\pi}{3}$ radians. Then

$$
s = r\theta = 6\cdot\frac{2\pi}{3} = 4\pi \approx 12.57 \text{ dm},
\qquad
A = \frac12 r^2\theta = \frac12 (36)\frac{2\pi}{3} = 12\pi \approx 37.70 \text{ dm}^2.
$$

**Check:** $120°$ is a third of a revolution, so the arc should be a third of the circumference $2\pi r = 12\pi$ ✓, and the area a third of the disk $\pi r^2 = 36\pi$ ✓. Converting to radians *first*, then using the clean formulas, is the reliable order of operations.
```

```{prf:definition} Sine and cosine
:label: def-sin-cos
Place an angle $\theta$ at the origin, measured counterclockwise from the positive $x$-axis, and let it intersect the unit circle at a point $P$. Then

$$\cos\theta = \text{the $x$-coordinate of } P, \qquad \sin\theta = \text{the $y$-coordinate of } P.$$

Both functions are defined for all real $\theta$, take values in $[-1, 1]$, and are **periodic with period $2\pi$**: $\sin(\theta + 2\pi) = \sin\theta$ and likewise for cosine.
```

```{figure} figures/ch02-unit-circle.png
:name: fig-unit-circle
:alt: Left: a unit circle with an angle theta marked, the horizontal leg labeled cosine theta and vertical leg labeled sine theta, meeting the circle at a highlighted point. Right: the sine and cosine waves over two full periods, visibly identical curves offset by a quarter period.

Left: the unit-circle definition — $\cos\theta$ and $\sin\theta$ are coordinates of a point on the circle. Right: as $\theta$ advances, those coordinates trace the familiar waves. Cosine is sine shifted left by $\pi/2$, which the graphs make visible.
```

The unit-circle definition explains the waves' features at a glance: the values stay in $[-1, 1]$ because coordinates on a unit circle cannot exceed $1$ in size; the functions repeat every $2\pi$ because a full lap returns to the same point; sine is *odd* and cosine is *even* (in Section 1.1's sense — reflecting $\theta \to -\theta$ flips the point across the $x$-axis, negating $y$ but preserving $x$); and the two waves are the same shape a quarter-turn apart, since rotating the circle by $\pi/2$ trades one coordinate for the other.

Because the point $(\cos\theta, \sin\theta)$ lies on the unit circle $x^2 + y^2 = 1$, we get for free the single most important identity in trigonometry:

$$
\sin^2\theta + \cos^2\theta = 1.
$$

The remaining four trigonometric functions are ratios of these two:

$$
\tan\theta = \frac{\sin\theta}{\cos\theta}, \qquad
\cot\theta = \frac{\cos\theta}{\sin\theta}, \qquad
\sec\theta = \frac{1}{\cos\theta}, \qquad
\csc\theta = \frac{1}{\sin\theta},
$$

each undefined where its denominator vanishes ($\tan$ and $\sec$ at odd multiples of $\pi/2$, for example). Dividing the Pythagorean identity by $\cos^2\theta$ gives its second form, needed for trigonometric substitution in Section 3.4:

$$
\tan^2\theta + 1 = \sec^2\theta.
$$

The values you should be able to produce without a calculator:

| $\theta$ | $0$ | $\pi/6$ | $\pi/4$ | $\pi/3$ | $\pi/2$ | $\pi$ |
|---|---|---|---|---|---|---|
| $\sin\theta$ | $0$ | $1/2$ | $\sqrt{2}/2$ | $\sqrt{3}/2$ | $1$ | $0$ |
| $\cos\theta$ | $1$ | $\sqrt{3}/2$ | $\sqrt{2}/2$ | $1/2$ | $0$ | $-1$ |
| $\tan\theta$ | $0$ | $1/\sqrt{3}$ | $1$ | $\sqrt{3}$ | undef. | $0$ |

Two identity families will be used later and are worth recording now. The **angle-sum identities**

$$
\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta, \qquad
\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta,
$$

and, setting $\alpha = \beta = \theta$, the **double-angle identities**

$$
\sin 2\theta = 2\sin\theta\cos\theta, \qquad
\cos 2\theta = \cos^2\theta - \sin^2\theta = 1 - 2\sin^2\theta = 2\cos^2\theta - 1.
$$

Rearranged, the last two give the **half-angle (power-reduction) forms** $\sin^2\theta = \tfrac{1 - \cos 2\theta}{2}$ and $\cos^2\theta = \tfrac{1 + \cos 2\theta}{2}$, indispensable when we integrate squared trig functions in Section 3.4.

```{prf:example} Exact evaluation without a calculator
:label: ex-trig-exact
Compute $\sin\!\frac{5\pi}{6}$ and $\cos\!\frac{5\pi}{6}$.

The angle $5\pi/6$ lies in the second quadrant, $\pi/6$ short of $\pi$. Its **reference angle** is $\pi/6$. In the second quadrant, sine is positive ($y > 0$) and cosine negative ($x < 0$), so

$$
\sin\frac{5\pi}{6} = +\sin\frac{\pi}{6} = \frac{1}{2}, \qquad
\cos\frac{5\pi}{6} = -\cos\frac{\pi}{6} = -\frac{\sqrt{3}}{2}.
$$

Check with the Pythagorean identity: $\left(\tfrac12\right)^2 + \left(\tfrac{\sqrt3}{2}\right)^2 = \tfrac14 + \tfrac34 = 1.$ ✓
```

```{prf:example} Solving a trigonometric equation
:label: ex-trig-equation
Find all solutions of $2\cos\theta = 1$ in $[0, 2\pi)$.

Rewrite as $\cos\theta = \tfrac12$ and consult the unit circle: cosine is the $x$-coordinate, and $x = \tfrac12$ happens at *two* points on the circle — one in the first quadrant, one in the fourth. The first-quadrant angle is the table value $\theta = \tfrac\pi3$; its fourth-quadrant mirror is $\theta = 2\pi - \tfrac\pi3 = \tfrac{5\pi}{3}$.

$$
\theta = \frac{\pi}{3} \quad\text{or}\quad \theta = \frac{5\pi}{3}.
$$

Two lessons generalize. First, trig equations usually have *multiple* solutions per period — a horizontal line typically cuts a wave twice per cycle — so "find the angle" really means "find all angles," located by quadrant reasoning from one reference solution. Second, outside a restricted window like $[0, 2\pi)$, every solution recurs with period $2\pi$: the complete solution set is $\theta = \pm\tfrac\pi3 + 2\pi k$ for integers $k$.
```

### Sinusoids: amplitude, period, and phase

Data that cycles — hourly temperatures, daily website traffic, seasonal sales — is modeled by *transformed* sine waves, and Section 1.1's transformation rules read the parameters off the formula:

$$
y = A\sin\bigl(\omega t - \varphi\bigr)
\quad\text{has}\quad
\textbf{amplitude } |A|, \qquad
\textbf{period } \frac{2\pi}{\omega}, \qquad
\textbf{phase shift } \frac{\varphi}{\omega} \text{ (rightward)}.
$$

The amplitude is a vertical stretch (the wave swings between $-|A|$ and $|A|$); the factor $\omega$ is a horizontal compression (the wave completes $\omega$ cycles in every $2\pi$ of $t$, so each cycle takes $2\pi/\omega$); and the phase shift is Section 1.1's horizontal shift, extracted by factoring: $\sin(\omega t - \varphi) = \sin\bigl(\omega(t - \varphi/\omega)\bigr)$.

```{prf:example} Reading a sinusoid's anatomy
:label: ex-sinusoid-anatomy
Describe the graph of $y = 3\sin\!\bigl(2t - \tfrac{\pi}{2}\bigr)$, and find the first time $t > 0$ at which it reaches its maximum.

Amplitude $3$: the wave oscillates between $-3$ and $3$. Angular frequency $\omega = 2$: the period is $2\pi/2 = \pi$, twice as fast as plain sine. Phase: factoring, $y = 3\sin\bigl(2(t - \tfrac\pi4)\bigr)$ — the compressed wave shifted right by $\tfrac\pi4$.

The maximum of $\sin(\cdot)$ occurs when its argument is $\tfrac\pi2$: solve $2t - \tfrac\pi2 = \tfrac\pi2$ to get $t = \tfrac\pi2$, where indeed $y = 3\sin\tfrac\pi2 = 3$. **Check** the story: the shifted wave starts a cycle at $t = \tfrac\pi4$ and, with period $\pi$, peaks a quarter-period later at $\tfrac\pi4 + \tfrac\pi4 = \tfrac\pi2$ ✓. This parameter-reading skill returns in force in Section 4.3, where Fourier series build *every* periodic signal out of exactly such ingredients.
```

Finally, the restricted-domain inverses. $\arcsin x$ (also written $\sin^{-1}x$) is the angle in $[-\pi/2, \pi/2]$ whose sine is $x$; $\arccos x$ the angle in $[0, \pi]$ whose cosine is $x$; $\arctan x$ the angle in $(-\pi/2, \pi/2)$ whose tangent is $x$. The restrictions exist for Section 1.1's reason: the waves fail the horizontal line test badly (every value is hit infinitely often), so invertibility must be *restored* by cutting the domain down to one increasing (or decreasing) stretch. Thus $\arcsin\frac12 = \pi/6$, and $\arctan 1 = \pi/4$. These reappear as antiderivatives in Chapter 3.

## 1.2.4 Now do it in Python

The code verifies our hand results from this section — the compounding comparison, the decay fraction, the doubling time, the exact trig values, and an identity — and demonstrates the log-scale plotting that makes exponential data legible.

```python
import numpy as np

# --- Verify Example 1.2.2: compounding $1000 at 5% for 10 years ---
print(1000 * 1.05**10)                    # annual:     1628.89...
print(1000 * (1 + 0.05/12)**120)          # monthly:    1647.00...
print(1000 * np.exp(0.5))                 # continuous: 1648.72...
# and watch (1 + 1/n)^n approach e:
for n in [1, 10, 100, 10**6]:
    print(n, (1 + 1/n)**n)                # -> 2, 2.5937, 2.7048, 2.71828
print(np.e)                               # 2.718281828...

# --- Verify Example 1.2.1: caffeine after 12 h, half-life 5 h ---
print(100 * 0.5**(12/5))                  # expect about 18.9 mg

# --- Verify Example 1.2.4: doubling time at 15% growth ---
t_double = np.log(2) / np.log(1.15)
print(t_double)                 # expect about 4.96
print(1.15**t_double)           # expect 2.0 (definition of doubling time)

# --- Verify Example 1.2.6: arc length and sector, r = 6, theta = 2*pi/3 ---
r, theta = 6.0, 2*np.pi/3
print(r*theta, 4*np.pi)                    # both 12.566...
print(0.5*r**2*theta, 12*np.pi)            # both 37.699...

# --- Verify Example 1.2.7: exact values at 5*pi/6 ---
theta = 5*np.pi/6
print(np.sin(theta), 1/2)                  # both 0.5
print(np.cos(theta), -np.sqrt(3)/2)        # both -0.8660...

# --- Verify Example 1.2.8: the two solutions of 2 cos(theta) = 1 ---
print(np.cos(np.pi/3), np.cos(5*np.pi/3))  # both 0.5

# --- Spot-check an identity at random angles ---
rng = np.random.default_rng(0)
th = rng.uniform(-10, 10, size=5)
print(np.sin(th)**2 + np.cos(th)**2)       # expect five 1.0's
```

SymPy works with these functions *exactly*, returning symbolic values rather than decimals — often the more useful check:

```python
import sympy as sp

print(sp.sin(sp.Rational(5, 6) * sp.pi))    # expect 1/2, exactly
print(sp.solve(sp.Eq(5 * 3**(2*sp.Symbol('t')) - 40, 0)))  # ln(8)/(2 ln 3) form
print(sp.simplify(sp.cos(2*sp.Symbol('x'))
                  - (1 - 2*sp.sin(sp.Symbol('x'))**2)))    # expect 0
```

**Visualization: the power of log scales.** Exponential data plotted on ordinary axes hides everything but its final surge; on a logarithmic vertical axis, exponentials become straight lines whose slopes reveal their growth rates.

```python
import matplotlib.pyplot as plt

x = np.linspace(0, 30, 200)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
for b in (1.1, 1.3, 1.6):
    axes[0].plot(x, b**x, label=f"${b}^x$")
    axes[1].semilogy(x, b**x, label=f"${b}^x$")   # log-scale y-axis
axes[0].set_title("Linear axes: only the fastest curve is visible")
axes[1].set_title("Log axes: each exponential is a straight line")
for ax in axes:
    ax.set_xlabel("x"); ax.legend()
plt.tight_layout(); plt.show()
```

**Interpretation.** On the left, $1.1^x$ and $1.3^x$ look flat next to $1.6^x$ — the picture misleads. On the right, all three are straight lines with slopes proportional to $\ln b$, and their behavior over the whole range is comparable at a glance. Whenever data spans several orders of magnitude, reach for a log scale. A companion experiment worth running: plot the sinusoid of {prf:ref}`ex-sinusoid-anatomy` on $[0, 2\pi]$ alongside plain $\sin t$, and confirm by eye all three parameters you read off algebraically — the tripled height, the doubled speed, the quarter-turn delay.

```{admonition} Common Mistakes
:class: warning
**Degrees in code.** `np.sin(30)` computes the sine of 30 *radians* (about $-0.988$), not of $30°$. Convert first: `np.sin(np.deg2rad(30))` gives $0.5$. Everything in this book is radians — including the arc-length and sector formulas $s = r\theta$ and $A = \frac12 r^2\theta$, which are simply false in degrees.

**$\ln(x + y) \neq \ln x + \ln y$.** The log of a *product* splits; the log of a sum does not simplify at all. Similarly $\ln(x)/\ln(y)$ is not $\ln(x/y)$ — the former is $\log_y x$ by change of base.

**Solving $b^x = c$ by dividing.** From $3^{2t} = 8$, one cannot "divide by 3"; the unknown is in the *exponent*, and only a logarithm brings it down. Isolate, take logs, apply the power law.

**One solution where there are two.** $\cos\theta = \frac12$ has two solutions per period ({prf:ref}`ex-trig-equation`); reporting only the reference angle silently discards half the answer.

**$\sin^{-1}x$ versus $(\sin x)^{-1}$.** By convention $\sin^{-1}$ means arcsine, while $\sin^2 x$ means $(\sin x)^2$. The notation is inconsistent; the meaning, unfortunately, must be memorized.

**Forgetting the quadrant.** $\arcsin$ returns values only in $[-\pi/2, \pi/2]$, so $\arcsin(\sin\theta)$ equals $\theta$ only for $\theta$ in that interval: $\arcsin\bigl(\sin\frac{5\pi}{6}\bigr) = \frac{\pi}{6}$, not $\frac{5\pi}{6}$.
```

```{admonition} Data Science Connection
:class: tip
The logistic (sigmoid) function of classification, $\sigma(x) = \dfrac{1}{1 + e^{-x}}$, is built from $e^x$; the log-loss it is trained with is built from $\ln$; learning-rate *decay schedules* are the exponential-decay template of §1.2.1 applied to optimization; and periodic features (hour of day, day of year) are routinely encoded as $\sin$/$\cos$ pairs precisely because of the unit-circle definition — the pair $(\cos\theta, \sin\theta)$ places each time on a circle so that 11:59 PM sits next to 12:01 AM, as it should. When a feature spans orders of magnitude (income, city population, word counts), the first transformation a practitioner tries is $\ln$ — §1.2.2's compression of dynamic range, applied as feature engineering.
```

```{admonition} Looking Ahead
:class: seealso
Section 2.3 will prove the facts asserted here: that $e^x$ is its own derivative and that $\sin' = \cos$ (in radians). The half-angle identities power Section 3.4's integrals; $s = r\theta$ and the sector area return as Section 6.5's polar area element; the sinusoid parameters of §1.2.3 become Fourier series ingredients in Section 4.3; and the "take logs of both sides" move reappears as *log-likelihood* throughout statistical practice.
```

## 1.2.5 Exercises

### Quick Check

1. Evaluate without a calculator: $\log_2 32$, $\ln e^7$, $10^{\log_{10} 4}$, $\log_5 1$.
2. Convert $135°$ to radians and $\pi/5$ to degrees.
3. What are the domain and range of $\ln x$? Of $e^x$? How are the answers related?
4. Which is larger for very large $x$: $x^{100}$ or $1.01^x$?
5. A quantity has half-life $8$ days. What fraction remains after $24$ days?
6. What are the amplitude and period of $y = 5\sin(3t)$?

````{admonition} Answers to Quick Checks
:class: dropdown
1. $5$; $7$; $4$; $0$.
2. $135° = \frac{3\pi}{4}$; $\ \pi/5 = 36°$.
3. $\ln$: domain $(0,\infty)$, range $\mathbb{R}$. $e^x$: domain $\mathbb{R}$, range $(0,\infty)$. Each is the other with domain and range swapped, because the functions are inverses.
4. $1.01^x$ — any exponential with base $>1$ eventually exceeds any fixed power.
5. Three half-lives: $\left(\frac12\right)^3 = \frac18$.
6. Amplitude $5$; period $\frac{2\pi}{3}$.
````

### Basic Practice

7. Solve for $x$: (a) $e^{3x} = 20$;  (b) $\log_2(x - 1) = 5$;  (c) $4 \cdot 2^{x} = 3^{x}$.
8. Simplify using log laws: (a) $\ln(e^2 x^3) - 3\ln x$;  (b) $\log_{10} 50 + \log_{10} 2$;  (c) $\dfrac{\ln 27}{\ln 9}$.
9. Using reference angles, evaluate exactly: $\cos\frac{2\pi}{3}$, $\sin\frac{7\pi}{6}$, $\tan\frac{3\pi}{4}$.
10. Given $\sin\theta = \frac{3}{5}$ with $\theta$ in the second quadrant, find $\cos\theta$ and $\tan\theta$ exactly.
11. \$500 is deposited at 4% annual interest. Find the balance after 6 years under annual compounding and under continuous compounding, and the difference between them.
12. A circular pizza slice has radius $12$ cm and central angle $\frac{\pi}{4}$. Find the length of its crust (the arc) and its area.
13. Find *all* solutions in $[0, 2\pi)$: (a) $\sin\theta = -\dfrac{\sqrt3}{2}$;  (b) $\tan\theta = 1$;  (c) $2\cos\theta + \sqrt{3} = 0$.

````{admonition} Solution to Exercise 7(c)
:class: dropdown
Take natural logs of $4 \cdot 2^x = 3^x$:

$$
\ln 4 + x\ln 2 = x \ln 3
\;\Longrightarrow\;
\ln 4 = x(\ln 3 - \ln 2)
\;\Longrightarrow\;
x = \frac{\ln 4}{\ln(3/2)} \approx \frac{1.3863}{0.4055} \approx 3.419.
$$

Check: $4 \cdot 2^{3.419} \approx 4(10.70) \approx 42.8$ and $3^{3.419} \approx 42.8$. ✓
````

````{admonition} Solution to Exercise 10
:class: dropdown
From $\sin^2\theta + \cos^2\theta = 1$: $\cos^2\theta = 1 - \frac{9}{25} = \frac{16}{25}$, so $\cos\theta = \pm\frac45$. In the second quadrant cosine is negative: $\cos\theta = -\frac{4}{5}$. Then $\tan\theta = \dfrac{\sin\theta}{\cos\theta} = \dfrac{3/5}{-4/5} = -\dfrac{3}{4}$.
````

````{admonition} Solution to Exercise 13(a)
:class: dropdown
Sine is the $y$-coordinate, and $y = -\frac{\sqrt3}{2}$ occurs in the third and fourth quadrants, with reference angle $\frac\pi3$ (since $\sin\frac\pi3 = \frac{\sqrt3}{2}$). The two angles: $\theta = \pi + \frac\pi3 = \frac{4\pi}{3}$ and $\theta = 2\pi - \frac\pi3 = \frac{5\pi}{3}$.
````

### Intermediate Practice

14. Derive the product law $\log_b(xy) = \log_b x + \log_b y$ from the exponent law $b^s b^t = b^{s+t}$: set $s = \log_b x$, $t = \log_b y$, and follow the definitions.
15. A quantity decays exponentially with half-life 12 hours: $Q(t) = Q_0 \left(\tfrac12\right)^{t/12}$. How long until only 10% remains?
16. How long does money take to *triple* at 6% annual growth? Then use the rule-of-70 idea from {prf:ref}`ex-doubling` to explain why the answer is roughly (but not exactly) $\ln 3/\ln 2 \approx 1.585$ doubling times.
17. Derive the identity $\cos^2\theta = \frac{1 + \cos 2\theta}{2}$ from the double-angle formula for cosine, showing each algebraic step.
18. Solve $2\sin^2 x - \sin x - 1 = 0$ for all $x$ in $[0, 2\pi)$. *(Hint: it factors like a quadratic in $\sin x$.)*
19. Show that $\ln\bigl(x + \sqrt{x^2 - 1}\bigr) + \ln\bigl(x - \sqrt{x^2-1}\bigr) = 0$ for $x \ge 1$, and explain what this says about the two quantities inside the logarithms.
20. A city's noon temperature is modeled by $T(t) = 22 + 8\sin\!\bigl(\tfrac{2\pi}{365}(t - 100)\bigr)$ (degrees Celsius, $t$ in days). Read off the average temperature, the amplitude of the seasonal swing, the period, and the day of the year on which the maximum occurs.

````{admonition} Hint for Exercise 18
:class: dropdown
Let $s = \sin x$. Then $2s^2 - s - 1 = (2s + 1)(s - 1)$. Solve each factor, then find *all* angles in $[0, 2\pi)$ with those sine values — one factor gives one angle, the other gives two.
````

````{admonition} Solution to Exercise 16 (first part)
:class: dropdown
Tripling requires $(1.06)^t = 3$:

$$
t = \frac{\ln 3}{\ln 1.06} = \frac{1.0986}{0.05827} \approx 18.85 \text{ years}.
$$

Check: $1.06^{18.85} \approx 3.0$ ✓. For the second part, note $\frac{\ln 3}{\ln 1.06} = \frac{\ln 3}{\ln 2}\cdot\frac{\ln 2}{\ln 1.06}$ — exactly $\log_2 3 \approx 1.585$ doubling times, and each doubling takes $\approx 70/6 \approx 11.7$ years by the rule of 70, predicting $\approx 18.5$ years: close, with the small gap coming from the approximation $\ln(1.06) \approx 0.06$.
````

### Conceptual Understanding

21. Explain why $b = 1$ is excluded in the definition of the exponential function and of $\log_b$.
22. Your plot of app downloads over three years looks like a hockey stick. A colleague says "growth exploded last quarter." Using this section, give an alternative explanation and describe the single plot change that would distinguish the two hypotheses.
23. Explain geometrically, using the unit circle, why $\sin(\pi - \theta) = \sin\theta$ and $\cos(-\theta) = \cos\theta$.
24. In Section 1.1's vocabulary, sine is an odd function and cosine an even one. Explain how each symmetry follows from the unit-circle definition, and predict — before Section 4.2 confirms it — which powers of $x$ can appear in a polynomial approximation of each.

### Python Practice

25. Verify your answers to Exercises 11, 12, 15, and 16 numerically, and reproduce Exercise 15 symbolically with `sp.solve`.
26. Write a loop (or vectorized expression) that checks the angle-sum identity $\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$ at 1000 random pairs $(\alpha, \beta)$ and prints the maximum absolute discrepancy. Explain why the result is not exactly zero.
27. Compute $(1 + 1/n)^n$ for $n = 10^k$, $k = 0, 1, \ldots, 8$, and print each alongside $e$. Roughly how does the error shrink as $n$ grows tenfold? *(Section 4.2 will explain the pattern you observe.)*

### Visualization Practice

28. Plot $\tan x$ on $(-\pi/2, \pi/2)$ and on a wider window with its vertical asymptotes indicated by dashed lines. Explain the asymptotes using the definition $\tan = \sin/\cos$.
29. Generate data $y = 3x^{2.5}$ for $x$ from 1 to 100, plot it on linear axes and on log-log axes, and read the exponent $2.5$ off the log-log slope between two chosen points, as in {prf:ref}`ex-power-law`.
30. Plot the temperature model of Exercise 20 over two full years, marking the maxima; confirm the peak day you computed by hand.
31. On one set of axes, plot $\sin t$, $3\sin t$, $\sin 2t$, and $3\sin\!\bigl(2t - \tfrac\pi2\bigr)$ over $[0, 2\pi]$ with a legend, and annotate which parameter each curve changes relative to plain $\sin t$.

### Challenge

32. Without a calculator, determine which is larger: $e^\pi$ or $\pi^e$. *(Hint: compare $\frac{\ln x}{x}$ at $x = e$ and $x = \pi$; you may use the fact, provable in Section 2.4, that $\frac{\ln x}{x}$ is decreasing for $x > e$.)*
33. The **hyperbolic functions** are $\cosh x = \frac{e^x + e^{-x}}{2}$ and $\sinh x = \frac{e^x - e^{-x}}{2}$ — precisely the even and odd parts of $e^x$ from Section 1.1's Exercise 33. Prove that $\cosh^2 x - \sinh^2 x = 1$ and explain in one sentence the analogy and the difference with $\sin^2 + \cos^2 = 1$.
34. Prove that $\log_2 3$ is irrational. *(Suppose $\log_2 3 = p/q$ with positive integers $p, q$; convert to $2^p = 3^q$ and find the contradiction in even versus odd.)*

## 1.2.6 Summary

Exponentials $b^x$ multiply by a fixed factor per unit step — growth for $b > 1$, decay for $b < 1$, with half-life and doubling-time templates making both computable by counting — share the point $(0,1)$, and eventually outgrow every polynomial; the special base $e \approx 2.71828$, the limit of $(1 + 1/n)^n$ and the yield of continuous compounding, is the calculus-native choice. Logarithms invert exponentials, turning products into sums and powers into multiples (each law an exponent law read backwards); $\ln$ and $e^x$ undo each other; the isolate–log–power-law pattern solves every exponent-unknown equation; and log scales — from pH to `semilogy` plots — make multiplicative data readable and power laws linear. Trigonometric functions come from coordinates on the unit circle, giving $[-1,1]$ range, $2\pi$-periodicity, sine's oddness and cosine's evenness, the free formulas $s = r\theta$ and $A = \frac12 r^2\theta$, and the identity $\sin^2 + \cos^2 = 1$ with its angle-sum, double-angle, and power-reduction descendants; trig equations have multiple solutions per period, found by quadrant reasoning from reference angles; and the sinusoid $A\sin(\omega t - \varphi)$ encodes amplitude, period $2\pi/\omega$, and phase — the reading skill behind seasonal models and Fourier series. Radians are mandatory. Python verifies all of this numerically (NumPy) and exactly (SymPy), and `semilogy`/log-log plots are the standard tools for exponential and power-law data.

*Parallel reading:* OpenStax *Calculus Volume 1*, Sections 1.3–1.5 {cite}`openstax_calc1`.
