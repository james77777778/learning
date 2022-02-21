---
tags: algorithms, notes
---
Algorithm (Dijkstra's Shortest-path)
===
## Single-Source Shortest Paths
Input:  
directed graph $G=(V, E)$ ($m=|E|, n=|V|$)
- each edge has nonnegative length $l_e$
- source vertex $s$

Output:  
for each $v \in V$, compute $L(v)$ = length of a shortest $s-v$ path in $G

![Image](https://i.imgur.com/OiQOhl7.png)

Assumptions:  
1. $\forall v \in V, \exists s-v \text{ path}$
2. $l_e \geq 0, \forall e \in E$

![Image](https://i.imgur.com/VvZm6cX.png)

### Why Another Shortest-Path Algorithm?
Question:  
doesn't BFS already compute shortest paths in linear time?

Answer:  
yes, IF $l_e = 1$ for every edge $e$

因為此問題的edge權重可能不同，所以BFS找出來的最短路徑會是錯誤的！BFS只能在每個edge權重相同時才會對！

## Dijkstra's Algorithm
```
Initialize
- X = {s}  (vertices processed so far)
- A[s] = 0  (computed shortest path distances)
- B[s] = empty path  (computed shortest paths)

Main Loop
- While X != V:
    - among all edges (v, w) with v in X, w not in X
    - pick the one that minimizes
        A[v] + l_vw (Dijkstra's greedy criterion)
        假設找到的edge為(v*, w*)
    - add w* to X
    - set A[w*] = A[v*] + l_v*w*
    - set B[w*] = B[v*] union (v*, w*)
```

### Example
- 正常的graph，都是非負的edge  
    ![Image](https://i.imgur.com/dkdjka6.png)  
    慢慢擴大$X$的範圍，每次都加一個greedy的edge  
    最後得到$A[t]=6, B[t]=s-v-w-t$

- 若有負的edge  
    ![Image](https://i.imgur.com/kqNnedx.png)  
    事實上$s-v-t$會更短，因為$A[t]=-4$

### Correctness Claim & Proof
Theorem:  
$\forall v \in V, A[v] = L(v)$  
- $A[v]$ Dijkstra's algorithm computes
- $L(v)$ true shortest path distance from $s$ to $v$

Proof:  
Inductive step:  
for all $v \in X, A[v] = L(v)$ and $B[v]$ is a true shortest $s-v$ path in $G$

In current iteration:  
we pick an edge $(v^*, w^*)$ and we add $w^*$ to $X$  
we set $B[w^*] = A[v^*] \cup (v^*, w^*)$

Also:  
$A[w^*] = A[v^*] + l_{v^*w^*} = L(v^*) + l_{v^*w^*}$

To finish proof:  
need to show that every $s-w^*$ path has length $\geq L(v^*) + l_{v^*w^*}$

![Image](https://i.imgur.com/ydvCtt9.png)

So:  
let $P = \text{any } s-w^* \text{ path}$. Must **cross the frontier** and so has the form:  
![Image](https://i.imgur.com/nGSmxnY.png)

藉由歸納法的inductive step可以保證$s-y$一定是真實的最短路徑  
path $P$的總長一定至少有$A[y] + C_{yz}$，藉由greedy法則可以保證$A[v^*] + l_{v^*w^*} \leq A[y] + l_{yz} \leq length(P)$

## Dijkstra's Algorithm: Implementation & Running Time
![Image](https://i.imgur.com/AWLBsza.png)

- $(n-1)$ iterations of while loop
- $O(m)$ work per iteration

利用Heap可以加速演算法！

### Heap Operations
Recall:  
Insert, Extract-Min in $O(\log n)$ time

- perfectly balanced binary tree (height $\approx \log_2 n$)
- heap property: at every node, key $\leq$ children's keys
- **Extract-Min** by swapping up last leaf, bubbling down
- **Insert** via bubbling up

Also:  
will need ability to delete from middle of heap

### Two Invariants
1. elements in heap = vertices of $V-X$  
    ![Image](https://i.imgur.com/Zws1ETG.png)
2. for $v \not \in X$, key[v] = smallest Dijkstra greedy score of an edge $(u, v) \in E$ with $u \in X$  
    ![Image](https://i.imgur.com/vEmi3S2.png)

如果能維持heap的2個不變性，則Extract-Min就可以得到Dijkstra's演算法中所需的$w^*$，並且加到$X$中

### Maintaining the Invariants
第1個invariant很容易維持

To maintain Invariant 2:  
當有新的$X$出現時(加入$w$後)，frontier vertices會改變。  
![Image](https://i.imgur.com/deOnb2v.png)

```
When w extracted from heap
- for each edge (w, v) in E:
    - if v in (V-X), means in heap:
        - delete v from heap
        - recompute key[v] = min(key[v], A[w]+l_wv)
        - re-Insert v into heap
```

### Running Time Analysis
Dominated by heap operations ($O(\log n)$ each)
- $(n-1)$ Extract-Mins
- each edge $(v, w)$ triggers at most 1 Delete/Insert combo (if $v$ added to $X$ first)

So:  
the number of heap operations is $O(n+m) = O(m)$  
(假設graph是weakly connected)

So:  
running time = $O(m\log n)$

基本上跟sorting在同一個級距，非常快！
