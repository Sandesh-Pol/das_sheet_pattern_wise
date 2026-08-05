# DSA Patterns & Algorithms — Documentation

---

## Table of Contents
1. [Greedy Variable Tracking](#1-greedy-variable-tracking)
2. [Check Sorted Array](#2-check-sorted-array)
3. [Two Pointer — Remove Duplicates](#3-two-pointer--remove-duplicates)
4. [Array Rotation — Reversal Algorithm](#4-array-rotation--reversal-algorithm)
5. [Two Pointer — Move Zeroes](#5-two-pointer--move-zeroes)
6. [Hash Map & Two Pointer — Two Sum](#6-hash-map--two-pointer--two-sum)
7. [Boyer-Moore Voting — Majority Element](#7-boyer-moore-voting--majority-element)
8. [Kadane's Algorithm — Max Subarray](#8-kadanes-algorithm--max-subarray)
9. [Greedy Min Tracking — Stock Buy & Sell](#9-greedy-min-tracking--stock-buy--sell)
10. [Two Pointer — Alternate Positives & Negatives](#10-two-pointer--alternate-positives--negatives)
11. [Singly Linked List — CRUD](#11-singly-linked-list--crud)
12. [Doubly Linked List — CRUD](#12-doubly-linked-list--crud)
13. [Binary Search — Median of Two Sorted Arrays](#13-binary-search--median-of-two-sorted-arrays)
14. [Binary Search — Search a 2D Matrix](#14-binary-search--search-a-2d-matrix)
15. [Merge Intervals](#15-merge-intervals)
16. [Matrix — Set Matrix Zeroes](#16-matrix--set-matrix-zeroes)
17. [Matrix — Spiral Matrix](#17-matrix--spiral-matrix)
18. [Prefix & Suffix Product — Product of Array Except Self](#18-prefix--suffix-product--product-of-array-except-self)
19. [Sorting — Bubble Sort](#19-sorting--bubble-sort)
20. [Sorting — Selection Sort](#20-sorting--selection-sort)
21. [Sorting — Insertion Sort](#21-sorting--insertion-sort)
22. [Sorting — Merge Sort](#22-sorting--merge-sort)
23. [Binary Search — Classic Search](#23-binary-search--classic-search)
24. [Binary Search — Lower Bound / Insert Position](#24-binary-search--lower-bound--insert-position)
25. [Binary Search — First & Last Position](#25-binary-search--first--last-position)
26. [Binary Search — Search in Rotated Sorted Array](#26-binary-search--search-in-rotated-sorted-array)
27. [Binary Search — Minimum in Rotated Sorted Array](#27-binary-search--minimum-in-rotated-sorted-array)
28. [Binary Search — Find Peak Element](#28-binary-search--find-peak-element)

---

## 1. Greedy Variable Tracking

**File:** `01array/01_largest_and_second_largest_no.py`
**LeetCode:** — (similar: 215. Kth Largest Element in an Array)

**Pattern:** Greedy Variable Tracking  
**When to use:** Find top-k elements in a single pass without sorting.

**Algorithm:**
- Initialize `first` and `second` as `-inf`.
- For each `num`:
  - If `num > first`: shift `first` to `second`, set `first = num`.
  - Else if `first > num > second`: set `second = num`.
- Return `(first, second)`.

**Code:**
```python
def largest_(nums):
    first = float('-inf')
    second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return first, second
```

**Time:** O(n) | **Space:** O(1)

---

## 2. Check Sorted Array

**File:** `01array/02_check_sorted_array.py`
**LeetCode:** 1752. Check if Array Is Sorted and Rotated

**Pattern:** Single Pass Flags  
**When to use:** Verify if array is sorted in either ascending or descending order.

**Algorithm:**
- Maintain two flags: `ascending = True`, `descending = True`.
- Iterate adjacent pairs:
  - If `nums[i] > nums[i+1]` → not ascending.
  - If `nums[i] < nums[i+1]` → not descending.
- Return `ascending or descending`.

**Code:**
```python
def chceck_assinding_decending(nums):
    ascending = True
    descending = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            ascending = False
        if nums[i] < nums[i+1]:
            descending = False
    return ascending or descending
```

**Time:** O(n) | **Space:** O(1)

---

## 3. Two Pointer — Remove Duplicates

**File:** `01array/03_remove_dublicate.py`
**LeetCode:** 26. Remove Duplicates from Sorted Array

**Pattern:** Two Pointer (slow/fast)  
**When to use:** In-place deduplication of a sorted array.

**Algorithm:**
- `i` = slow pointer (last unique position).
- `j` = fast pointer (scanner).
- When `nums[j] != nums[i]`, advance `i` and copy `nums[j]` to `nums[i]`.
- Return `i+1` (new length).

**Code:**
```python
def remove_duplicate(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
```

**Time:** O(n) | **Space:** O(1)

---

## 4. Array Rotation — Reversal Algorithm

**File:** `01array/04_rotate_array.py`
**LeetCode:** 189. Rotate Array

**Pattern:** Reversal Algorithm (In-place)  
**When to use:** Rotate array by `k` positions without extra space.

**Algorithm:**
- `k %= n` (handle k > n).
- **With space:** Place each element at `(i + k) % n` in a temp array.
- **Without space (reversal):**
  1. Reverse entire array.
  2. Reverse first `k` elements.
  3. Reverse remaining `n-k` elements.

**Code:**
```python
def rotate_array_no_extra_space(nums, k):
    n = len(nums)
    k %= n

    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums
```

**Time:** O(n) | **Space:** O(1) reversal / O(n) with temp

---

## 5. Two Pointer — Move Zeroes

**File:** `01array/05_move_zero_to_end.py`
**LeetCode:** 283. Move Zeroes

**Pattern:** Two Pointer (partitioning)  
**When to use:** Move all zeroes to end while maintaining relative order (stable partition).

**Algorithm:**
- `i` = position to place next non-zero.
- For each `j`, if `nums[j] != 0`, swap `nums[i]` with `nums[j]`, increment `i`.

**Code:**
```python
def move_zero_to_end(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums
```

**Time:** O(n) | **Space:** O(1)

---

## 6. Hash Map & Two Pointer — Two Sum

**File:** `01array/06_two_sum.py`
**LeetCode:** 1. Two Sum

**Pattern:** Hash Map (complement lookup) / Two Pointer (sorted)  
**When to use:** Find pair that sums to target.

### Approach 1 — Hash Map (unsorted, returns indices)
```python
def two_sum_using_map(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]] = i
    return []
```

### Approach 2 — Two Pointer (sorted, returns values)
```python
def two_sum_using_binary(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [nums[l], nums[r]]
        elif s < target:
            l += 1
        else:
            r -= 1
    return []
```

**Time:** O(n) map / O(n log n) two-pointer | **Space:** O(n) map / O(1) two-pointer

---

## 7. Boyer-Moore Voting — Majority Element

**File:** `01array/07_mejority_element.py`
**LeetCode:** 169. Majority Element

**Pattern:** Boyer-Moore Voting Algorithm  
**When to use:** Find element appearing more than ⌊n/2⌋ times in O(n) time and O(1) space.

**Algorithm:**
- `candidate = None`, `count = 0`.
- For each `num`:
  - If `count == 0`, set `candidate = num`.
  - If `num == candidate`, `count++` else `count--`.
- Return `candidate`.

**Code:**
```python
def majority_element_candidate(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
```

**Time:** O(n) | **Space:** O(1)

---

## 8. Kadane's Algorithm — Max Subarray

**File:** `01array/08_kadane's_algrothem_max_sub_array.py`
**LeetCode:** 53. Maximum Subarray

**Pattern:** Kadane's Algorithm (Dynamic Programming)  
**When to use:** Maximum sum contiguous subarray.

**Algorithm:**
- Maintain `current` (max ending here) and `max_sum` (global max).
- **Reset variant:** Add num to `current`. If `current < 0`, reset to 0.
- **DP variant:** `current = max(num, current + num)`.

**Code:**
```python
# Variant 1 — reset on negative
def max_sum_kd_alg(nums):
    max_sum = float('-inf')
    current = 0
    for num in nums:
        current += num
        max_sum = max(current, max_sum)
        if current < 0:
            current = 0
    return max_sum

# Variant 2 — DP
def op_max_sum_kd_alg(nums):
    current = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        max_sum = max(max_sum, current)
    return max_sum
```

**Time:** O(n) | **Space:** O(1)

---

## 9. Greedy Min Tracking — Stock Buy & Sell

**File:** `01array/09_stock_buy_sell_121.py`
**LeetCode:** 121. Best Time to Buy and Sell Stock

**Pattern:** Greedy (track minimum price so far)  
**When to use:** Single transaction — max profit from buying low, selling high.

**Algorithm:**
- Track `min_price` (lowest seen so far).
- For each `price`, compute `profit = price - min_price`.
- Update `max_profit` and `min_price`.

**Code:**
```python
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
```

**Time:** O(n) | **Space:** O(1)

---

## 10. Two Pointer — Alternate Positives & Negatives

**File:** `01array/10rearranging_array_element.py`
**LeetCode:** 2149. Rearrange Array Elements by Sign

**Pattern:** Two Pointer (even/odd index placement)  
**When to use:** Rearrange array with alternating positive/negative numbers.

**Algorithm (in-place):**
- Create `ans` array of same length.
- `pos` pointer at index 0, `neg` pointer at index 1.
- For each `num`:
  - If `num > 0`: place at `ans[pos]`, `pos += 2`.
  - Else: place at `ans[neg]`, `neg += 2`.

**Code:**
```python
def rearranging_element_opt(nums):
    ans = [0] * len(nums)
    pos = 0
    neg = 1
    for num in nums:
        if num > 0:
            ans[pos] = num
            pos += 2
        else:
            ans[neg] = num
            neg += 2
    return ans
```

**Time:** O(n) | **Space:** O(n)

---

## 11. Singly Linked List — CRUD

**File:** `linked_list.py`
**LeetCode:** 707. Design Linked List | 206. Reverse Linked List | 21. Merge Two Sorted Lists

**Pattern:** Linked List Traversal / Pointer Manipulation  
**When to use:** Implement or operate on a singly linked list.

**Operations:**
| Operation | Description |
|-----------|-------------|
| `insert_fr(data)` | Insert at head |
| `insert_end(data)` | Insert at tail |
| `insert_pos(pos, data)` | Insert at position |
| `delete_fr()` | Delete head |
| `delete_end()` | Delete tail |
| `delete_pos(pos)` | Delete at position |
| `length()` | Count nodes |
| `search(value)` | Find value |
| `display()` | Print list |

**Code (core):**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_fr(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
```

**Time:** O(n) worst-case insert/delete | **Space:** O(1) per operation

---

## 12. Doubly Linked List — CRUD

**File:** `double_linked_list.py`
**LeetCode:** 1472. Design Browser History | 432. All O(1) Data Structure

**Pattern:** Linked List with Previous Pointer  
**When to use:** Bidirectional traversal, efficient deletion of a node given its pointer.

**Code (core):**
```python
class Node:
    def __init__(self, value=None):
        self.prev = None
        self.data = value
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_fr(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        new.next = self.head
        self.head.prev = new
        self.head = new

    def insert_end(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def delete_ll(self, value):
        if self.head is None:
            return
        temp = self.head
        if temp.data == value:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
        while temp:
            if temp.data == value:
                if temp.next:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                else:
                    temp.prev.next = None
                return
            temp = temp.next
```

**Time:** O(n) search/delete | **Space:** O(1)

---

## 13. Binary Search — Median of Two Sorted Arrays

**File:** `leetcode_4.py`
**LeetCode:** 4. Median of Two Sorted Arrays

**Pattern:** Binary Search on Partitions  
**When to use:** Find median of two sorted arrays in O(log(min(m,n))) time.

**Algorithm:**
- Ensure `nums1` is the smaller array (swap if needed).
- Binary search on `nums1` partition index `p1`.
- `p2 = (m+n+1)//2 - p1` (partition on `nums2`).
- Compute `l1, r1, l2, r2` around the partitions.
- If `l1 <= r2` and `l2 <= r1`: found correct partition.
  - Even length → average of max left and min right.
  - Odd length → max of left side.
- Else adjust bounds.

**Code:**
```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            p1 = (low + high) // 2
            p2 = (m + n + 1) // 2 - p1

            l1 = float('-inf') if p1 == 0 else nums1[p1-1]
            r1 = float('inf') if p1 == m else nums1[p1]
            l2 = float('-inf') if p2 == 0 else nums2[p2-1]
            r2 = float('inf') if p2 == n else nums2[p2]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                return max(l1, l2)
            elif l1 > r2:
                high = p1 - 1
            else:
                low = p1 + 1
```

**Time:** O(log(min(m,n))) | **Space:** O(1)

---

## 14. Binary Search — Search a 2D Matrix

**File:** `leetcode_74_binary.py`
**LeetCode:** 74. Search a 2D Matrix

**Pattern:** Nested Binary Search  
**When to use:** Search in a row-wise and column-wise sorted matrix.

**Algorithm:**
1. **Find row:** Binary search on first/last element of each row to find the row containing target.
2. **Find column:** Standard binary search within that row.

**Code:**
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        def search_for_row():
            low, high = 0, len(matrix) - 1
            while low <= high:
                mid = (low + high) // 2
                first, last = matrix[mid][0], matrix[mid][-1]
                if first <= target <= last:
                    return mid
                elif target > last:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        def search_on_row(row):
            low, high = 0, len(matrix[row]) - 1
            while low <= high:
                mid = (low + high) // 2
                value = matrix[row][mid]
                if value == target:
                    return True
                elif value < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        row = search_for_row()
        if row == -1:
            return False
        return search_on_row(row)
```

**Time:** O(log m + log n) | **Space:** O(1)

---

## 15. Merge Intervals

**File:** `01array/11_marged_inetrvals.py`
**LeetCode:** 56. Merge Intervals

**Pattern:** Sort + Greedy Merge  
**When to use:** Given overlapping intervals, merge them into non-overlapping intervals.

**Algorithm:**
- Sort intervals by start time.
- **Brute (in-place pop):** Compare adjacent intervals; if overlapping, merge by extending `end` and pop the merged interval.
- **Optimal (separate list):** Start `ans` with first interval. For each `current`:
  - If `current[0] <= last[1]` → overlap → `last[1] = max(last[1], current[1])`.
  - Else → append `current` to `ans`.

**Code:**
```python
def merge_intervals_obt(intervals):
    intervals.sort()
    ans = [intervals[0]]

    for current in intervals[1:]:
        last = ans[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            ans.append(current)
    return ans
```

**Time:** O(n log n) (sorting) | **Space:** O(n) (output)

---

## 16. Matrix — Set Matrix Zeroes

**File:** `01array/12_matrix_set_row_col_zero.py`
**LeetCode:** 73. Set Matrix Zeroes

**Pattern:** In-place Marker / First Row-Column Flags  
**When to use:** If an element in matrix is 0, set its entire row and column to 0.

**Algorithm:**
### Approach 1 — Brute (Marker)
- Traverse matrix. When `mat[i][j] == 0`, mark all non-zero elements in row `i` and col `j` with a special marker (e.g., `-1`).
- Second pass: replace all markers with 0.

### Approach 2 — Optimal (O(1) space)
- Check if first row / first column contains any zero → store in `first_row`, `first_col`.
- Use first row and first column as markers: for `i >= 1, j >= 1`, if `mat[i][j] == 0`, set `mat[i][0] = 0` and `mat[0][j] = 0`.
- Fill interior using markers: if `mat[i][0] == 0 or mat[0][j] == 0`, set `mat[i][j] = 0`.
- Handle first row and first column using saved flags.

**Code:**
```python
def set_mat_to_zero(mat):
    row = len(mat)
    col = len(mat[0])
    MARK = -1
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 0:
                for c in range(col):
                    if mat[i][c] != 0:
                        mat[i][c] = MARK
                for r in range(row):
                    if mat[r][j] != 0:
                        mat[r][j] = MARK
    for i in range(row):
        for j in range(col):
            if mat[i][j] == MARK:
                mat[i][j] = 0
    return mat
```

**Time:** O((n*m)*(n+m)) brute / O(n*m) optimal | **Space:** O(1)

---

## 17. Matrix — Spiral Matrix

**File:** `01array/13_spiral_matrix.py`
**LeetCode:** 54. Spiral Matrix

**Pattern:** Boundary Traversal  
**When to use:** Traverse a matrix in spiral order (clockwise).

**Algorithm:**
- Maintain four boundaries: `top`, `bottom`, `left`, `right`.
- While `top <= bottom` and `left <= right`:
  1. Traverse left → right on `top` row, increment `top`.
  2. Traverse top → bottom on `right` col, decrement `right`.
  3. If `top <= bottom`: traverse right → left on `bottom` row, decrement `bottom`.
  4. If `left <= right`: traverse bottom → top on `left` col, increment `left`.
- Return collected elements.

**Code:**
```python
def set_spiral_order(mat):
    ans = []
    top = 0
    right = len(mat[0]) - 1
    left = 0
    bottom = len(mat) - 1
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            ans.append(mat[top][col])
        top += 1
        for row in range(top, bottom + 1):
            ans.append(mat[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                ans.append(mat[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                ans.append(mat[row][left])
            left += 1
    return ans
```

**Time:** O(n*m) | **Space:** O(1) (excluding output)

---

## 18. Prefix & Suffix Product — Product of Array Except Self

**File:** `01array/14_product_without_self.py`
**LeetCode:** 238. Product of Array Except Self

**Pattern:** Prefix & Suffix Product (running product)  
**When to use:** Find product of all elements except `nums[i]` without division (handles zeroes safely).

**Algorithm:**
- **Brute:** For each index `i`, multiply all elements where `i != j`. O(n²) — too slow.
- **Optimal (prefix × suffix):**
  1. `ans[i]` = product of all elements **to the left** of `i` (prefix pass).
  2. Multiply `ans[i]` by product of all elements **to the right** of `i` (suffix pass, scanning from end).
  3. Use running `prefix` / `suffix` variables instead of extra arrays → O(1) extra space.

**Code:**
```python
def product_of_array_without_self(nums):
    n = len(nums)
    ans = [1] * n
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
            ans[i] = prod
    return ans

def productExceptSelf(nums):
    n = len(nums)
    ans = [1] * n

    prefix = 1
    for i in range(n):
        ans[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= suffix
        suffix *= nums[i]

    return ans
```

**Time:** O(n²) brute / O(n) optimal | **Space:** O(n) output (O(1) extra in optimal)

---

## 19. Sorting — Bubble Sort

**File:** `02sorting/01_bubble_sort.py`
**LeetCode:** — (fundamental; used in variants like 283. Move Zeroes)

**Pattern:** Adjacent Swapping (Brute Sorting)  
**When to use:** Understand the simplest sorting idea; small or nearly sorted arrays.

**Algorithm:**
- Loop `i` times for each pass over the array.
- In each pass, compare adjacent elements `nums[j]` and `nums[j+1]`.
- If `nums[j] > nums[j+1]`, swap them (bigger elements "bubble up" to the end).
- After each pass, the largest remaining element is fixed at the end, so inner loop shrinks by `i`.

**Code:**
```python
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
```

**Time:** O(n²) worst/avg, O(n) best (already sorted with flag) | **Space:** O(1)

---

## 20. Sorting — Selection Sort

**File:** `02sorting/02_selection_sort.py`
**LeetCode:** — (concept in 215. Kth Largest Element, 912. Sort an Array)

**Pattern:** Find-Minimum-and-Swap  
**When to use:** Small arrays where number of swaps must be minimized.

**Algorithm:**
- For each position `i`, assume `min = i`.
- Scan the rest of the array from `i+1` to find the smallest element.
- If a smaller element is found, update `min`.
- Swap `nums[i]` with `nums[min]` — the correct element is now fixed in place.

**Code:**
```python
def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums
```

**Time:** O(n²) always | **Space:** O(1)

---

## 21. Sorting — Insertion Sort

**File:** `02sorting/03_inserction_sort.py`
**LeetCode:** — (concept in 147. Insertion Sort List)

**Pattern:** Insert into Sorted Left Part (like playing cards)  
**When to use:** Small or nearly sorted arrays; stable sorting; online (incremental) data.

**Algorithm:**
- Start from index 1 (left part is already sorted).
- Pick `key = nums[i]`, then shift larger elements one position right using `j = i - 1`.
- While `j >= 0` and `nums[j] > key`, move `nums[j]` to `nums[j+1]` and decrement `j`.
- Place `key` at `nums[j+1]` — the sorted part now grows by one.

**Code:**
```python
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
```

**Time:** O(n²) worst/avg, O(n) best (already sorted) | **Space:** O(1)

---

## 22. Sorting — Merge Sort

**File:** `02sorting/04_merge_sort.py`
**LeetCode:** 912. Sort an Array | 148. Sort List | 23. Merge k Sorted Lists

**Pattern:** Divide & Conquer (Recursive Split + Merge)  
**When to use:** Stable sort needed; large arrays where O(n log n) is required; linked list sorting.

**Algorithm:**
- **Divide:** Recursively split the array into two halves until each half has 1 element.
- **Conquer:** Merge two sorted halves back together:
  - Create temp arrays `L` and `R` from the halves.
  - Compare `L[i]` and `R[j]`, placing the smaller into `nums[k]`.
  - Copy any remaining elements from `L` or `R`.
- Base case: `l >= r` → single element is already sorted.

**Code:**
```python
def merge(nums, l, m, r):
    s1 = m - l + 1
    s2 = r - m
    L = [0] * s1
    R = [0] * s2
    for i in range(s1):
        L[i] = nums[l + i]
    for j in range(s2):
        R[j] = nums[m + 1 + j]
    i = j = 0
    k = l
    while i < s1 and j < s2:
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1
    while i < s1:
        nums[k] = L[i]
        i += 1
        k += 1
    while j < s2:
        nums[k] = R[j]
        j += 1
        k += 1

def divide(nums, l, r):
    if l < r:
        m = (l + r) // 2
        divide(nums, l, m)
        divide(nums, m + 1, r)
        merge(nums, l, m, r)
    return nums
```

**Time:** O(n log n) always | **Space:** O(n) (temp arrays + recursion)

---

## 23. Binary Search — Classic Search

**File:** `03binary/01_binary_search.py`
**LeetCode:** 704. Binary Search

**Pattern:** Divide & Conquer on Sorted Array  
**When to use:** Search for a target in a sorted array in O(log n) time.

**Algorithm:**
- Set `l = 0`, `r = len(nums) - 1`.
- While `l <= r`:
  - `mid = (l + r) // 2`.
  - If `nums[mid] == target` → return `mid`.
  - If `nums[mid] < target` → search right half (`l = mid + 1`).
  - Else → search left half (`r = mid - 1`).
- Return `-1` if target not found.

**Code:**
```python
def binary_search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1
```

**Time:** O(log n) | **Space:** O(1)

---

## 24. Binary Search — Lower Bound / Insert Position

**File:** `03binary/02_lower_bound_search_at_insert_pos.py`
**LeetCode:** 35. Search Insert Position

**Pattern:** Lower Bound (first index where `nums[mid] >= target`)  
**When to use:** Find insertion position for a target in a sorted array; template for lower bound.

**Algorithm:**
- Standard binary search loop with `l <= r`.
- If `nums[mid] == target` → return `mid` (position found).
- Else narrow the search; when the loop ends, `l` is the first index where `nums[l] >= target`.
- Return `l` (safe insert position).

**Code:**
```python
def lower_bound(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
                r = mid - 1
        else:
                l = mid + 1

    return l
```

**Time:** O(log n) | **Space:** O(1)

---

## 25. Binary Search — First & Last Position

**File:** `03binary/03_lower_and_upper_bound.py`
**LeetCode:** 34. Find First and Last Position of Element in Sorted Array

**Pattern:** Dual Binary Search (left bound + right bound)  
**When to use:** Find the range of a target in a sorted array with duplicates.

**Algorithm:**
- **Left bound:** binary search that keeps searching left after a match — on match, save `index` and set `high = mid - 1`.
- **Right bound:** binary search that keeps searching right after a match — on match, save `index` and set `low = mid + 1`.
- Return `[left, right]`; both stay `-1` if target absent.

**Code:**
```python
def searchRange(nums, target):

    def find_left_bound(nums, target):
        index = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return index

    def find_right_bound(nums, target):
        index = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return index

    return [find_left_bound(nums, target), find_right_bound(nums, target)]
```

**Time:** O(log n) | **Space:** O(1)

---

## 26. Binary Search — Search in Rotated Sorted Array

**File:** `03binary/04_rotating_array.py`
**LeetCode:** 33. Search in Rotated Sorted Array

**Pattern:** Partition Check (identify sorted half)  
**When to use:** Search in an array rotated at an unknown pivot — at least one half is always sorted.

**Algorithm:**
- Base case: `l > r` → `-1`.
- `mid = l + (r - l) // 2`. If `nums[mid] == target` → return `mid`.
- **If left half is sorted** (`nums[l] <= nums[mid]`):
  - Target in `[nums[l], nums[mid])` → recurse left, else recurse right.
- **Else right half is sorted:**
  - Target in `(nums[mid], nums[r]]` → recurse right, else recurse left.

**Code:**
```python
def rotated_array(nums, target, l, r):

    if l > r:
        return -1

    mid = l + (r - l) // 2

    if nums[mid] == target:
        return mid

    # Left half is sorted
    if nums[l] <= nums[mid]:

        if nums[l] <= target < nums[mid]:
            return rotated_array(nums, target, l, mid - 1)
        else:
            return rotated_array(nums, target, mid + 1, r)

    # Right half is sorted
    else:

        if nums[mid] < target <= nums[r]:
            return rotated_array(nums, target, mid + 1, r)
        else:
            return rotated_array(nums, target, l, mid - 1)
```

**Time:** O(log n) | **Space:** O(log n) (recursion stack)

---

## 27. Binary Search — Minimum in Rotated Sorted Array

**File:** `03binary/05_find_minimum_in_sorted_array.py`
**LeetCode:** 153. Find Minimum in Rotated Sorted Array | 154. (with duplicates)

**Pattern:** Boundary Binary Search (compare `mid` with `r`)  
**When to use:** Find the pivot (minimum) of a rotated sorted array.

**Algorithm:**
- **Distinct values:** while `l < r`, `mid = (l + r) // 2`:
  - If `nums[mid] > nums[r]` → min is in right half (`l = mid + 1`).
  - Else → min is at `mid` or left (`r = mid`).
- **With duplicates:** when `nums[mid] == nums[r]`, decrement `r -= 1` to skip the duplicate.

**Code:**
```python
def find_minimim(nums):
    l = 0
    r = len(nums)-1

    while l < r:

        mid = (l+r)//2

        if nums[mid] > nums[r]:
            l = mid + 1

        else:
            r = mid

    return nums[l]

def find_minimim2(nums):
    l = 0
    r = len(nums)-1

    while l < r:

        mid = (l+r)//2

        if nums[mid] > nums[r]:
            l = mid + 1

        elif nums[mid] < nums[r]:
            r = mid

        else:
            r -= 1

    return nums[l]
```

**Time:** O(log n) (O(log n) avg, O(n) worst with duplicates) | **Space:** O(1)

---

## 28. Binary Search — Find Peak Element

**File:** `03binary/06_peak_element.py`
**LeetCode:** 162. Find Peak Element

**Pattern:** Binary Search on Comparison (`mid` vs `mid+1`)  
**When to use:** Find a peak (element greater than its neighbors) in O(log n); no full sorting required.

**Algorithm:**
- Binary search on indices. `mid = l + (r - l) // 2`.
- If `nums[mid] < nums[mid + 1]` → peak lies on the right, move `l = mid + 1`.
- Else → `nums[mid]` is at least a peak on the left side, move `r = mid`.
- When `l == r`, return `l` (a valid peak index).

**Code:**
```python
def find_peak_element(nums):
    l = 0
    r = len(nums)

    while l < r:
        mid = l + (r-l) // 2

        if nums[mid] < nums[mid+1]:
            l = mid + 1
        else:
            r = mid

    return l
```

**Time:** O(log n) | **Space:** O(1)

---

## Pattern Cheat Sheet

| # | Pattern | Use Case |
|---|---------|----------|
| 1 | Greedy Variable Tracking | Top-k elements, min/max |
| 2 | Single Pass Flags | Check sorted, monotonic |
| 3 | Two Pointer (slow/fast) | In-place dedup, partitioning |
| 4 | Reversal Algorithm | Rotate array, reverse words |
| 5 | Two Pointer (partition) | Move zeroes, segregate |
| 6 | Hash Map (complement) | Pair sum, subarray sum |
| 7 | Boyer-Moore Voting | Majority element |
| 8 | Kadane's Algorithm | Max subarray sum |
| 9 | Greedy Min/Max Tracking | Stock buy/sell |
| 10 | Even/Odd Index Placement | Alternate reordering |
| 11 | Linked List Traversal | CRUD on linked list |
| 12 | Bidirectional Traversal | CRUD on doubly linked list |
| 13 | Binary Search on Partitions | Median of two arrays |
| 14 | Nested Binary Search | 2D matrix search |
| 15 | Sort + Greedy Merge | Merge overlapping intervals |
| 16 | In-place Marker / First Row-Col Flags | Set matrix zeroes |
| 17 | Boundary Traversal | Spiral order traversal |
| 18 | Prefix & Suffix Product | Product of array except self |
| 19 | Adjacent Swapping | Bubble sort |
| 20 | Find-Minimum-and-Swap | Selection sort |
| 21 | Insert into Sorted Left Part | Insertion sort |
| 22 | Divide & Conquer (Split + Merge) | Merge sort |
| 23 | Divide & Conquer on Sorted Array | Classic binary search |
| 24 | Lower Bound (first ≥ target) | Insert position |
| 25 | Dual Binary Search (left/right) | First & last occurrence |
| 26 | Partition Check (sorted half) | Search in rotated array |
| 27 | Boundary Binary Search (mid vs r) | Min in rotated array |
| 28 | Binary Search on Comparison | Find peak element |
