---
tags: algorithms, notes
---
Algorithm (Heaps, Balanced Binary Search Trees)
===
不同的data structure支援不同的operations，並且能應對不同種類的tasks

我們應該要選擇**剛剛好支援**的data structure

## Heaps
a container for objects that have **keys**
- employer records, network edges, events, etc.

### Supported Operations
1. INSERT:  
    add a new object to a heap  
    running time: $O(\log n)$
2. EXTRACT-MIN (or EXTRACT-MAX):  
    remove an object in heap with a minimum (or maximum) key value  
    running time: $O(\log n)$
3. HEAPIFY  
    n batched INSERTs in $O(n)$ time
4. DELETE  
    running time: $O(\log n)$

### Application: Sorting
SelectionSort $\approx O(n)$ linear time, $O(n^2)$ running time on array of length $n$

HeapSort:  
```
- INSERT all n array elements into a heap
- EXTRACT-MIN to pluck out 拔出 elements in sorted order
```
running time = $2n$ heap operations = $O(n \log n)$ time  
(optimal for a **comparison-based** sorting algorithm!)

### Application: Median Maintanence
Input:  
a sequence $x_1, ..., x_n$ of numbers, 1-by-1

Output:  
at each time step $i$, the median of $\{x_1, ..., x_i\}$

Constraint:  
use $O(\log i)$ time at each step $i$

Solution:  
maintain heaps
- $H_{low}$: supports EXTRACT-MAX
- $H_{high}$: supports EXTRACT-MIN

Key idea:  
maintain invariant that $\approx \frac{i}{2}$  smallest (largest) elements in $H_{low}$ ($H_{high}$)

- 當一個新的數字進來，先利用$H_{low}$ (EXTRACT-MAX) 和$H_{high}$ (EXTRACT-MIN) 找出新的數字應該放在哪個heap？
- 再利用兩個heaps的長度去維持balance
- 最後找到中位數

### Application: Dijkstra's Algorithm
利用heaps來維持並找出Dijkstra greedy score (edge)
