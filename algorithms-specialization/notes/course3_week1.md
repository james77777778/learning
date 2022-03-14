---
tags: algorithms, notes
---
Algorithm (Greedy Algorithms, Scheduling Application, Prim's Minimum Spanning Tree)
===
## Greedy Algorithms
### Algorithm Design Paradigms
- Divide and Conquer
- Randomized Algorithms
- Greedy Algorithms
- Dynamic Programming

### Greedy Algorithms
Definition:  
iteratively make **myopic 近視的** decisions, hope everything works out at the end

Example:  
Dijkstra's shortest path

Contrast with Divide & Conquer  
1. easy to propose multiple greedy algorithms
2. easy running time analysis (不像Master method需要較複雜分析)
3. hard to establish correctness (不容易證明greedy演算法的正確性)

Most greedy algorithms are **NOT** correct  
舉Dijkstra's algorithm為例：  
![Image](https://i.imgur.com/qzEs2iw.png)  
- 用greedy的作法會找到：s->w (2)
- 但實際上最短距離應為：s->v->w (1)

### Proofs of Correctness
1. Induction (greedy stays ahead)  
    correctness proof for Dijkstra's algorithm
2. Exchange Argument
3. Whatever Works!

### Application: Optimal Caching
- small fast memory (the cache)
- big slow memory
- process sequence of **page requests**
- on a **page fault** (cache miss)  
    need to evict 驅逐 something from cache to make room - but what?

Example:  
![Image](https://i.imgur.com/AFw1NSo.png)

![Image](https://i.imgur.com/A9Fk6SK.png)  
Request sequence: c, d, e, f, a, b  

=> 4 page faults
- 2 were inevitable (e, f)
- 2 consequences of poor eviction choices (should evict c, d instead of a, b)

### The Optimal Caching Algorithm
Theorem:  
the **farthest-in-future** algorithm is optimal (i.e., minimuizes the number of cache misses)

Why useful?  
1. serves as guideline for practical algorithms (e.g., Least Recently Used, LRU) should do well provided data exhibits locality of reference
2. serves as idealized benchmark for caching algorithms

Proof:  
tricky exchange argument

### Application: A Scheduling Problem
Setup:  
- 1 shared resource (e.g., a processor)
- many jobs to do (e.g., processes)

Question:  
in what order should we sequence the jobs?  

Assume each job $j$ has a:    
- weight $w_j$ (priority)
- length $l_j$

#### Completion Times
Definition:  
completion time $C_j$ of job $j$ = sum of job lengths up to and including $j$

Example:  
3 jobs, $l_1=1, l_2=2, l_3=3$  
![Image](https://i.imgur.com/zTR95EH.png)

Question:  
what is $C_1, C_2, C_3$?  
Ans: 1, 3, 6

#### The Objective Function
Goal:  
minimize the weighted sum of completion times: $\min \Sigma_{j=1}^{n} w_jC_j$

前情提要： $C_1, C_2, C_3$? Ans: 1, 3, 6  
If $w_1=3, w_2=2, w_1=1$, sum is $3\cdot 1+ 2\cdot 3 + 1\cdot 6 = 15$

#### Intuition for Algorithm
Recall:  
want to $\min \Sigma_{j=1}^{n} w_jC_j$

Goal:  
devise correct greedy algorithm

Question:  
1. with equal lengths, schedule larger- or smaller-weight jobs earlier? **larger**
2. with equal weigths, schedule shorter or longer jobs earlier? **shorter**

#### Resolving Conflicting Advice
Question:  
what if $w_i > w_j$ but $l_i > l_j$?

Idea:  
assign **scores** to jobs that are!
- increasing in weight
- decreasing in length

1. Guess: order jobs by decreasing value of $w_j - l_j$
2. Guess: order jobs by decreasing ratio $\frac{w_j}{l_j}$

Breaking a greedy algorithm:  
To distinguish guess 1 and 2: find example where the two produce different outputs

Example:  
- $l_1=5, w_1=3$ (larger ratio, $\frac{3}{5} > \frac{1}{2}$)
- $l_2=2, w_2=1$ (larger difference, $-1 > -2$)

Question:  
what is the sum of weighted completion times of algorithms 1 & 2, respectively?  
1. 先2再1： $1\cdot 2 + 3 \cdot 7 = 23$
2. 先1再2： $3\cdot 5 + 1 \cdot 7 = 22$

So:  
Alg 1 not (always) correct

Claim:  
Alg 2 (order jobs by decreasing ratio $\frac{w_j}{l_j}$) is always correct!

#### Correctness Proof
order jobs by decreasing ratio $\frac{w_j}{l_j}$

Proof:  
by an **Exchange Argument**

Plan:  
Fix arbitrary input of $n$ jobs. Will proceed by contradiction.  
let $\sigma=$ greedy schedule, $\sigma^*=$ optimal schedule  
greedy schedule will produce schedule even better than $\sigma^*$, contradicting purported 據稱的 optimality of $\sigma^*$

Assume:  
1. all $\frac{w_j}{l_j}$ is distinct
2. (by renaming jobs) $\frac{w_1}{l_1} > \frac{w_2}{l_2} > ... > \frac{w_n}{l_m}$

Thus:  
greedy scheduler $\sigma$ is just $1,2,3,...,n$

Thus:  
if optimal scheduler $\sigma^* \neq \sigma$, then there are consecutive jobs $i, j$ with $i > j$

Thought Experiment:  
suppose we **exchage** order of $i, j$ in $\sigma^*$ (leaving other jobs unchanged)

![Image](https://i.imgur.com/JUWd8gY.png)

Question:  
what is the effect of exchaning on the completion times of:
1. job $k$ other that $i, j$: **uneffected**
2. job $i$: **goes up**  $l_j$
3. job $j$: **goes down** $l_i$

Upshot:  
1. cost of exchange $w_il_j$
2. benefit of exchange $w_jl_i$

Note:  
$i > j$ =>  
$\frac{w_i}{l_i} < \frac{w_j}{l_j}$ =>  
$w_il_j < w_jl_i$ => cost < benefit

**swap improves $\sigma^*$, contradicts optimality of $\sigma^*$, QED**

延伸：  
如果$\frac{w_i}{l_i}$可以相等於$\frac{w_j}{l_j}$ (有tie的情況)

證明基本上都相同  
$i > j$ =>  
$\frac{w_i}{l_i} \leq \frac{w_j}{l_j}$ =>  
$w_il_j \leq w_jl_i$ => cost $\leq$ benefit

after at most $C_2^n$ such exchanges, can transform $\sigma^*$ into $\sigma$ =>  
$\sigma$ at least as good as $\sigma^*$ =>  
greedy 也是optimal的一種 QED!

## Minimum Spanning Tree
connect a bunch of points together as cheaply as possible

Applications:  
clustering, networking

Blazingly fast greedy algorithms ($O(m\log n)$):  
1. Prim's algorithm
2. Kruskal's algorithm (MST)

### Problem Definition
Input:  
undirected graph $G=(V, E)$, adjacency list representation and a cost $c_e$ for each edge $e \in E$

Output:  
minimum cost tree $T\subset E$ that spans all vertices  
- $T$ has no cycles
- the subgraph $(V, T)$ is connected

Assumption:  
1. input graph $G$ is connected
    - 不然就沒有spanning tree (沒辦法span all vertices)
    - 很容易檢查 (depth-first search)
2. edge costs are distinct
    - Prim + Kruskal remain correct with ties
    - 正確性不容易證明 (跳過)

### Prim's MST Algorithm
跟Dijkstra's Shortest Path Algorithm很相似，但是Dijkstra是要找$A[v] + l_{vw}$ (Dijkstra's greedy criterion)，每次找的$l_{vw}$是以source vertex為根源，找到整條路徑cost最低的。  
相對的Prim's MST Algorithm每次只找所有可選的edge中，cost最小的，並沒有source vertex的概念。

Example 從右上開始:  
![Image](https://i.imgur.com/K0DgEbM.png)

Pseudocode:  
```
- init X = {s}  (s為隨機選的vertex)
- T = {}  (一開始的spanning tree沒有任何vertex)
- while X != U:
    - let e = (u, v) be the cheapest edge of G with u in X, v not in X
    - add e to T
    - add v to X
```

### The Correctness of Prim's Algorithm
Theorem:  
Prim's algorithm always compute an MST.

Part I:  
compute a spanning tree $T^*$

Part II:  
$T^*$ is an MST (cut property)

