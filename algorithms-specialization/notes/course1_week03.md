---
tags: algorithms, notes
---
Algorithm (Quick Sort, )
===
## Quick Sort
Input:  
array of n numbers, unsorted.

Output:  
Same numbers, sorted in increasing order.

Assume:  
All array entries distinct

### Quick Sort: High-Level Description
(Hoore Cicca 1961)

```
QuickSort(array A, length n)
    if n = 1
        return
    p = ChoosePivot(A, n)
    Partition A around p
    recursively sort 1st part
    recursively sort 2nd part
```
![Image](https://i.imgur.com/23TQLq0.png)

相對於Merge Sort，沒有combine step

### Partitioning Around a Pivot
1. linear time ($O(n)$), no extra memory
2. reduces problem size

![Image](https://i.imgur.com/3GYbW4v.png)

#### Example
![Image](https://i.imgur.com/T54ksjg.png)

![Image](https://i.imgur.com/OsxhdhG.png)
最後pivot要跟$i$交換

#### Pseudocode for Partition
```
Input = A[l, ..., r]

Partition(A, l, r)
    p = A[l]
    i = l + 1
    for j = l + 1 to r
        if A[j] < p  (if A[j] > p, do nothing)
            swap A[j] and A[i]
            i++
    swap A[l] and A[i + 1]
```

![Image](https://i.imgur.com/YJl3Syh.png)

Running Time:  
$O(n)$, where $n=r-l+1$ is the length of the input subarray.

$O(1)$ work per array entry and works inplace (by swaping)

Correctness:  
The for loop maintains the invariants  
1. $A[l+1], ..., A[i-1]$ are all less than the pivot
2. $A[i], ..., A[j-1]$ are all greater than pivot

=> after final swap, array partitioned around pivot

### Choosing a Good Pivot
Running time of Quick Sort dependds on the quality of the pivot

如果總是選第一個元素作為pivot，在一個已經反向排序好的array上：  
Running time最差為$O(n^2)$  
![Image](https://i.imgur.com/PjW1XUu.png)

若運氣很好，每次都剛好選到中位數  
Running time為$O(nlogn)$  
![Image](https://i.imgur.com/LYuqh4F.png)

#### Random Pivots
Intuition:  
1. If always get a 25-75 split, good enuough for $O(nlogn)$ running time  
    (prove via recursion tree)
2. Half of elements give a 25-75 split
