---
tags: algorithms, notes
---
Algorithm (Graph Search, Topological Sort, Strongly Connected Component)
===
## Generic Graph Search
Goals:  
1. find everying findable from a given start vertex
2. don't explore anyting twice

```
Generic Algorithm (given graph G, vertext s)  
- initially s explored, all other vertices unexplored
- while possible:
    - choose an edge (u, v) with u explored and v unexplored
    - mark v explored
```

Claim:  
at end of the algorithm, $v$ explored => $G$ has a path from $s$ to $v$

Proof:  
- (=>) easy induction on number of iterations
- (<=) By contradiction. Suppose $G$ has a path $P$ from $s$ to $v$:
    ![Image](https://i.imgur.com/AJoco6c.png)
    but $v$ unexplored at end of the algorithm. Then $\exists (u, w) \in P$ with $u$ explored and $w$ unexplored.
    Contradiction. QED!

## BFS vs. DFS
Note:  
how to choose among the possibly many **frontier** edges?

## Breadth-First Search (BFS)  
- explore nodes in **layers**
- can compute shortest paths
- can compute connected components of an undirected graph
- $O(m+n)$ time using a queue (FIFO)

### Pseudocode
```
BFS(graph G, start vertex s)
- mark s as explored
- let Q queue data structure (FIFO), initialized with s
- while Q not empty:
    - remove the first node of Q, call it v
    - for each edge (v, w):
        - if w unexplored
            - mark w as explored
            - add w to Q (at the end)

```

![Image](https://i.imgur.com/AtdGoeu.png)

### Basic Properties
- Claim #1:  
    at the end of BFS, $v$ explored <=> $G$ has a path from $s$ and $v$  
    Reason:  
    special case of the generic algorithm
- Claim #2:
    running time of main while loop = $O(n+m)$

### Application: Shortest Paths
(DFS無法找到shortest paths)

Goal:  
compute $dist(v)$, the fewest number of edges on a path from $s$ to $v$

Extra code:  
```
- initialize dist(v) = 0 if v = s / dist(v) = +inf if v != s
- when considering edge (v, w):
    - if w unexplored, then set dist(w) = dist(v) + 1
```

Claim:  
at termination, $dist(v) = i$ <=> $v$ in $i^{\text{th}}$ layer

Proof idea:  
every layer-$i$ node $w$ is added to $Q$ by a layer-$(i-1)$ node $v$ via the edge $(v, w)$

### Application: Undirected Connectivity
Let $G=(V, E)$ be an undirected graph

Connected components = the **pieces** of $G$

Formal definition:  
equivalence classes of the relation $u \sim v$ <=> $\exists u-v$ path in $G$

Goal:  
compute all connected components

To compute all components (undirected case)
```
- all nodes unexplored (assume label from 1 to n)
- for i=1 to n
    - if i not yet explored
        - BFS(G, i)
```
![Image](https://i.imgur.com/ETYKVKE.png)

Running time:  
$O(m+n)$

## Depth-First Search (DFS)
- explore aggressively like a maze, backtrack only when necessary
- compute topological ordering of directed acyclic graph
- compute strongly connected components of directed graphs
- $O(m+n)$ time using a stack (LIFO)

![Image](https://i.imgur.com/EwYkfxX.png)

### Pseudocode
Recursive version:  
```
DFS(graph G, start vertex s)
- mark s as explored
- for every edge (s, v):
    - if v unexplored
        - DFS(G, v)
```

### Basic Properties
跟BFS完全一樣

- Claim #1:  
    at the end of DFS, $v$ explored <=> $G$ has a path from $s$ and $v$  
    Reason:  
    special case of the generic algorithm
- Claim #2:
    running time of main while loop = $O(n+m)$

### Application: Topological Sort
Definition:  
a topological ordering of a directed graph G is a labelling $f$ of $G$'s nodes such that:  
1. the $f(v)$'s are the set ${1, 2, ..., n}$
2. $(u, v) \in G$ => $f(u) < f(v)$

![Image](https://i.imgur.com/cCnhNGX.png)

Note:  
$G$ has directed cycle => no topological ordering  
不能具有有向的迴圈，不然會造成無窮迴圈

Motivation:  
要排列一系列的tasks且有constrains時 (例如修課順序)

**Straightforward Solution:**  
Note:  
every directed acyclic graph has a **sink vertex**

Compute topological ordering:  
```
- let v be a sink vertex of G
- set f(v) = n
- recruse on G - {v}
```
![Image](https://i.imgur.com/FFFZHPm.png)

**Topological Sort via DFS (Slick 光滑的)**
```
DFS-Loop(graph G)
- mark all nodes unexplored
- current_label = n (keep track of ordering)
- for each vertex v in G:
    - if v not yet explored
        - DFS(G, v)
```
```
DFS(graph G, start vertex s)
- mark s as explored
- for every edge (s, v):
    - if v unexplored
        - DFS(G, v)
- set f(s) = current_label
- current_label--
```

Running Time:  
$O(m+n)$  
($O(1)$ per node & $O(1)$ per edge)

