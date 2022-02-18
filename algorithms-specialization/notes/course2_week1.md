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

## Strongly Connected Components
Definition:  
the strongly connected components (SCCs) of a directed graph $G$ are the equivalence classes of the relation  
$u \sim v$ <=> $\exists \text{ path } u-v$ **and** $\text{ a path } v-u$ in $G$

![Image](https://i.imgur.com/J4teDrx.png)

### Why Depth-First Search?
![Image](https://i.imgur.com/bEJAEUv.png)

如果從紅色點開始，有機會找到SCC。但是如果從綠色點開始，則會找到錯誤的SCC。  
使用DFS的**起點**會影響結果

### Kosaraju's Two-Pass Algorithm
Theorem:  
can compute SCCs in $O(m+n)$ time

Algorithm: (given directed graph)  
```
- let G^rev = G with all arcs reversed
- run DFS-Loop on G^rev (goal: compute "magical ordering" of nodes)
    - let f(v) = "finishing time" of each v in V
- run DFS-Loop on G (goal: discover the SCCs 1-by-1)
    - processing nodes in decreasing order of fininshing times
```

DFS-Loop
```
DFS-Loop(graph G)
- global variable t=0 (# of nodes processed so far)
- global variable s=NULL (current source vertex)
- label nodes 1 to n
- For i=n to 1
    - If i not yet explored
        - s = i
        - DFS(G, i)
```

```
DFS(graph G, node i)
- mark i as explored (for rest of DFS-Loop)
- set leader(i) = nodes
- For each arc (i, j) in G:
    - If j not yet explored:
        - DFS(G, j)
- t++
- set f(i) = t
```

Example:  
![Image](https://i.imgur.com/7KY7gpv.png)

第一次的pass，先將arcs反轉後從node最大開始做DFS：  
- 從node=9開始，走9-6-3之後死路，所以$f(3)=1$，因為第一個結束的。  
- 再來從6開始走6-8-2-5之後死路，所以$f(5)=2$，依此類推。  
- ...
- 最後會得到所有的finishing time $f(v)$

![Image](https://i.imgur.com/iuR5svV.png)

第二次的pass，恢復原本的arcs，並從$f(v)$最大的開始做DFS：  
- 9-7-8後死路，找到第一個SCC
- 6-1-5後死路，找到第二個SCC
- 4-2-3後死路，找到第三個SCC
- 結束，找到所有的SCCs

Running Time:  
兩次的DFS = $O(m+n)$

### 證明演算法 Observation
Claim:  
the SCCs of a directed graph induce an acyclic "meta-graph":  
- meta-nodes = the SCCs ($C_1, ..., C_k$ of $G$)
- $\exists \text{ arc } C \text{ -> } \hat{C}$ <=> $\exists \text{ arc } (i, j) \in G$ with $i\in C, j\in \hat{C}$

![Image](https://i.imgur.com/i0k2Psi.png)

Why acyclic?  
a cycle of SCCs would collapse into one

對於$G$和$G^{\text{rev}}$來說，SCCs是完全相同的

### Key Lemma
Lemma (引理):  
consider two "adjacent" SCCs in $G$  
![Image](https://i.imgur.com/GvyA1YB.png)

let $f(v)$ = finishing times of DFS-Loop in $G^{\text{rev}}$  
then $max_{v \in C_1} f(v) < max_{v \in C_2} f(v)$

Corollary (推論):  
maximum f-value of $G$ must lie in a "sink SCC"  
![Image](https://i.imgur.com/VdHUCMh.png)

### Correctness Intuition
By Corollary:  
2nd pass of DFS-Loop beings somewhere in a sink SCC $C^*$  
=> first call to DFS discover $C^*$ and nothing else?  
=> rest of DFS-Loop like recursing on $G$ with $C^*$ deleted  
(starts in a sink node of $G-C^*$)  
=> successive calls to $\text{DFS}(G, i)$ "peal off 剝離" the SCCs 1-by-1  
(in reverse topological order of the "meta-graph" of SCCs)

### Proof of Key Lemma
![Image](https://i.imgur.com/1R0qnqX.png)

## Problems
- ![Image](https://i.imgur.com/D7ygCyy.png)
    [https://andrew-exercise.blogspot.com/2015/11/algorithms-design-and-analysis-part-1_5.html](https://andrew-exercise.blogspot.com/2015/11/algorithms-design-and-analysis-part-1_5.html)
- ![Image](https://i.imgur.com/e5yBj5y.png)
    [https://andrew-exercise.blogspot.com/2015/11/algorithms-design-and-analysis-part-1_30.html](https://andrew-exercise.blogspot.com/2015/11/algorithms-design-and-analysis-part-1_30.html)
- ![Image](https://i.imgur.com/NctXCxG.png)
    任何情況都有可能發生，所以選(4) 
    - 例如1->2->3有3個SCCs，加上3->1則會變成只有1個SCCs
    - 例如1->2->3有3個SCCs，加上1->3則還是有3個SCCs