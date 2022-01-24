---
tags: algorithms, notes
---
Algorithm (Linear-Time Selection)
===
## Problem
Input:  
array A with n distinct numbers and a number $i \in \{1, 2, ..., n\}$

Output:  
$i^{th}$ order statistic. (i.e., $i^{th}$ smallest element of input arrary)

Example:  
median

### Reduction
可以利用Merge Sort  
1. 先sort後
2. return第i個element

可在$O(n\log n)$內解決

如果利用sorting的話，沒辦法比$O(n\log n)$更快了

Next:  
$O(n)$ time (randomized) by modifying QuickSort  

也有比較複雜的deterministic algorithm (optional video)  
- pivot = "median of median" (不過實務上不常用)

## Randomized Selection
