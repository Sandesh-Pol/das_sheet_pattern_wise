# Contest Patterns & Algorithms — Documentation

---

## Table of Contents
1. [GCD Pair Strength — Pairwise Maximization](#1-gcd-pair-strength--pairwise-maximization)
2. [Subarray Enumeration — Even/Odd Ratio](#2-subarray-enumeration--evenodd-ratio)
3. [Pointer Simulation — Unfinished Tasks](#3-pointer-simulation--unfinished-tasks)

---

## 1. GCD Pair Strength — Pairwise Maximization

**File:** `z01contest/leetcode_4010_max_stringth_gcd.py`
**LeetCode:** 4010. Maximize Pair Strength Using GCD

**Pattern:** Brute Force Pair Enumeration + GCD (Euclidean)  
**When to use:** Given an array, maximize a numeric "strength" over all pairs `(i, j)`, `i < j`.

**Algorithm:**
- `strength(i, j) = (nums[i] * nums[j]) // (gc * gc)` where `gc = gcd(nums[i], nums[j])`.
- Since `gc²` divides `nums[i] * nums[j]`, integer division is exact — this equals the product of the two numbers after removing their common factors.
- For each pair `(i, j)`, compute `gc` via the Euclidean algorithm and update `ans = max(ans, strength)`.
- Return `ans`.

**Code:**
```python
def max_stringth(nums):

    def gcd(a,b):
        while b:
            a,b = b,a%b
        return a
    n = len(nums)
    ans = 0

    for i in range(n):
        for j in range(i+1,n):
            gc = gcd(nums[i],nums[j])

            ans = max(ans,(nums[i] * nums[j]//(gc*gc)))

    return ans
```

**Time:** O(n² · log M) where M = max value | **Space:** O(1)

---

## 2. Subarray Enumeration — Even/Odd Ratio

**File:** `z01contest/leetcode_4011_count_subarrays_with_even_odd_ratio.py`
**LeetCode:** 4011. (Weekly Contest)

**Pattern:** Fixed Start + Expanding End (Sliding Window / Subarray Count)  
**When to use:** Count subarrays satisfying a ratio condition between counts of two categories (e.g. even vs odd).

**Algorithm:**
- For each start `i`, expand end `j` from `i` to `n - 1`:
  - Track `even` and `odd` counts incrementally.
  - The subarray is valid when `odd > 0` and `even * b <= odd * a` (i.e. `even / odd <= a / b`).
  - If valid, increment `ans`.
- Return `ans`.

**Code:**
```python
def countValidSubarrays(nums, a, b):
    n = len(nums)
    ans = 0

    for i in range(n):
        even = 0
        odd = 0

        for j in range(i, n):

            if nums[j] % 2 == 0:
                even += 1
            else:
                odd += 1

            if odd > 0 and even * b <= odd * a:
                ans += 1

    return ans
```

**Time:** O(n²) | **Space:** O(1)

---

## 3. Pointer Simulation — Unfinished Tasks

**File:** `z01contest/leetcode_4012_count_of_unfinished_tasks_after_each_shift.py`
**LeetCode:** 4012. (Weekly Contest)

**Pattern:** Greedy Pointer Consumption with Cyclic Reset  
**When to use:** Simulate time budgets consuming tasks in order, reporting the remaining count after each shift.

**Algorithm:**
- `cur` points to the next task to work on; `remain` holds remaining work per task.
- For each shift with `time` budget:
  - While time remains and tasks are left, consume the current task:
    - If `time >= remain[cur]` → finish the task, subtract, advance `cur`.
    - Else → partially work the task and exhaust the budget.
  - Append `len(tasks) - cur` (unfinished task count).
  - If all tasks finished, reset `remain` and `cur` for the next cycle.

**Code:**
```python
def unfinishedTasks(tasks, shifts):

    remain = tasks[:]
    cur = 0

    ans = []

    for time in shifts:

        while cur < len(tasks) and time > 0:

            if time >= remain[cur]:

                time -= remain[cur]
                remain[cur] = 0
                cur += 1

            else:

                remain[cur] -= time
                time = 0

        ans.append(len(tasks) - cur)

        if cur == len(tasks):
            remain = tasks[:]
            cur = 0

    return ans
```

**Time:** O(S + T) amortized (S shifts, T tasks) | **Space:** O(T) (copy of tasks)

---

## Pattern Cheat Sheet

| # | Pattern | Use Case |
|---|---------|----------|
| 1 | Pair Enumeration + GCD | Maximize strength over pairs |
| 2 | Fixed Start + Expanding End | Count subarrays by ratio condition |
| 3 | Greedy Pointer Consumption | Simulate sequential time budgets |
