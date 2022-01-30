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

### Graph Representation
只考慮edge number，而非考慮minimu cuts
![Image](https://i.imgur.com/HY1NAsD.png)

- Adjacency Matrix
- Adjacency Lists (後續課程主要使用這個資料結構)

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

## Random Contraction Algorithm
(Karger, early 90s)

```
While there are more than 2 vertices:  
- pick a remaining edge (u, v) uniformly at random
- merge (or contract) u and v into a single vertex
- remove self-loops
return cut represented by final 2 vertices
```

主要做法就是不停的把nodes合併成super nodes，最後再展開來得到cut

Example:  
![Image](https://i.imgur.com/VnuIKq1.png)

但是這是個random的演算法，也有可能找到不好的結果：

![Image](https://i.imgur.com/SUQQ7y3.png)

重要要問的是，有多少的機率能夠成功找到min cut？

### Random Contraction Algorithm: The probability of success?
Fix a graph G=(V, E) with n vertices, m edges  
Fix a minimum cut (A, B)  
Let k = number of edges crossing (A, B)  
(call these edges F)

### What coud go wrong?
1. Suppose an edge of F is contracted at some point  
    algorithm will not output (A, B)
2. Suppose only edges inside A or inside B get contracted  
    algorithm will output (A, B)

![Image](https://i.imgur.com/Dx3PK04.png)

Thus:  
$\Pr[\text{output is (A, B)}]$ = $\Pr[\text{never contracts an edge of F}]$

Let Si = event that an edge of F contracted in iteration i

Goal:  
compute $\Pr[\neg S_1 \cap \neg S_2 \cap ... \cap \neg S_{n-2}]$

### The First Iteration
Key Observation:  
degree of each vertex is at least k

- 假設有min cut分成(A, B)兩個set，k為crossing edges的數量
- v個vertices
- m個edges

Reason:  
each vertex v defines a cut ($\{v\}, V-\{v\}$)

![Image](https://i.imgur.com/orkjSE0.png)

Since:  
$kn \leq \Sigma_v\text{degree}(v) = 2m$, we have $m \geq \frac{kn}{2}$

Since:  
$\Pr[S_1] = \frac{k}{m}$, $\Pr[S_1] \leq \frac{2}{n}$

### The Second Iteration
Recall:  
$\Pr[\neg S_1 \cap \neg S_2] = \Pr[\neg S_2 | \neg S_1] \cdot \Pr[\neg S_1]$

其中  
$\Pr[\neg S_2 | \neg S_1]=1-\frac{k}{\text{number remaining edges}}$  
$\Pr[\neg S_1] \geq (1-\frac{2}{n})$

Note:  
all nodes in contracted graph define cuts in G (with at least k crossing edges)  
=> all degrees in contracted graph are at least k

So:  
number of remaining edges $\geq \frac{1}{2}k(n-1)$

So:  
$\Pr[\neg S_2 | \neg S_1] \geq 1-\frac{2}{n-1}$

### All Iterations
In general:  
$\Pr[\neg S_1 \cap \neg S_2 \cap ... \cap \neg S_{n-2}] = \Pr[\neg S_1]\Pr[\neg S_2 | \neg S_1]\Pr[\neg S_3 | \neg S_1 \cap \neg S_2]...\Pr[\neg S_{n-2}|\neg S_1 \cap ... \cap \neg S_{n-1}]$

$\geq (1-\frac{2}{n})(1-\frac{2}{n-2})(1-\frac{2}{n-2})...(1-\frac{1}{n-(n-4)})(1-\frac{1}{n-(n-3)})$

$= \frac{n-2}{n}\frac{n-3}{n-1}...\frac{2}{4}\frac{1}{3}=\frac{2}{n(n-1)} \geq \frac{1}{n^2}$

Problem:  
low success probability!

### Repeated Trials
多試幾次，利用試驗的數量來讓probability不要那麼低

Solution:  
run the basic algorithm a large number $N$ times, remember the smallest cut found

Question:  
how many trials needed?

Let $T_i$ = event that the cut (A, B) is found on the ith try.  
=> by definition, different $T_i$'s are independent

So:  
$\Pr[\text{all N trials fail}] = \Pr[\neg T_1 \cap \neg T_2 \cap ... \cap \neg T_N] = \prod_{i=1}^N\Pr[\neg T_i] \leq (1-\frac{1}{n^2})^N$

Calculus fact:  
$1+x \leq e^x$  
![Image](https://i.imgur.com/hW12bGk.png)

So:  
- if we take $N=n^2$, $\Pr[\text{all fail}] \leq (e^{-\frac{1}{n^2}})^{n^2}=\frac{1}{e}$
- if we take $N=n^2\ln n$, $\Pr[\text{all fail}]\leq (\frac{1}{e})^{\ln n} = \frac{1}{n}$

Running Time:  
polynomial in $n, m$ but slow  
but can get big speedups with more ideas! ($O(n^2)$)

## The Number of Minimum Cuts
Note:  
a graph can have multiple min cuts  
(a tree with n vertices has (n-1) minimum cuts)  
![Image](https://i.imgur.com/ex53tBg.png)

Question:  
what's the largest number of min cuts that a graph with n vertices can have?  

Answer:  
$\begin{pmatrix}n\\2\end{pmatrix} = \frac{n(n-1)}{2}$

### The Lower Bound
Consider the n-cycle  
![Image](https://i.imgur.com/0VpY0K5.png)

Note:  
each pair of the n edges defines a distinct minimum cut (with two crossing edges)  
=> has $\geq \frac{n(n-1)}{2}$ min cuts

每個node都可以跟其他(n-1)個node形成min cut，故全部的可能有$\frac{n(n-1)}{2}$種

### The Upper Bound
Let $(A_1, B_1), (A_2, B_2), ..., (A_+, B_+)$ be the min cuts of a graph with n vertices

By the Contraction Algorithm analysis (without repeated trials):  
$\Pr[\text{output}=(A_i, B_i)] \geq \frac{2}{n(n-1)} = \frac{1}{\begin{pmatrix}n\\2\end{pmatrix}}$  
($\text{output}=(A_i, B_i)) = S_i$

Note:  
$S_i$'s are disjoint events (i.e., only one can happen)  
=> their probabilities sum to at most 1

機率全部相加最多為1

Thus:  
$\frac{+}{\begin{pmatrix}n\\2\end{pmatrix}} \leq 1$  
$+ \leq \begin{pmatrix}n\\2\end{pmatrix}$

## Problem Set
3. Let $0.5 < \alpha < 1$ be some constant. Suppose you are looking for the median element in an array using RANDOMIZED SELECT (as explained in lectures). What is the probability that after the first iteration the size of the subarray in which the element you are looking for lies is $\leq \alpha$ times the size of the original array?  
    ANS: $2\cdot \alpha - 1$  
    原因是要找pivot落在合適的範圍，$p=1-(1-\alpha) - (1-\alpha)=2\cdot \alpha - 1$
4. Let $0 < \alpha < 1$ be a constant, independent of $n$.  Consider an execution of RSelect in which you always manage to throw out at least a $1 - \alpha$ fraction of the remaining elements before you recurse.  What is the maximum number of recursive calls you'll make before terminating?  
    ANS: $-\frac{\log n}{\log \alpha}$  
    假設總共有$n$個元素，第一次call完有$\alpha n$個元素，在第$d$次call完會有$\alpha ^d n$個元素，假設到第$d$次結束則$\alpha ^d n \leq 1$  
    則$d = -\frac{\log n}{\log \alpha}$
5. Now suppose you are given an instance of the minimum cut problem -- that is, you are given an undirected graph (with no specially labelled vertices) and need to compute the minimum cut.  What is the minimum number of times that you need to call the given min s-t cut subroutine to guarantee that you'll find a min cut of the given graph?  
    ANS: $n-1$  
    Fix $s$ to be one of the vertex and $t$ varies across all others, then we are done by picking the smallest one, therefore we need at most $n−1$ call.
