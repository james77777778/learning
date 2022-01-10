---
tags: algorithms, notes
---
Algorithm (Divide & Conquer, Counting Inversions, Master Method)
===
## The Divide and Conquer Paradigm
1. Divde into smaller subproblems
2. Conquer via recursive calls
3. Combine solutions of subproblems into one for the original problem

### Inversion 倒置 The Problem
input: array $A$ containing the numbers $1, 2, 3,..., n$ in some arbitrary order

output: number of inversions = number of pairs $(i, j)$ of array indices with $i<j$ and $A[i] > A[j]$

ex. (1, 3, 5, 2, 4, 6)
![](https://i.imgur.com/ns6Hv1c.png)

motivation: numerical similarity measure between two ranked lists

#### Questions
![](https://i.imgur.com/llYA3vl.png)
solution: ordered list (6, 5, 4, 3, 2, 1)

#### High-Level Approach
brute-force: $O(n^2)$ time  
key idea #1: Divide and Conquer  
![](https://i.imgur.com/fl4JoRl.png)

能不能做得更好？ 可以  
利用Divide + Conquer  
左右兩邊可以利用recursive的方式解，而最後split則需要特別演算法處理

#### High-Level Algorithm
![](https://i.imgur.com/3cXOE19.png)

主要目標是將CountSplitInv壓在linear time ($O(n)$)，若做得到則整個演算法可以在$nlogn$時間內 (like merge sort)

利用Merge Sort特性：
- Count變成Sort-and-Count
- CountSplitInv變成Merge-and-CountSplitInv

為何Merge Sort可以拿來Count Inversions?  
思考一下Merge subroutine，會發現若第二部份比第一部份大，則能找到split inversions

#### Questions
![](https://i.imgur.com/VxzgRKZ.png)

#### Merge Subroutine Example
consider merging B:(1, 3, 5) and C:(2, 4, 6)

output: D: (1, 2, )
=> when 2 copied to output, discover the split inversions (3, 2) and (5, 2)

output: (1, 2, 3, 4, )
=> when 4 copied to output discover (5, 4)

output (1, 2, 3, 4, 5, 6)
finished.

#### General Claim
the split inversions involving an element y of the 2nd array C are precisely the numbers left in the 1st array B when y is copied to the output D

proof:
let $x$ be an element of the 1st array B.  
(1) if $x$ copied to output D before $y$, then $x < y$ => no inversion involving $x, y$  
(2) if $y$ copied to output D before $x$, then $y < x$ => $x, y$ are a spilt inversion  

#### Merge_and_CountSplitInv
- while merging the two sorted subarrays, keep running total of number of split inversions
- when element of 2nd array C gets copied to output D, increment total by number of elements remaining in 1st array B

runtime of subroutine:
$O(n) + O(n) = O(n)$
(merge + running total)
=> Sort_and_Count runs in $O(nlogn)$ time
