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

### Application
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