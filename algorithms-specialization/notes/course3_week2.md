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

### Correctness of Kruskal (Part II)


## Clustering
