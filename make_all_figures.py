"""Regenerate every figure in the book.

Run from the repository root:  python make_all_figures.py
Each fig_partN.py script writes PNGs into book/partN/figures/ and prints
the verification numbers quoted in the corresponding chapters' prose.
"""

import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent / "figures" / "scripts"

def main() -> int:
    scripts = sorted(SCRIPTS_DIR.glob("fig_part*.py"))
    if not scripts:
        print("No figure scripts found in", SCRIPTS_DIR)
        return 1
    for script in scripts:
        print(f"=== {script.name} ===")
        result = subprocess.run([sys.executable, script.name],
                                cwd=SCRIPTS_DIR)
        if result.returncode != 0:
            print(f"FAILED: {script.name}")
            return result.returncode
    print("All figures regenerated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

# --- ch26 (Section 2.5): absolute extrema on a closed interval ---
def fig_ch26_extrema():
    f = lambda x: x**3 - 3*x**2 + 1
    xs = np.linspace(-1, 4, 400)
    fig, ax = plt.subplots(figsize=(7.2, 4.4), dpi=150)
    ax.plot(xs, f(xs), color='tab:blue', lw=2.2, label=r'$f(x)=x^3-3x^2+1$')
    for cx, kind in {-1: 'endpoint', 0: 'critical', 2: 'critical', 4: 'endpoint'}.items():
        ax.plot(cx, f(cx), 'o', ms=8,
                color='tab:red' if kind == 'critical' else 'tab:orange', zorder=5)
    ax.annotate('local max, $f(0)=1$', (0, 1), xytext=(0.35, 5.5),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
    ax.annotate('absolute min (tie), $f(-1)=f(2)=-3$', (2, -3), xytext=(0.9, -8.5),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
    ax.annotate('', (-1, -3), xytext=(0.95, -8.0),
                arrowprops=dict(arrowstyle='->', color='gray'))
    ax.annotate('absolute max, $f(4)=17$', (4, 17), xytext=(2.1, 14.5),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
    ax.axhline(0, color='k', lw=0.6)
    ax.set_xlabel('$x$'); ax.set_ylabel('$f(x)$')
    ax.set_title('Absolute extrema on $[-1,4]$: compare critical points and endpoints')
    ax.grid(alpha=0.25); ax.legend(loc='upper left', fontsize=9)
    plt.tight_layout()
    plt.savefig('book/part1/figures/ch26-extrema.png')
    plt.close(fig)

fig_ch26_extrema()
