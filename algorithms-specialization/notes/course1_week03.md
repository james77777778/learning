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
Key idea:  
Partition array around a **pivot** element
- pick element of array
    ![Image](https://i.imgur.com/X7dCzVM.png)
- rearrange array so that:  
    - left of pivot => less than pivot
    - right of pivot => greater than pivot
    ![Image](https://i.imgur.com/1Gvqpze.png)

Note:  
Puts pivot in its "rightful position"

Partition的特別特性:  
1. linear time ($O(n)$), no extra memory
2. reduces problem size

![Image](https://i.imgur.com/3GYbW4v.png)

#### In-Place Implementation
Assume:  
pivot = 1st element of array  
(if not, let choosing pivot as preprocessing step)

High-level idea:  
![Image](https://i.imgur.com/vDiON88.png)
- single scan through array
- invariant: everything looked at so far is partitioned

#### Example
![Image](https://i.imgur.com/T54ksjg.png)

![Image](https://i.imgur.com/OsxhdhG.png)
最後pivot要跟$i$交換

```
Partition(A, l, r)

```