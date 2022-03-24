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

## Clustering
