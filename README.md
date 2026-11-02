# ACS Assignment: Minimum Digit Product ≥ Digit Sum

## Problem

Given an integer **K**, find a valid **K-digit** integer such that:

1. the **product** of its digits is **greater than or equal to** the **sum** of its digits, and
2. the product of its digits is as **small as possible**.

If more than one integer qualifies, return the **smallest** one.

A valid integer has no leading zeros: `234` and `123` are valid 3-digit integers, `012` is not.
For an integer `a1 a2 … ak`, sum = `a1 + a2 + … + ak` and product = `a1 × a2 × … × ak`.

**Constraints:** `1 ≤ K ≤ 100000`

### Examples

| K | Output | Why |
|---|---|---|
| 2 | `22` | product 2×2 = 4 ≥ sum 2+2 = 4, and no smaller 2-digit number qualifies |
| 3 | `123` | product 1×2×3 = 6 ≥ sum 1+2+3 = 6, and no smaller 3-digit number qualifies |

## Solutions

| File | Approach | Practical for |
|---|---|---|
| [`task_solution.py`](task_solution.py) | Brute force: try every K-digit number from `11…1` upward and return the first that qualifies. | Small K only (time grows as 10^K) |
| [`task_solution_fast.cpp`](task_solution_fast.cpp) | Greedy: only a handful of digits (at most 6) need to be greater than 1. Start with those set to 9 and the rest to 1, lower each 9 to the smallest digit that keeps product ≥ sum, then sort the digits ascending. | All K up to 100000 |

## Running

```bash
# Python (brute force)
echo 3 | python3 task_solution.py          # → 123

# C++ (fast)
g++ -O2 -o solution task_solution_fast.cpp
echo 3 | ./solution                         # → 123
```

> The C++ file includes `<bits/stdc++.h>`, which only GCC provides. On macOS, compile with Homebrew GCC (`g++-14`), or replace that line with `<iostream>`, `<string>`, `<cmath>` and `<algorithm>`.
