---
tags: algorithms, notes
---
Algorithm (Kruskal's MST Algorithm, Clustering)
===
## Kruskal's MST Algorithm
### Pseudocode
```
- sort edges in order of increasing cost
(rename edges 1, 2, ..., m so that c_1 < c_2 < ... < c_m)
- T = {}
- for i = 1 to m
    - if T union {i} has no cycles
        - add i to T
- return T
```

![Image](https://i.imgur.com/W5c7TmA.png)

### Correctness of Kruskal (Part I)
Theorem:  
Kruskal's algorithm is correct

Proof:  
Let $T^* = $ output of Kruskal's algorithm on input graph $G$  
1. clearly $T^*$ has no cycles
2. $T^*$ is connected  
    - By Empty Cut lemma, only need to show that $T^*$ crosses every cut  
    - Fix a cut $(A, B)$. Since $G$ connected, at least one of its edges crosses $(A, B)$

Key point:  
Kruskal will include first edge crossing $(A, B)$ that is sees

![Image](https://i.imgur.com/HKs98Y2.png)

3. every edge of $T^*$ justified by the Cut Property (implies $T^*$ is the MST)  
    Reason of 3:  
    Consider iteration where edge $(u, v)$ added to current set $T$  
    Since $T \cup \{(u, v)\}$ has no cycle, $T$ has no $u-v$ path  
    => $\exists$ empty cut $(A, B)$ separating $u, v$  
    => by 2, no edges crossing $(A, B)$ were previously considered by Kruskal  
    => $(u, v)$ is the first (and cheapest!) edge crossing $(A, B)$  
    => $(u, v)$ justified by the Cut Property

![Image](https://i.imgur.com/efueAW5.png)

QED!

### Implementing Kruskal's Algorithm via Union-Find
```
- sort edges in order of increasing cost
(rename edges 1, 2, ..., m so that c_1 < c_2 < ... < c_m)
- T = {}
- for i = 1 to m -> O(m) iterations
    - if T union {i} has no cycles -> O(n) time to check for cycle (BFS/DFS)
        - add i to T
- return T
```

Running time of straightforward implementation:  
$m$: number of edges  
$n$: number of vertices  
$O(m\log n) + O(mn) = O(mn)$

Plan:  
data structure for $O(1)$ cycle checks  
=> $O(m\log n)$

### Union-Find Data Structure
maintain partition of a set of objects

![Image](https://i.imgur.com/2x4jK6x.png)

- FIND(x): return name of group that $x$ belongs to
- UNION(C_i, C_j): fuse groups $C_i$ and $C_j$ into a single one.

Why useful for Kruskal's algorithm?  
- objects = vertices  
- groups = connected components w.r.t currently chosen edges $T$
- adding new edge $(u, v)$ to $T$ <=> fusing connected component of $u, v$

#### Basics
![Image](https://i.imgur.com/92JY1g3.png)  
可以看到：
- $v, w$都有pointer指向$u$
- $y, z$都有pointer指向$x$

Invariant:  
each vertex points to the leader of its component ("name" of a component inherited from leader vertex)

Key point:  
given edge $(u, v)$, can check if $u, v$ already in same component in $O(1)$ time  
(if and only if leader pointers of $u, v$ match, FIND(u) == FIND(v))  
=> $O(1)$-time cycle checks!

#### Maintaining the Invariant:  
when new edge $(u, v)$ added to $T$, connected components of $u, v$ merge.  

Question:  
how many leader pointer updates are needed to restore the invariant in the worst case?  
$\Theta(n)$, when merging two components with $\frac{n}{2}$ vertices each

Idea 2:  
when two connected components merge, smaller one inherit the leader of the larger one

Question:  
how many leader pointer updates are needed to restore the invariant in the worst case?  
$\Theta(n)$, 理由跟前面相同

#### Updating Leader Pointers
But:  
how many times does a single vertex have its leader pointer updated over the course of Kruskal's algorithm (in the worst case)?  
$\Theta(\log n)$, every time $v$'s leader pointer gets updated, population of its component at least doubles.  
=> can only happen $\leq \log_2n$ times

#### Running Time of Fast Implementation
- $O(m\log n)$ for sorting
- $O(m)$ for cycle checks ($O(1)$ per iteration)
- $O(n\log n)$ overall for leader pointer updates

=> $O(m\log n)$ total!

### State-of-the-Art MST Algorithms
Question:  
can we do better than $O(m\log n)$? (Prim, Kruskal)

Answer:  
yes!  
- $O(m)$ randomized algorithm (Karger-Klein-Tarjan, JACM 1995)
- $O(m\alpha(n))$ deterministic (Chazelle JOTCM 2000)  
    $\alpha(n)$ inverse Ackermann function, grows much slower than $\log n$ = number of times you can apply $\log$ to $n$ until result drops below $1$

## Clustering
Informal goal:  
given $n$ points, classify into "coherent groups" (unsupervised learning)

Assumptions:  
1. as input, given a (dis)similarity measure: a distance $d(p, q)$ between each point pair
2. symmetric (i.e., $d(p, q) = d(q, p)$)

Examples:  
Euclidean distance, genome similarity, etc.

### Max-Spacing k-Clusterings
Assume:  
we know $k =$ number of clusters desired  
(all points $p, q$ separated if they're assigned to different clusters)

Definition:  
the spacing of a k-clustering is $\min_{\text{separated p,q}} d(p,q)$ (the bigger, the better)

Problem statement:  
given a distance measure $d, k$, compute the k-clustering with maximum spacing

### Greedy Algorithm
![Image](https://i.imgur.com/PqDrS9c.png)

```
- initially, each point in a separate cluster
- repeat until only k clusters:
    - let p, q = closest pair of separated points
    - merge the clusters containing p, q into a single cluster
```

Note:  
just like Kruskal's MST algorithm, but stopped early  
=> single-link clustering

### Correctness of Greedy Algorithm
Theorem:  
single-link clustering finds the max-spacing k-clustering

Proof:  
let $C_1, ..., C_k$ = greedy clustering with spacing $S$  
let $\hat{C_1}, ..., \hat{C_k}$ = arbitrary other clustering

Need to show:  
spacing of $\hat{C_1}, ..., \hat{C_k}$ is $\leq S$

#### Proof
Case 1:  
$\hat{C_i}$'s are the same as the $C_i$'s (may be after ranaming) => has the same spacing $S$

Case 2:  
otherwise, can find a point pair $p, q$ such that  
1. $p, q$ in the same greedy cluster $C_i$
2. $p, q$ in different clusters $\hat{C_i}, \hat{C_j}$

Property of greedy algorithm:  
if two points $x, y$ directly merged at some point, then $d(x, y) \leq S$  
(distance between merged point pairs only goes up)

Tricky case:  
$p, q$ indirectly merged through multiple direct merges

![Image](https://i.imgur.com/im2F9Lx.png)

let $p, q_1, ..., q_e, q$ be the path of direct greedy merges connecting $p, q$

Key point:  
since $p \in \hat{C_i}$ and $q \not \in \hat{C_i}$, $\exists$ consecutive pair $a_j, a_{j+1}$ with $a_j \in \hat{C_i}$, $a_{j+1} \not \in \hat{C_i}$  
=> $S \geq d(a_j, a_{j+1}) \geq \text{spacing of } \hat{C_1}, ..., \hat{C_k}$

QED!
