---
tags: algorithms, notes
---
Algorithm (Heaps, Balanced Binary Search Trees)
===
不同的data structure支援不同的operations，並且能應對不同種類的tasks

我們應該要選擇**剛剛好支援**的data structure

## Heaps
a container for objects that have **keys**
- employer records, network edges, events, etc.

### Supported Operations
1. INSERT:  
    add a new object to a heap  
    running time: $O(\log n)$
2. EXTRACT-MIN (or EXTRACT-MAX):  
    remove an object in heap with a minimum (or maximum) key value  
    running time: $O(\log n)$
3. HEAPIFY  
    n batched INSERTs in $O(n)$ time
4. DELETE  
    running time: $O(\log n)$

### Application: Sorting
SelectionSort $\approx O(n)$ linear time, $O(n^2)$ running time on array of length $n$

HeapSort:  
```
- INSERT all n array elements into a heap
- EXTRACT-MIN to pluck out 拔出 elements in sorted order
```
running time = $2n$ heap operations = $O(n \log n)$ time  
(optimal for a **comparison-based** sorting algorithm!)

### Application: Median Maintanence
Input:  
a sequence $x_1, ..., x_n$ of numbers, 1-by-1

Output:  
at each time step $i$, the median of $\{x_1, ..., x_i\}$

Constraint:  
use $O(\log i)$ time at each step $i$

Solution:  
maintain heaps
- $H_{low}$: supports EXTRACT-MAX
- $H_{high}$: supports EXTRACT-MIN

Key idea:  
maintain invariant that $\approx \frac{i}{2}$  smallest (largest) elements in $H_{low}$ ($H_{high}$)

- 當一個新的數字進來，先利用$H_{low}$ (EXTRACT-MAX) 和$H_{high}$ (EXTRACT-MIN) 找出新的數字應該放在哪個heap？
- 再利用兩個heaps的長度去維持balance
- 最後找到中位數

### Application: Dijkstra's Algorithm
利用heaps來維持並找出Dijkstra greedy score (edge)

### Heap Property
heap就像是tree
- rooted
- binary
- as complete as possible

![Image](https://i.imgur.com/GeiXdRz.png)

at every node $x$:  
key[x] <= all keys of x's children  
所以root會有最小的key

### Heap: Array Implementation
![Image](https://i.imgur.com/a5PqPY0.png)
- $parent(i) = \frac{i}{2}$ 如果$i$是偶數；$floor(\frac{i}{2})$ 如果$i$是奇數
- $child(i) = 2i, 2i+1$

```
Insert(key k)
- 將k加入到heap的最後
- Bubble-Up k直到heap的性質被滿足
```

1. Bubble-Up一定會停止，且heap的性質會被滿足
2. runtime = $O(\log n)$

![Image](https://i.imgur.com/ge7vl6W.png)  
加入5到最後時，違反了heap的性質，先將5與12交換，再將5與8交換。

```
Extract-Min
- 將root拿掉 (必為最小值，heap的性質)
- 將最後的leaf作為新的root
- Bubble-Down新的root，每次交換時要選擇較小的child，直到heap的性質被滿足
```

1. Bubble-Down在每個level最多執行1次
2. runtime = $O(\log n)$

![Image](https://i.imgur.com/c7Y2Bc7.png)  
拿掉root時，將13作為新的root，違反了heap的性質，先將13與4交換(與較小的child交換，4<8)，再將13與4交換。

## Balanced Search Tree
### Sorted Arrays: Supported Operations
|Operations|Running Time|
|-|-|
|SEARCH|$O(\log n)$ (binary search)|
|SELECT (given order $i$)|$O(1)$|
|MIN/MAX|$O(1)$|
|PRED/SUCC (given pointer to a key)|$O(1)$|
|RANK (number of keys <= given value)|$O(\log n)$|
|OUTPUT in SORTED ORDER|$O(n)$|
|INSERT|$O(n)$ 太慢了|
|DELETE|$O(n)$ 太慢了|

### Balanced Search Tree: Supported Operations
基本上跟Sorted Array相同，但是有更快的INSERT與DELETE。

|Operations|Running Time|
|-|-|
|SEARCH|$O(\log n)$ (binary search)|
|SELECT (given order $i$)|$O(\log n)$ 稍慢|
|MIN/MAX|$O(\log n)$ 稍慢|
|PRED/SUCC (given pointer to a key)|$O(\log n)$ 稍慢|
|RANK (number of keys <= given value)|$O(\log n)$|
|OUTPUT in SORTED ORDER|$O(n)$|
|INSERT|$O(\log n)$ 快很多|
|DELETE|$O(\log n)$ 快很多|

### Binary Search Tree Structure
- exactly one node per key
- each node has
    1. left / right child pointer
    2. parent pointer

Search Tree Property:  
![Image](https://i.imgur.com/xJu977Y.png)

The Height of a BST:  
height could be $\approx \log_2 n$ to $\approx n$

![Image](https://i.imgur.com/Ta62Qv5.png)

### Searching & Inserting
```
SEARCH (key k, tree T)
- start at the root
- traverse left (k < key) / right (k > key) child pointers
- return node with key k or NULL
```

```
INSERT (key k, tree T)
- search for k (必須要失敗，代表沒有一樣的key)
- rewire final NULL pointer to new node with key k
```

![Image](https://i.imgur.com/Ls8jgjZ.png)  
最後一定會繼續保持search tree性質，只是不一定平衡

### Min, Max, Pred and Succ
```
MIN
- start at root
- follow `left child pointers` until last key found
```

```
MAX
- start at root
- follow `right child pointers` until last key found
```

```
PREDECESSOR(key k)
- if k's left subtree nonempty:
    - return max key in left subtree
- otherwise:
    - follow parent pointers until get to a key less than k (first time `turn left`)
```
![Image](https://i.imgur.com/XhneR0X.png)

### In-Order Traversal
將key依序印出，由小到大

```
- let r = root of search tree, with subtrees T_L and T_R
- recurse on T_L
- print out r's key
- recurse on T_R
```
![Image](https://i.imgur.com/LVKtJTG.png)

Running Time: $O(n)$

### Deletion
```
DELETE(key k)
- search for k
- (EASY CASE: k's node has no children)
    - just delete k's node
- (MEDIUM CASE: k's node has 1 child)
    - just `splice out 對接` k's node
- (DIFFICULT CASE: k's node has 2 children)
    - compute k's predecessor l
    - swap k & l!
    - (k has no right child!) delete or splice out k node
```
![Image](https://i.imgur.com/N3EEy0Q.png)
![Image](https://i.imgur.com/q71IFLa.png)

Running Time: $O(\text{height})$

### Select & Rank
Idea:  
store a little bit of extra info at each tree node **about the tree itself**

Example:  
size(x) = number of tree nodes in subtree rooted at x

![Image](https://i.imgur.com/URlmJkz.png)

if x has children y and z, then size(x) = size(y) + size(z) + 1

```
Select(ith order statistic)
- start at root x, with children y & z
- let a = size(y)
- if a = i-1
    - return x's key
- if a >= i
    - recursively compute ith order statistic of search tree rooted at y
- if a < i-1
    - recursively compute (i-a-1)th order statistic of search tree rooted at z
```

Running Time = $O(\text{height})$

## Red-Black Trees
### Red-Black Invariants
1. each node **red** or **black** (因為當時paper的印刷技術只支援很少數的顏色)
2. root is **black**
3. no 2 reds in a row (red node => only black children)
4. every root-NULL path (unsuccessful search) has same number of black nodes  
    從root開始，走到leaf的路徑為root-NULL path

### Examples
Claim:  
a chain of length 3 cannot be a red-black tree

Proof:  
![Image](https://i.imgur.com/Z7ags41.png)  
- 搜尋0，則會得到1個black node (1)
- 搜尋4，則會得到2個black nodes (1, 3)

![Image](https://i.imgur.com/url0eRT.png)  
![Image](https://i.imgur.com/ss9bh6m.png)

### Height Guarantee
Claim:  
every red-black tree with $n$ nodes has $\text{height} \leq 2\log_2(n+1)$

Proof:  
observation: if every root-NULL path has $\geq k$ nodes, then tree includes a perfectly balanced search tree of depth $k-1$

![Image](https://i.imgur.com/TTt615A.png)

size $n \geq 2^k-1$ where $k=$ minumum number of nodes on root-NULL path

(假設$k=3$，代表每個path有至少3個black nodes，所以$n$必定大於等於$2^k-1=7$)

Thus:  
in a red-black tree with $n$ nodes, there is a root-NULL path with at most $\log_2(n+1)$ black nodes

By 4th invariants:  
every root-NULL path has $\leq \log_2(n+1)$ black nodes

By 3rd invariants:  
every root-NULL path has $\leq 2\log_2(n+1)$ total nodes

### Rotations
Idea:  
locally rebalance subtrees at a node in $O(1)$ time

Left Rotation:  
![Image](https://i.imgur.com/AGeu58s.png)  
- A: 比x小
- B: 在x與y之間
- C: 比y大

Right Rotation:  
![Image](https://i.imgur.com/H9LZE7F.png)

只要交換pointer即可，因此為$O(1)$時間

### Insertion in a Red-Black Tree
```
Insert(x)
- insert x as usual (x as a leaf)
- try coloring x red
- if x's parent y is black
    - done
- else y is red
    - y has a black parent w
    ...
```

1. the other child z of x's grandparent w is also red  
    ![Image](https://i.imgur.com/NVVOi76.png)  
    => recolor y, z black and w red  
    (key point: does not break invariant 4)  
    => either restores invariant 3 or propagate the double red upward  
    => 如果跑到root了，再把root重新塗成black來符合invariant 2
    => can only happen $O(\log n)$ time

2. the other child z of x's grandparent w is black    
    ![Image](https://i.imgur.com/mxjFd7j.png)
    => 利用2~3次rotations + recoloring即可在$O(1)$ time解決 (練習)

## Problem Set
![Image](https://i.imgur.com/xyGA1MR.png)  
如果新加入的數字是最大的，則需要掃過全部的$n$，$O(n)$

![Image](https://i.imgur.com/41JPLrm.png)  
因為是unsorted array，所以新加入的數字可以隨便加，$O(1)$

![Image](https://i.imgur.com/p0a84M8.png)  
直接做5次的Extract-Min，所以可以在constant time做完。  
[https://andrew-exercise.blogspot.com/2015/11/algorithms-design-and-analysis-part-1_86.html](https://andrew-exercise.blogspot.com/2015/11/algorithms-design-and-analysis-part-1_86.html)

![Image](https://i.imgur.com/5KuKR9p.png)  
A chain with four nodes is a counterexample.  
[https://andrew-exercise.blogspot.com/2015/11/algorithms-design-and-analysis-part-1_75.html](https://andrew-exercise.blogspot.com/2015/11/algorithms-design-and-analysis-part-1_75.html)
