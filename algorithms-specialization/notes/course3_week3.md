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

## Dynamic Programming
