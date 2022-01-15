---
tags: algorithms, notes
---
Algorithm (Counting Inversions, Strassen's Subcubic Matrix Multiplication, Cloeset Pair)
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
![Image](https://i.imgur.com/vuVgqkR.png)
1. make copies of points sorted by x-coor ($P_x$) and y-coor ($P_y$) ($O(nlogn)$ time)
2. Use divide & conquer

#### ClosestPair($P_x, P_y$)
1. let $Q$ = left half of $P$, $R$ = right half of $P$. Form $Q_x, Q_y, R_x, R_y$ (takes $O(n)$ time)
2. $(p_1, q_1)$ = ClosetPair($Q_x, Q_y$)
3. $(p_2, q_2)$ = ClosetPair($R_x, R_y$)
4. $\delta=min(d(p_1, q_1), d(p_2, q_2))$ 
4. $(p_3, q_3)$ = ClosetSplitPair($P_x, P_y, \delta$)
5. return best of $(p_1, q_1), (p_2, q_2), (p_3, q_3)$

![Image](https://i.imgur.com/4ipe5Xp.png)
只有在不幸運的情況下才需要計算ClosestSplitPair

ClosetSplitPair需要$O(n)$ time

#### ClosestSplitPair($P_x, P_y, \delta$)
($\delta$是原本divide & conquer找到最小的pair的距離)  
![Image](https://i.imgur.com/ieAMYn3.png)

let $\bar{x}$ = biggest x-coordinate in left of $P$ ($O(1)$ time)  
let $S_y$ = points of $P$ with x-coordinate in $[\bar{x} - \delta, \bar{x} + \delta]$, sorted by y-coordinate ($O(n)$ time)

```
Initialize best = $\delta$, best pair = NULL
For i=1 to |Sy| - 1
    For j=1 to min(7, |Sy|-i)
        let p, q = (i)th, (i+j)th points of Sy
        If d(p, q) < best
            best pair = (p, q)
            best = d(p, q)
```
($O(n)$ time，因為for loop的迭代次數是固定量的)  
![Image](https://i.imgur.com/duPbAyO.png)

#### ClosestSplitPair($P_x, P_y, \delta$) Correctness Claim
Claim:  
let $p \in Q, q \in R$ be a split pair with $d(p, q) < \delta$

Then:  
(A) $p, q$ are members of $S_y$  
(B) $p, q$ are at most 7 positions apart in $S_y$  
(意思指如果$S_y$中有距離最短的pair則他們一定在7個距離內)

推論Corollary 1:  
If no closest pair of $P$ is a split, then ClosestSplitPair finds it.


推論Corollary 2:  
ClosestPair is correct, and runs in $O(nlogn)$ time

#### Proof of Correctness Claim (A)
因為$\bar{x}$是左半邊的最大x值，且$\delta$為左與右半邊pair的最短距離，所以如果split中有最短距離的pair，一定會在$[\bar{x} - \delta, \bar{x} + \delta]$之間。

![Image](https://i.imgur.com/ES1Uv3N.png)

#### Proof of Correctness Claim (B
key picture:  
draw $\frac{\delta}{2}\times \frac{\delta}{2}$ with center $\bar{x}$ and bottom $min(y_1, y_2)$

![Image](https://i.imgur.com/BR9YAe4.png)

引理lemma 1:  
all points of $S_y$ with y-coordinate between those of $p, q$, lie in one of 8 boxes

Proof:  
1. y-coordinates of $p, q$ differ by $< \delta$  
2. by definition of $S_y$, all have x-coordinates between $[\bar{x} - \delta, \bar{x} + \delta]$

引理lemma 2:  
At most one point of $P$ in each box.

Proof:  
By contradicition.  
如果$a, b$都在同一個box中，已知每個box一定會在同一側 ($Q, R$)，且$d(a,b) \leq \frac{\delta}{2}\sqrt{2} < \delta$  
則違反了原本的假設，因為我們已經確定$\delta$是左或右邊的最短距離

#### Final Wrap-Up
![Image](https://i.imgur.com/nxgjSaA.png)

根據lemma 1和2  
最多只會有8個點在這張圖中  
所以$S_y$中若有最短距離pair $(p, q)$，則$p, q$最多距離7  

故得證ClosesPair演算法

也可參考演算法筆記：  
[http://web.ntnu.edu.tw/~algo/Point2.html#3](http://web.ntnu.edu.tw/~algo/Point2.html#3)

### The Master Method
Cool feature:  
A "black box" for solving recurrences.

Assumption:  
All subproblems have equal size.

#### Recurrence Format
1. Base case:  
    $T(n) \leq$ a constant for all sufficiently small $n$
2. For all larger $n$:  
    $T(n) \leq aT(\frac{n}{b}) + O(n^d)$ where  
    - a = number of recursive calls ($\geq 1$)  
    - b = input size shrinkage factor ($> 1$)  
    - d = exponent in running time of "combine step" ($\geq 0$)  
    
    a, b, d independent of n

#### The Master Method
$
T(n) \leq aT(\frac{n}{b}) + O(n^d)
$

$
T(n) = 
\begin{cases}
    O(n^dlogn) & \text{if } a = b^d & \text{(case 1)}\\
    O(n^d) & \text{if } a < b^d & \text{(case 2)}\\
    O(n^{log_ba}) & \text{if } a > b^d & \text{(case 3)}
\end{cases}
$

#### Examples
1. Merge Sort:  
    $T(n) \leq 2T(\frac{n}{2}) + O(n^1)$ (case 1)  
    => $T(n) \leq O(n^dlogn) = O(nlogn)$

2. Binary Search:  
    $T(n) \leq 1T(\frac{n}{2}) + O(n^0)$ (case 1)  
    => $T(n) = O(n^dlogn) = O(logn)$

3. Normal Recursive Integer Multiplication  
    $T(n) \leq 4T(\frac{n}{2}) + O(n^1)$ (case 3)  
    => $T(n) = O(n^{log_ba}) = O(logn^{log_24}) = O(n^2)$

4. Gauss's Recursive Integer Multiplication  
    $T(n) \leq 3T(\frac{n}{2}) + O(n^1)$ (case 3)  
    => $T(n) = O(n^{log_ba}) = O(logn^{log_23}) \approx O(n^{1.59})$

5. Strassen's Matrix Multiplication  
    $T(n) \leq 7T(\frac{n}{2}) + O(n^1)$ (case 3)  
    => $T(n) = O(n^{log_ba}) = O(logn^{log_27}) \approx O(n^{2.81})$

6. 虛擬的 Fictitious Recurrence  
    $T(n) \leq 2T(\frac{n}{2}) + O(n^2)$ (case 2)  
    => $T(n) = O(n^d) = O(n^2)$

### Problem Set #2
![Image](https://i.imgur.com/XUTKb53.png)
https://stackoverflow.com/a/34258332
