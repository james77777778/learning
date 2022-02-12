---
tags: algorithms, notes
---
Algorithm (Graph Search, Topological Sort, Computing Strong Components)
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


## Depth-First Search (DFS)
- explore aggressively like a maze, backtrack only when necessary
- compute topological ordering of directed acyclic graph
- compute connected components in directed graphs
- $O(m+n)$ time using a stack (LIFO)

