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
