---
tags: algorithms, notes
---
Algortihms (Intro, Merge Sort, Guiding, Notations ($O, \Omega,\Theta$))
===
![](https://i.imgur.com/ZPwbR0s.png)
## Mantra (箴言)
![](https://i.imgur.com/iewOXRD.png)

CAN WE DO BETTER?

## Karatusba Multiplication
### Example
x = 5678  
y = 1234

step0: let $a=56, b=78, c=12, d=34$  
step1: compute $a*c = 672$  
step2: compute $b*d = 2652$  
step3: compute $(a+b)*(c+d) = 134*46 = 6164$  
step4: compute $step3 - step2 - step1 = 2840$  
step5: compute $a*c*10000 + b*d + ((a+b)*(c+d)-a*c-b*d)*100 = 7006652$  
![](https://i.imgur.com/o6wve5V.png)

### A Recursive Algorithm
$n = \text{digit number}$
![](https://i.imgur.com/3nPPpgl.png)

### Karatsuba Multiplication
![](https://i.imgur.com/lpVkOqk.png)  

只需要3次乘法就能得到結果，少於原本傳統算法的4次。

## Merge Sort
### Example
![](https://i.imgur.com/VKRtv1t.png)

### Merge Sort Running Time?
Claim:  
$6nlog_2n+6n$

**Recursion Tree Method**  
![](https://i.imgur.com/VVvLqFi.png)

總共會有$log_2n$層

每層$j=0, 1,..., log_2n$, 會有$2^j$ subproblems, 且每個subproblem的大小為$n/2^j$

假設每個subproblem共有$6$行code要執行，所以會得到$6(n/2^j)$  
而每層$j$總共的operations則 $\leq 2^j * 6(n/2^j) = 6n$  
(此結果獨立於$j$)

全部的operations則為  
$\leq 6n * (log_2n+1)$  
故最一開始的claim為真  

總結: $n$個元素共會有$log_2n+1$層，且每層的執行數為$6n$

## Guiding Principle
### Worst-case Analysis
our running time bound holds for every input of length $n$.  
particularly appropriate for "general-purpose"  

As opposed to:  
- "average-case" analysis
- benchmarks

requires domain knowledge

### Won't pay much attention to constant factor, lower-order terms
Justifications:
- way easier
- constants depend on architecture / compiler / programmer anyways
- lose very little prediction power

### Asymptotic Analysis
focus on running time for large input sizes $n$.  

E.g. $6nlog_2n+6n$ better than $\frac{1}{2}n^2$  
(merge sort vs. insertion sort)

Justification:  
- any big problems are interesting

## What Is a **Fast** Algorithm?
fast algorithm ~= worst-case running time grows slowly with input size

Holy Grail 聖杯: linear running time (or close to it)

## Asymptotic Analysis 漸進分析
### Motivation
Importance: vacabulary for the design and analysis of algorithms (e.g. "big-oh" notation)
- sweet spot for high-level reasoning about algorithms
- coarse enough to suppress architecture/language/compiler-dependent details
- sharp enough to make useful comparisons between different algorithms, especially on large inputs

### Asymptotic Analysis
High-level idea: suppress constant factors (too system-dependent) and lower-order terms (irrelevant for large inputs)

Example: equate 等同 $6nlog_2n+6n$ with just $nlogn$  
Terminology: running time is $O(nlogn)$ (big-Oh of $nlogn$) where $n$ is input size

### Example
#### One Loop
Problem: does array $A$ contain the integer $t$?  
given $A$ (array of length $n$)  
given $t$ (an integer)  

```bash=
for i = 1 to n
    if A[i] == t return TRUE
return FALSE
```
What is the runnning time?  
$O(n)$
#### Two Loops
Problem: does array $A, B$ contain the integer $t$?  
given $A, B$ (array of length $n$)  
given $t$ (an integer)  

```bash=
for i = 1 to n
    if A[i] == t return TRUE
for i = 1 to n
    if B[i] == t return TRUE
return FALSE
```
What is the runnning time?  
$O(n)$

#### Two Nested Loops
Problem: does array $A, B$ have a number in common?  
given $A, B$ (array of length $n$)  

```bash=
for i = 1 to n
    for j = 1 to n
        if A[i] == B[j] return TRUE
return FALSE
```
What is the runnning time?  
$O(n^2)$

#### Two Nested Loops (II)
Problem: does array $A$ have duplicate entries?  
given $A$ (array of length $n$)  

```bash=
for i = 1 to n
    for j = i+1 to n
        if A[i] == A[j] return TRUE
return FALSE
```
What is the runnning time?  
$O(n^2)$

## Big-Oh, Big Omega and Theta Notation
### Big-Oh
let $T(n)$ = function on $n=1,2,3,...$  
Q: When is $T(n) = O(f(n))$  
A: If eventually, $T(n)$ is bounded above by a constant multiple of $f(n)$  

![](https://i.imgur.com/B1wGHvH.png)

正式的定義為以下：  
exist $c, n_0$  
$T(n) \leq cf(n)$ for all $n \geq n_0$  
$c, n_0$ cannot depend on $n$  

### Basic Examples
#### 1.
Claim: if $T(n) = a_kn^k+...+a_1n+a_0$ then $T(n) = O(n^k)$  
Proof:  
Choose $n_0=1$ and $c=|a_k|+|a_{k-1}|+...+|a_1|+|a_0|$  
Need to show that $\forall n\geq 1, T(n) \leq cn^k$  

$T(n) \leq |a_k|n^k + ... + |a_1|n + |a_0|$  
$T(n) \leq |a_k|n^k + ... + |a_1|n^k + |a_0|n^k = cn^k$  
$T(n) \leq cn^k = O(n^k)$  

$c$基本上是反向工程，先猜再來驗證。

#### 2.
Claim: for every $k \geq 1, n^k$ is not $O(n^{k-1})$  
Proof:  
by contradition  
suppose $n^k = O(n^{k-1})$  
Then $\exists c,n_0 > 0$  
such that $n^k \leq cn^{k-1},\forall n\geq n_0$  
But then  
$n \leq c, \forall n \geq n_0$  
which is clearly false contradiction  

原因是$c$不能depends on $n$

### Omega
正式的定義如下：  
$T(n) = \Omega(f(n))$ if and only if  
$\exists c, n_0$ such that  
$T(n) \geq cf(n), \forall n \geq n_0$  

![](https://i.imgur.com/lEeQfWG.png =400x)

### Theta
正式的定義如下：  
$T(n) = \Theta(f(n))$ if and only if  
$T(n) = O(f(n))$ **and** $T(n) = \Omega(f(n))$  

$\exists c_1, c_2, n_0$ such that  
$c_1f(n) \leq T(n) \leq c_2f(n)$ for all $n \geq n_0$  

被夾在中間就是Theta

### Little-Oh
$T(n) = o(f(n))$ if and only if  
for all constant $c>0, \exists n_0$ such that  
$T(n) \leq cf(n), \forall n \geq n_0$  

Exercise: for all $k \geq 1, n^{k-1} = o(n^k)$

相對於Big-Oh，必須要證明所有的constant $c$，所以比Big-Oh更嚴格。

### Example
![](https://i.imgur.com/YZnUfZa.png)  
後3個為正確答案，因為$T > n$故有第二個答案；$T$被$n^2$ bound住故有第三個答案；$T < n^3$故有第四個答案

### Additional Examples
#### 1.
Claim: $2^{n+10} = O(2^n)$  
Proof: $2^{n+10} \leq c2^n$  
Make: $2^{n+10} = 2^{10}2^n = c2^n$  
So $c=1024, n_0=1$

#### 2.
Claim: $2^{10n}$ is not $O(2^n)$  
Proof: by contractdiction if $2^{10n} = O(2^n)$  
$2^{10n} \leq c2^n$  
but then cancelling $2^n$  
$2^{9n} \leq c$  
which is certainly false

#### 3. (harder)
Claim: for every pair of (positive) functions $f(n), g(n)$, $max\{f, g\} = \Theta(f(n)+g(n))$  

![Image](https://i.imgur.com/a0SjxyM.png)

Proof: $max\{f, g\} = O(f(n)+g(n))$  
for every $n$, we have  
$max\{f, g\} \leq f(n) + g(n)$ and  
$2max\{f, g\} \geq f(n) + g(n)$  
Thus:  
$\frac{1}{2}(f(n)+g(n)) \leq max\{f(n), g(n)\} \leq f(n) + g(n)$  
=>   $max\{f, g\} = \Theta(f(n)+g(n))$  
where $n_0=1, c_1=\frac{1}{2}, c_2=1$  

