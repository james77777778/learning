---
tags: algorithms, notes
---
Algorithm (Hashing, Bloom Filters)
===
## Hash Table
Maintain a (possibly evolving) set of stuff.  
(transactions, people+associated data, IP addresses, etc.)

### Supported Operations
1. INSERT:  
    add new record
2. DELETE:  
    delete existing record
3. LOOKUP:  
    check for a particular record

Amazing Guarantee:  
all run in $O(1)$ time!
1. properly implemented
2. 資料正常

### Applications
#### De-Duplication
Claim:  
a "stream" of objects  

Goal:  
remove duplicates (i.e. keep track of unique objects)

Solution:  
where new object x arrives, LOOKUP x, if not found then INSERT x

#### The 2-SUM Problem
Input:  
unsorted array $A$ of $n$ integers. Target sum $t$.

Goal:  
determine whether or not there are two numbers $x, y \in A$ with $x+y=t$

Solution:  
1. INSERT elements of $A$ into hash table $H$
2. for each $x \in A$, LOOKUP $t-x \in H$

Running time: $n*O(1) = O(n)$

#### Birthday Paradox
![Image](https://i.imgur.com/EluoXXa.png)

### Implementation
#### High-Level Idea
universe $u$ and want to maintain evolving set $s \subseteq u$  
($s$變動不會太大)

Solution:  
1. pick $n=$ number of "buckets" with $n \approx |s|$
2. choose a hash function $h: u \to \{0, 1, 2, ..., n-1\}$
3. use array $A$ of length $n$, store $x$ in $A[h(x)]$

#### Resolving Collisions:  
$x, y \in u$ such that $h(x) = h(y)$

Solution 1:  
chaining
- keep linked list in each bucket
- given a key/object $x$, perform INSERT/DELETE/LOOKUP in the list in $A[h(x)]$

Solution 2:  
open addressing (1 object per bucket)
- hash function specifies probe sequence $h_1(x), h_2(x), ...$ (keep tring til find open slot)
- examples: linear probing, double hashing

#### Good Hash Function?
假設有$n$個buckets，則對於$m$個objects，最差會產生$m-1$次collisions，而這取決於hash function的好壞

1. good performance => i.e., should **spread data out** (completely random hashing)
2. should be easy to store / very fast to evaluate

反例：  
$h(x) = x \mod 1000$, 導致奇數的bucket都不會被用到。

#### Quick-Dirty Hash Functions
![Image](https://i.imgur.com/Du4OzTO.png)

How to choose $n$ (number of buckets)?  
1. n to be a prime
2. not too close to a power of 2
3. not too close to a power of 10

## Universal Hashing
### The Load of a Hash Tabel
Definition:  
the load factor of a hash table is  
$\alpha = \frac{\text{number of objects in hash table}}{\text{number of buckets of hash table}}$

Note:  
1. $\alpha = O(1)$ is necessary condition for operations to run in constant time
2. with open addressing, need $\alpha << 1$

### Pathological Data Sets
For every hash function, there is a pathological data set

Reason:  
fix a hash function $h:U \to \{0, 1, ..., n-1\}$  
By Pigeonhole Priciple, $\exists \text{bucket } i$ such that at least $\frac{|u|}{n}$ elements of $u$ hash to $i$ under $h$  
只要發現collisions，就可以一直重複塞同樣資料，來產生非常多collisions

Solutions:  
1. use a cryptographic hash function (e.g., SHA-2)
    - infeasible to reverse engineer a pathological data set
2. use randomization
    - design a family $H$ of hash functions such that, $\forall$ data sets $S$, **almost all** functions $h \in H$ spread $S$ out **pretty evenly**
    - 在程式runtime中，隨機挑選$h$來避免逆向工程

### Universal Hash Functions
Definition:  
Let $H$ be a set of hash functions from $u$ to $\{0, 1, 2, ..., n-1\}$  
$H$ is **universal** if and only if:  
for all $x, y \in u$,  
$\Pr_{h \in H}[x, y \text{ collide}] \leq \frac{1}{n}$  
($n=$ number of buckets)  
where $h$ is chosen uniformly at random from $H$  
對於每個$h$，所有的$x,y$相撞的機率都會$\leq \frac{1}{n}$

![Image](https://i.imgur.com/sFDIHjg.png)  
- Yes: Take $H=$ all functions from $u$ to $\{0, 1, ..., n-1\}$
- No: Take $H=$ the set of $n$ differnet constant functions  
    譬如$h(x) = 10$

### Example: Hashing IP Addresses
Let $u=$ IP addresses (of the form $(x_1, x_2, x_3, x_4)$ with each $x_i \in \{0, 1, ..., 255\}$)  
Let $n=$ a prime  

Construction:  
Define 1 hash function $h_a$ per 4-tuple $a=(a_1, a_2, a_3, a_4)$ with each $a_i \in \{0, 1, ..., n-1\}$

Define:  
$h_a$: IP address -> buckets by $h_a(x_1, x_2, x_3, x_4) = (a_1x_1+a_2x_2+a_3x_3+a_4x_4) \mod n$  
$H=\{h_a|a_1, a_2, a_3, a_4 \in \{0, 1, ..., n-1\}\}$

Theorem:  
This family is universal

#### Proof (Part I)  
consider distinct IP addresses $(x, y)$

Assume:  
$x_4 \neq y_4$

Question:  
collisions probability?

Note:  
collision <=> $a_1x_1+a_2x_2+a_3x_3+a_4x_4=a_1y_1+a_2y_2+a_3y_3+a_4y_4$  
<=> $a_4(x_4-y_4) \mod n = \Sigma_{i=1}^3a_i(y_i-x_i) \mod n$

Next:  
condition on random choices of $a_1, a_2, a_3$

#### Proof (Part II)
with $a_1, a_2, a_3$ fixed arbitrarily, how many choices of $a_4$ satisfy $a_4(x_4-y_4) \mod n = \Sigma_{i=1}^3a_i(y_i-x_i) \mod n$ ?

![Image](https://i.imgur.com/i2QpEZp.png)

Key Claim:  
left-hand side equally likely to be any of $\{0, 1, 2, ..., n-1\}$, implies $\Pr[h_a(x) = h_a(y)] = \frac{1}{n}$

Reason:  
$x_4 \neq y_4$ ($x_4 - y_4 \neq 0$), $n$ is prime, $a_4$ uniform at random

Proof by example:  
$n=7, x_4-y_4=2 \text{ or } 3 \mod n$

### Open Addressing
1 object per slot, hash function produces a probe sequence for each possible key x

Fact:  
difficult to analyze rigorously 嚴格的

#### Heuristic Analysis
Heuristic assumption (沒有證明):  
all $n!$ probe sequences equally likely

Observation:  
under heuristic assumption, expected INSERT time is $\approx \frac{1}{1-\alpha}$, where $\alpha=$ load

Proof:  
A random probe finds an empty slot with probability $1-\alpha$

So:  
INSERT time $\approx$ the number $N$ of coin flips to get **heads**, where $\Pr[\text{heads}] = 1-\alpha$

Note:  
$E[N] = 1+\alpha E[N]$ (第一次就中head，加上$\alpha$乘上下一次中head)  
=> $E[N] = \frac{1}{1-\alpha}$

#### Linear Probing
Note:  
heuristic assumption completely false

Assume instead:  
initial probe uniformly random, independent for different keys

Theorem (Knuth 1962):  
under above assumption, expected INSERT time is $\approx \frac{1}{(1-\alpha)^2}$, where $\alpha = \text{load}$

#### 補充
以下內容來自網路 `algorithms-specialization/complementary/hash_table.pdf`

一旦發生碰撞，就往下一位置探測，如果下一位置仍然被占用，則繼續往下搜尋，直到找空白的位置為止  
以線性探測的方式存放資料，搜尋資料時會發生三種可能的情形如下：
1. 經雜湊函數計算位置後，資料值與鍵值相同，表示搜尋成功。
2. 資料值與鍵值不相同，所以繼續往下探測，直到搜尋成功為止。
3. 在搜尋過程中遇到空白位置，這就表示搜尋失敗。

當資料值若集中在某一區段，則每次該區段資料值插入時，發生碰撞的頻率將會快速增加，這種現象稱之為叢集（cluster）。

## Bloom Filters
### Supported Operations
Fast INSERT & LOOKUP

Comparison to Hash Table:  
- Pros: move space efficient
- Cons:
    1. can't store an associated object
    2. no deletions
    3. small false positive probability (might say $x$ has been INSERTed even though it hasn't been)

### Applications
- Early: spellcheckers (利用預先建好的超大詞庫來檢查是否有typo)
- Canonical 典範: list of forbidden passwords
- Modern: network routers
    - limited memory, need to be super-fast

### Under the Hood 本質上
Ingredients:  
1. array of $n$ bits (so $\frac{n}{|s|} = $ number of bits per object in dataset $S$)
2. $k$ hash functions $h_1, ..., h_k$ ($k=$ small constant)

```
INSERT(key x)
- for i=1, 2, ..., k
    - set A[h_i(x)] = 1 (不管之前有沒有設過，都設成1)
```

```
LOOKUP(key x)
- if A[h_i(x)] = 1 for every i=1, 2, ..., k
    - return True
```

譬如說有3個hash functions $h_1, h_2, h_3$:
- $h_1(x) = x \mod 3$
- $h_2(x) = x \mod 5$
- $h_3(x) = x \mod 7$

若輸入$x=10$，則同時把$A[1], A[0], A[3]$設為$1$，  
若查詢$x=10$，只要同時檢查$A[1], A[0], A[3]$是否為$1$即可  
(代價就是查詢可能會有false positive，即沒有$x=10$在裡面，但bloom filters卻說有)

- 如果 Bloom Filter 回傳沒有（negative）：代表資料**一定沒有**在Bloom Filter中
- 如果 Bloom Filter 回傳有（positive）：代表資料**可能有**在Bloom Filter中，並**不是一定有**在Bloom Filter中 (有可能被其他$x$設過$h_i(x)=1$了)

### Heuristic Analysis
Assume:  
all $h_i(x)$'s uniformly random and independent (across different i's and x's)  
現實中其實不太容易實現

Setup:  
$n$ bits, insert data set $S$ into bloom filter  

假設bloom filter有$n$ bits且插入了$S$個資料在有$k$個hash functions的情況下：  
其中1個bit還維持是$0$的機率為$(1-\frac{1}{n})^{k|S|}$  
false positive的機率就會是$(1-(1-\frac{1}{n})^{k|S|})^k$

Note:  
for each bit of $A$, the probability it's been set to 1 is $1-(1-\frac{1}{n})^{k|S|}$  
$(1-\frac{1}{n})^{k|S|} \leq 1-e^{\frac{-k|S|}{n}} = 1-e^{\frac{-k}{b}}$  
$b$ = number of bits per object ($n/|S|$)

![Image](https://i.imgur.com/luvPqe7.png)

So:  
under assumption, for $x \not\in S$, false positive probability is $\leq (1-e^{\frac{-k}{b}})^k$, where $b$ = number of bits per object  
error rate: $\epsilon = (1-e^{\frac{-k}{b}})^k$

for fixed $b$, $epsilon$ is minimized by setting $k \approx (\ln 2)b$ ($\ln 2 \approx 0.693$)

$\epsilon \approx (\frac{1}{2})^{(\ln 2)b}$ or $b \approx 1.44\log_2\frac{1}{\epsilon}$

EX:  
with $b=8$, choose $k=5, 6$, error probability only $\approx 0.02$

## Problem Set
![Image](https://i.imgur.com/bstvJPe.png)

![Image](https://i.imgur.com/KacUmoT.png)