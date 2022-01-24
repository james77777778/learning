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
### Pseudocode
```
RSelect(array A, lenght n, order statistic i)
    if n = 1
        return A[1]
    
    choose pivot p from A uniformly at random

    partition A around p
    let j = new index of p

    if j = i
        return p
    if j > i
        return RSelect(1st part of A, j-1, i)
    if j < i
        return RSelect(2nd part of A, n-j, i-j)
```

![Image](https://i.imgur.com/c2xR3g4.png)

### Running Time
Depends on which pivots get chosen. (could be as bad as $O(n^2)$)

Key:  
Find pivot giving "balanced" split  

Best pivot:  
Median! (but this is circular 因為我們就是要找order statistic)  
=> would get recurrence $T(n) \leq T(\frac{n}{2}) + O(n)$  
=> $T(n) = O(n)$  
(case 2 of Master Method)

期待random pivot能夠做到pretty good和often enuough

RSelect Theorem:  
For every input array of length $n$, the average running time of RSelect is $O(n)$
- holds for every input
- average is over random pivot choices made by the algorithm

### Properties of RSelect
Claim:  
RSelect is correct (guaranteed to output ith order statistic)

Proof:  
By induction

