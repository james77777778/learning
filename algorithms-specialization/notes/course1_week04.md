---
tags: algorithms, notes
---
Algorithm (Linear-Time Selection, Graphs, Contraction Algorithm)
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

### Proof I: Tracking Progress via Phases
Note:  
RSelect uses $\leq cn$ operations outside of the recursive call (for some constant $c > 0$)

Notation:  
RSelect is in phase $j$ if current array size between $(\frac{3}{4})^{j+1}n$ and $(\frac{3}{4})^{j}n$
- $X_j$ = number of recursive calls during phase $j$

Note:  
Running time of RSelect $\leq \Sigma_{\text{phase }j}X_j \cdot c \cdot (\frac{3}{4})^jn$ (\*)
- $(\frac{3}{4})^jn$: $\leq$ array size during phase $j$
- $c \cdot (\frac{3}{4})^jn$: works per phase $j$ subproblem
- $X_j$: number of phase $j$ subproblems

### Proof II: Reduction to Coin Flipping
Note:  
If RSelect choose a pivot giving a 25-75 split (or better), **then current phase ends!**  
新的subarray最大就是75%的原本長度

Recall:  
probability of 25-75 split or better is 50%

So:  
$E[X_j] \leq$ expected number of times you need to flip a fair coin to get one "heads"  
(如果正面代表好的pivot; 反面代表不好的pivot)

### Proof III: Coin Flipping Analysis
Let $N$ = number of coin flips until get heads. (geometric random variable)

Note:  
$E[N] = 1 + \frac{1}{2} \cdot E[N]$
- $1$: 代表第一次就骰到正面
- $\frac{1}{2} \cdot E[N]$: 代表骰到反面，之後的期望值

Solution:  
$E[N] = 2$ 並且已知 $E[X_j] \leq E[N]$

### Final Proof
Running time of RSelect $\leq \Sigma_{\text{phase }j}X_j \cdot c \cdot (\frac{3}{4})^jn$ (\*)

Expected running time of RSelect $\leq E[cn\Sigma_{\text{phase }j}(\frac{3}{4})^jX_j]$ (\*)

$= cn\Sigma_{\text{phase }j}(\frac{3}{4})^jE[X_j]$

$\leq 2cn\Sigma_{\text{phase }j}(\frac{3}{4})^j$  
(利用等比級數公式得到$\Sigma_{\text{phase }j}(\frac{3}{4})^j \leq \frac{1}{1-\frac{3}{4}} = 4$)

$\leq 8cn = O(n)$

證明完畢！

## Graphs
- Verices (Nodes, V)
- Edges (E): pairs of vertices
    - can be undirected (unordered) / directed (ordered, arcs)
    ![Image](https://i.imgur.com/gTVanwW.png)

Examples:  
road networks, the web

### Cuts of Graphs
Definition:  
a cut of a graph (V, E) is a partition of V into two non-empty sets A and B
![Image](https://i.imgur.com/Z5lruvj.png)

Definition:  
the crossing edges of a cut (A, B) are those with:
- one endpoint in each of (A, B) (undirected)
- tail in A, head in B (directed)

A graph with $n$ vertices has $2^n$ cuts

### The Minimum Cut Problem
Input:  
An undriected graph $G=(V, E)$, parallel edges allowed  
![Image](https://i.imgur.com/GJH9iz0.png)

Goal:  
compute a cut with fewest number of crossing edges (min cut)

![Image](https://i.imgur.com/Q8cWENL.png)

A Few Applications:  
- identify network bottlenecks
- community detection
- iamge segmentation

### Graph Representation
只考慮edge number，而非考慮minimu cuts
![Image](https://i.imgur.com/HY1NAsD.png)

- Adjacency Matrix
- Adjacency Lists (後續課程主要使用這個資料結構)
