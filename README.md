# 📁 Selection Sort
> A Python implementation of selection sort, an in place sorting algorithm that repeatedly finds the minimum element and swaps it into position.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Algorithms-red?logo=python&logoColor=white)

---

## 📌 About

This project implements selection sort and rounds out the sorting algorithm collection alongside Merge Sort and Quick Sort. Where those two use divide-and-conquer to achieve O(n log n), selection sort takes a simpler nested loop approach, scanning for the minimum element each pass and swapping it into place. Built to understand O(n²) sorting, in place swapping, and why knowing a slower algorithm makes the faster ones more meaningful

---

## 🧠 What I Learned

- **Nested loops for comparison-based sorting** — The outer loop tracks the current position, the inner loop scans everything to the right of it looking for a smaller value, a clear and readable way to see how O(n²) complexity emerges
- **Tracking the minimum index** — Storing `min_index = i` before the inner loop and updating it whenever a smaller element is found, then only swapping once per outer iteration rather than on every comparison
- **In-place swapping with tuple unpacking** — Using `lst[min_index]`, `lst[i] = lst[i]`, `lst[min_index]` to swap two elements in a single line without a temporary variable
- **Skipping unnecessary swaps** — Checking if `min_index != i` before swapping avoids a pointless operation when the minimum is already in the correct position
- **O(n²) vs O(n log n)** — Understanding that selection sort always performs n² comparisons regardless of input order, making it significantly slower than merge sort or quicksort on large datasets — but simpler to read and reason about
- **When simple algorithms still matter** — Selection sort makes at most O(n) swaps, which makes it useful in situations where writes are expensive, even though comparisons are slow

---

## 🛠️ Technologies Used
| Tool/Library | Purpose |
|---|---|
| Python 3.x | Core Langauge |

---

## 💡 How It Works
```
Original:  [33, 1, 89, 2, 67]

Pass 1: min = 1  at index 1 → swap with index 0 → [1, 33, 89, 2, 67]
Pass 2: min = 2  at index 3 → swap with index 1 → [1, 2, 89, 33, 67]
Pass 3: min = 33 at index 3 → swap with index 2 → [1, 2, 33, 89, 67]
Pass 4: min = 67 at index 4 → swap with index 3 → [1, 2, 33, 67, 89]

Sorted: [1, 2, 33, 67, 89] ✅
```

**Example output:**
```
selection_sort([33, 1, 89, 2, 67, 245])
# [1, 2, 33, 67, 89, 245]

selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3])
# [3, 5, 12, 15, 16, 23, 72, 99, 567]
```

---

## 🚀 Future Improvements

- [ ] Benchmark against merge sort and quicksort on large lists to visualize the O(n²) gap
- [ ] Implement bubble sort for comparison — another O(n²) algorithm with a different swap pattern
- [ ] Add a swap counter to show how few writes selection sort makes compared to other algorithms
- [ ] Visualize each pass using a printed output or `matplotlib`

---

## 📂 Project Structure
```
selection-sort/
│
├── README.md
└── SelectionSortAlgorithm.py    # selection_sort function with example usage
```

*Part of my Python learning journey 🐍 — completing the sorting algorithm collection and understanding the O(n²) vs O(n log n) trade off*
