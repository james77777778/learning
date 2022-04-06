---
tags: algorithms, notes
---
Algorithm (Huffman codes, Dynamic Programming)
===
## Huffman codes
假設要對英文字母編碼，直覺想到可以用固定的5個bits編碼，但是能不能做更好？  
若是有些英文字母出現較頻繁，或許可以用不同長度的編碼。

### Prefix-Free Codes
Problem:  
with variable-length codes, not clear where 1 character ends and the next 1 begins

Solution:  
prefix-free codes, make sure that for every pair $i, j \in \Sigma$, neither of the encodings $f(i), f(j)$ is a prefix of the other

Example:  
$\{0, 10, 110, 111\}$

![Image](https://i.imgur.com/MoM5KOe.png)

### Prefix-Free Codes as Trees
In general:  
- left child edges: 0, right child edges: 1
- for each $i \in \Sigma$, exactly 1 node labeled $i$
- encoding of $i \in \Sigma$ <-> bits along path from root to the node $i$
- prefix-free <-> labelled nodes = the leaves

![Image](https://i.imgur.com/Cw5l8eU.png)

Note:  
encoding length of $i \in \Sigma$ = depth of $i$ in tree

### Problem Definition
Input:  
probability $p_i$ for each character $i \in \Sigma$

Notation:  
if $T$ = tree with leaves <-> symbols of $\Sigma$, then $L(T)=\Sigma_{i\in Sigma}p_i - \text{[depth of i in T]}$  
($L(T)$ = average encoding length)

Example:  
根據前面的例子，  
if $P_A=0.6, P_B=0.25, P_C=0.1, P_D=0.05$, then $L(T) = 1.55$

Output:  
a binary tree $T$ minimizing the average encoding length $L(T)$

### A Greedy Algorithm
Question:  
what's a principled approach for building a tree with leaves <-> symbols of $\Sigma$?

Natural but suboptimal idea:  
top-down / divide + conquer  
- partition $\Sigma$ into $\Sigma_1, \Sigma_2$, each with $\approx 50\%$ of total frequency
- recursively compute $T_1$ for $\Sigma_1$, $T_2$ for $\Sigma_2$

#### Huffman's (optimal) idea:  
- build tree bottom-up
- using successive merges

Question:  
which pair of symbols is **safe** to merge?

Observation:  
final encoding length of $i\in \Sigma =$ number of merges its subtree endures 忍受

![Image](https://i.imgur.com/SdsPd5Q.png)

#### How to recurse?  
Suppose:  
1st iteration of algorithm merges symbols $a, b$

Idea:  
replace the symbols $a, b$ by a new **meta-symbol** $ab$  
the frequency $P_{ab} = P_a + P_b$ 

#### Huffman's Algorithm
```
If |Sigma| = 2 return

Let a,b in Sigma have the smallest frequencies
Let Sigma' = Sigma with a,b replaced by new symbol ab
Define P_ab = P_a + P_b
Recursively compute T'
Expand T' to a tree T with leaves
Return T
```
![Image](https://i.imgur.com/KuSAy1I.png)

### Examples
從最小的frequency開始merge  
![Image](https://i.imgur.com/hROqifw.png)

另一個例子：  
![Image](https://i.imgur.com/xSA7NBh.png)  
![Image](https://i.imgur.com/769ohZ8.png)  
![Image](https://i.imgur.com/Kzz7se1.png)  
- A: 000
- B: 0010
- C:0011
- D: 01
- E: 10
- F: 11

### Correctness of Huffman's Algorithm
Theorem:  
Huffman's algorithm computes a binary tree (with leaves is the symbols of $\Sigma$) that minimizes the average encoding length:  
$L(T)=\Sigma_{i\in \Sigma}p_i [\text{depth of leaf i in T}]$

Proof:  
by induction on $n=|\Sigma|$ (assume $n \geq 2$)
- Base case: when $n=2$, algorithm outpus the optimal tree (1 bit per symbol)
- Induction step: fix input with $n=|\Sigma| > 2$
- By induction hypothesis: algorithm solves smaller subproblem optimally

Inductive step:  
Let $\Sigma' = \Sigma$ with $a, b$ replaced by meta-symbol $ab$.  
Define $p_{ab}=p_a+p_b$

![Image](https://i.imgur.com/FlOZETC.png)

Important:  
for every such pair $T', T$,  
($T$為merge前，$a,b$還分開的狀態；$T'$為merge後，$a,b$成為$ab$)  
$L(T) - L(T') = p_a(d+1) + p_b(d+1) - (p_a+p_b) d = p_a + p_b$  
indepent of $T, T'$!!

Key lemma:  
there is an optimal tree (for $\Sigma$) in $X_{ab}$ (i.e., $a, b$ were **safe** to merge)

Intuition:  
can make an optimal tree better by pushing $a, b$ as deep as possible (since $a, b$ have smallest frequencies)

Proof of Key Lemma:  
By exchange argument. Let $T^*$ be any tree that minimizes $L(T)$ for $\Sigma$  
Let $x, y$ be siblings at the deepest level of $T^*$

The exchange:  
obtain $\hat{T}$ from $T^*$ by swapping lables $a, x$, $b, y$

![Image](https://i.imgur.com/lBcOqB7.png)

Note:  
$\hat{T} \in X_{ab}$ (by choice of $x, y$)

To finish:  
will show that $L(\hat{T}) \leq L(T^*)$ ($\hat{T}$ also optimal, complete proof)

Reason:  
$L(T^*) - L(\hat{T}) =$  
$(p_x - p_a)[\text{depth of x in T* - depth of a in T*}] +$  
$(p_y-p_b)[\text{depth of y in T* - depth of b in T*}]$

$L(T^*) - L(\hat{T}) \geq 0$

QED!

### Running Time
Naive implementation:  
$O(n^2)$ time where $n=|\Sigma|$

Speed up:  
use a heap!  
keys = frequencies  
=> $O(n\log n)$

Even faster:  
sorting + $O(n)$ additional work  
manage (meta-)symbols using two queues

## Dynamic Programming
### Problem Statement
Input:  
a path graph $G=(V, E)$ with nonnegative weights on vertices

![Image](https://i.imgur.com/njdCCsj.png)

Desired output:  
subset of nonadjacent vertices (an independent set) of maximum total weight

Next:  
iterate through our algorithm design priciples

### A Greedy Approach
iteratively choose the max-weight vertex not adjacent to any previously chosen vertex

![Image](https://i.imgur.com/h3IrQ9Y.png)

真正最大值應該為$4+4=8$，但是greedy的作法只能得到$5+1=6$  
在此問題下，Greedy沒辦法得到最佳解

### A Divide & Conquer Approach
recursively compute the max-weight IS of 1st half, for 2nd half, then combine the solutions

![Image](https://i.imgur.com/JytXSy4.png)

what if recursive sub-solutions conflict?  
=> 沒辦法找到快速的解法

### Optimal Substructure
Critical step:  
reason about structure of an optimal solution (in terms of optimal solutions of smaller subproblems)

Motivation:  
this thought experiment narrows down the set of candidates for the optimal solution; can search through the small set using brute-force search

Notation:  
let $S \subseteq U$ be a max-weight independent set (IS).  
let $v_n$ = last vertex of path

#### A Case Analysis
Case 1:  
suppose $v_n \not \in S$, let $G'=G$ with $v_n$ deleted.  
Note: $S$ also an IS of $G'$  
Note: $S$ must be a max-weight IS of $G'$ if $S^*$ was better, it would also be better than $S \in G$ (矛盾)

Case 2:  
suppose $v_n \in S$   
Note: previous vertex $v_{n-1} \not \in S$, let $G''=G$ with $v_{n-1}, v_n$ deleted.  
Note: $S - \{v_n\}$ is an IS of $G''$  
Note: must in fact be a max-weight IS of $G''$ if $S^*$ is better than $S \in G''$, then $S^* \cup \{v_n\}$ is better than $S \in G$ (矛盾)