---
tags: algorithms, notes
---
Algorithm (Quick Sort)
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
Running time為$O(n\log n)$  
![Image](https://i.imgur.com/LYuqh4F.png)

#### Random Pivots
Intuition:  
1. If always get a 25-75 split, good enuough for $O(n\log n)$ running time  
    (prove via recursion tree)
2. Half of elements give a 25-75 split  
    譬如說1-100的數列，只要選到26-75就會落在25-75的範圍內，故會有50%的機率

#### Average Running Time of QuickSort
QuickSort Theorem:  
For every input array of length $n$, the average running time of QuickSort (with random pivot) is $O(n\log n)$

對於任何的input data皆成立！

### QuickSort: Analysis
#### Preliminaries
Fix input array A of length n.

Sample space $\Omega$ = all possible outcomes of random choices in QuickSort (i.e., pivot sequences)

Key random variable:  
for $\sigma \in \Omega$, $C(\sigma)$ = number of comparisons between two input elements made by QuickSort (given random choices $\sigma$)

Lemma:  
Running time of QuickSort dominated by comparisons  
沒有去證明，不過相對不重要，因為QuickSort大部分消耗的時間都來自於"比較"

Goal:  
$E[C] = O(n\log n)$

#### Building Blocks
無法使用Master Method  
(因為random, unbalanced subproblems)

Notation:  
- $A$ = fixed input array
- $z_i=i^{\text{th}}$ smallest element of $A$  
    ![Image](https://i.imgur.com/qBlDalY.png)
- For $\sigma \in \Omega$, indices $i<j$, let $X_{ij}(\sigma)$ = number of times $z_i, z_j$ get compared in QuickSort with pivot sequence.

![Image](https://i.imgur.com/pxOnuBY.png)  
pivot會和其他元素比較正好1次，且這個pivot結束partition流程後就不會再被拿來比較了 (divide & conquer)

#### A Decomposition Approach
So:  
- $C(\sigma)$ = number of comparisons between input elements
- $X_{ij}(\sigma)$ = number of comparisions between $z_i, z_j$

Thus:  
$\forall \sigma, C(\sigma)=\Sigma_{i=1}^{n-1}\Sigma_{j=i+1}^{n}X_{ij}(\sigma)$

By linearity of expection:  
$E[C] = \Sigma_{i=1}^{n-1}\Sigma_{j=i+1}^{n}E[X_{ij}]$  
Since $E[X_{ij}]=0\cdot Pr[X_{ij}=0]+1\cdot Pr[X_{ij}=1]=Pr[X_{ij}=1]$

Thus:  
$E[C] = \Sigma_{i=1}^{n-1}Pr[z_i, z_j \text{ get compared}]$ (\*)

上面流程主要為：
1. 找出真正重要的random variable Y
2. 將Y表達成其他指標性的random variable的總和, $Y=\Sigma_{l=1}^mX_l$
3. 利用linearity of expectation:  
    $E[Y]=\Sigma_{l=1}^mPr[X_l=1]$  
    就只要知道$X_l$即可求解

#### Key Claim
$\forall i<j, Pr[z_i, z_j \text{ get compared}] = \frac{2}{j-i+1}$

Proof:  
Fix $z_i, z_j$ with $i<j$. Consider the set $z_i, z_{i+1}, ..., z_{j-1}, z_j$

Inductively:  
As long as some of these are chosen as a pivot, all are passed to the same recursive call

Consider the first among $z_i, z_{i+1}, ..., z_{j-1}, z_j$ that gets chosen as a pivot  
1. if $z_i$ or $z_j$ gets chosen first, then $z_i$ and $z_j$ get compared  
    如果其中一者被選為pivot, 則這兩者一定會被比較
2. if one of $z_{i+1}, ..., z_{j-1}$ get chosen first, then $z_i, z_j$ are never compared  
    如果(i+1)~(j-1)被選為pivot, 則i和j一定不會被比較，因為被分成不同split了

Note:  
Since pivots always chosen uniformly at random, each of $z_i, z_{i+1}, ..., z_{j-1}, z_j$ is equally likely to be the first pivot.  
=> $Pr[z_i, z_j \text{ get compared}] = \frac{2}{j-i+1}$  
- 分子$2$代表第一種情況，其中兩者之一被選為pivot
- 分母$j-i+1$代表所有可能的情況 (第一種+第二種)

So:  
$E[C] = \Sigma_{i=1}^{n-2}\Sigma_{j=i+1}^n\frac{2}{j-i+1}$ (\*)

#### Final Calculations
$E[C] = 2\Sigma_{i=1}^{n-2}\Sigma_{j=i+1}^n\frac{1}{j-i+1}$

Note:  
For each fixed $i$, the inner sum is $\Sigma_{j=i+1}^n\frac{1}{j-i+1}=\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+...$

![Image](https://i.imgur.com/LfVtAGp.png)

So:  
$E[C] \leq 2\cdot n\cdot \Sigma_{k=2}^n\frac{1}{k}$

現在只要證明$\Sigma_{k=2}^n\frac{1}{k} < \ln n$

![Image](https://i.imgur.com/0Kmk8i0.png)

So:  
$E[C] = 2n\ln n$ 證明完畢！

### Problem Set
[https://blogs.asarkar.com/algorithms-design-analysis/probability/](https://blogs.asarkar.com/algorithms-design-analysis/probability/)
