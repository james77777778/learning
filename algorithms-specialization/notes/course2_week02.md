---
tags: algorithms, notes
---
Algorithm (Counting Inversions, Strassen's Subcubic Matrix Multiplication)
===
## The Divide and Conquer Paradigm
1. Divde into smaller subproblems
2. Conquer via recursive calls
3. Combine solutions of subproblems into one for the original problem

### Inversion 倒置 The Problem
input: array $A$ containing the numbers $1, 2, 3,..., n$ in some arbitrary order

output: number of inversions = number of pairs $(i, j)$ of array indices with $i<j$ and $A[i] > A[j]$

ex. (1, 3, 5, 2, 4, 6)
![](https://i.imgur.com/ns6Hv1c.png)

motivation: numerical similarity measure between two ranked lists

#### Questions
![](https://i.imgur.com/llYA3vl.png)
solution: ordered list (6, 5, 4, 3, 2, 1)

#### High-Level Approach
brute-force: $O(n^2)$ time  
key idea #1: Divide and Conquer  
![](https://i.imgur.com/fl4JoRl.png)

能不能做得更好？ 可以  
利用Divide + Conquer  
左右兩邊可以利用recursive的方式解，而最後split則需要特別演算法處理

#### High-Level Algorithm
![](https://i.imgur.com/3cXOE19.png)

主要目標是將CountSplitInv壓在linear time ($O(n)$)，若做得到則整個演算法可以在$nlogn$時間內 (like merge sort)

利用Merge Sort特性：
- Count變成Sort-and-Count
- CountSplitInv變成Merge-and-CountSplitInv

為何Merge Sort可以拿來Count Inversions?  
思考一下Merge subroutine，會發現若第二部份比第一部份大，則能找到split inversions

#### Questions
![](https://i.imgur.com/VxzgRKZ.png)

#### Merge Subroutine Example
consider merging B:(1, 3, 5) and C:(2, 4, 6)

output: D: (1, 2, )
=> when 2 copied to output, discover the split inversions (3, 2) and (5, 2)

output: (1, 2, 3, 4, )
=> when 4 copied to output discover (5, 4)

output (1, 2, 3, 4, 5, 6)
finished.

#### General Claim
the split inversions involving an element y of the 2nd array C are precisely the numbers left in the 1st array B when y is copied to the output D

proof:
let $x$ be an element of the 1st array B.  
(1) if $x$ copied to output D before $y$, then $x < y$ => no inversion involving $x, y$  
(2) if $y$ copied to output D before $x$, then $y < x$ => $x, y$ are a spilt inversion  

#### Merge_and_CountSplitInv
![Image](https://i.imgur.com/cDjYW9V.png)

- 當要merge 2個已排序好的subarrays時，持續記錄total number of split inversions
- 如果有2nd array C要複製到output D時，增加split inversion數量，增加量等同目前在1st array B的元素個數

runtime of subroutine:  
$O(n) + O(n) = O(n)$  
(merge + running total)  
此加法有點瑕疵，因為如果加了n次$O(n)$則沒辦法簡化，不過這個演算法只有2次$O(n)$，故可以簡化  
=> Sort_and_Count runs in $O(nlogn)$ time

### Strassen's Subcubic Matrix Multiplication
#### Matrix Multiplication Problem
![Image](https://i.imgur.com/M0k76gM.png)

where $z_{ij} = (\text{ith row of x}) * (\text{jth col of y})$  
$= \Sigma_{k=1}^n(x_{ik}*y_{kj})$

#### Example (n=2)
![Image](https://i.imgur.com/vfnwqZo.png)

asymptotic running time of the straightforward iterative algorithm:  
$\Theta(n^3)$

這邊的n代表矩陣的大小為nxn

#### Applying  Divide and Conquer
![Image](https://i.imgur.com/9vv2679.png)

#### Strassen's Algorithm (1969)
1. recursively compute only $f$ (cleverly chosen) products
2. do the necessary (clever) additions + subtractions (still $\Theta(n^2)$ time)

Fact: better than cubic time! (Master Method lecture)


$X=\begin{pmatrix} A & B \\ C & D \\ \end{pmatrix}$

$Y=\begin{pmatrix} E & F \\ G & H \\ \end{pmatrix}$

The Seven Products:
- $P_1=A(F-H)$
- $P_2=(A+B)H$
- $P_3=(C+D)E$
- $P_4=D(G-E)$
- $P_5=(A+D)(E+H)$
- $P_6=(B-D)(G+H)$
- $P_7=(A-C)(E+F)$

不需要8次乘法，故減少了1次，將演算法複雜度降到cubic time以下

Claim:  
$XY=\begin{pmatrix} AE+BG & AF+BH \\ CE+DG & CF+DH \\ \end{pmatrix}=\begin{pmatrix} P_5+P_4-P_2+P_6 & P_1+P_2 \\ P_3+P_4 & P_1+P_5-P_3-P_7 \\ \end{pmatrix}$

Proof:  
自己代數運算即可

### Closest Pair $O(nlogn)$
#### The Closest Pair Problem
Input:  
a set $P={p_1, ..., p_n}$ of n points in the plane ($R^2$)  
(distinct x-coordinates, y-coordinates for convience)

Notation:  
$d(p_i, p_j)$ = Euclidean distance  
So if $p_i=(x_i, y_i)$ and $p_j=(x_j, y_j)$, then $d(p_i, p_j)=\sqrt{(x_i-y_i)^2+(x_j-y_j)^2}$

Output:  
a pair $p^*, q^+\in P$ of distinct points that minimize $d(p, q)$

#### Brute-force search
Takes $O(n^2)$ time

#### 1-D version of Closest Pair:
1. sort points ($O(nlogn)$)
2. return closest pair of adjacent points ($O(n)$)

Goal:  
$O(nlogn)$ time for 2-D version

#### High-Level Approach
1. make copies of points sorted by x-coor ($P_x$) and y-coor ($P_y$) ($O(nlogn)$ time)
