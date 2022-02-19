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
