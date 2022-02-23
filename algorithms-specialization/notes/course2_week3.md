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

## Binary Search Tree
### Sorted Arrays: Supported Operations
|Operations|Running Time|
|-|-|
|SEARCH|$O(\log n)$ (binary search)|
|SELECT (given order $i$)|$O(1)$|
|MIN/MAX|$O(1)$|
|PRED/SUCC (given pointer to a key)|$O(1)$|
|RANK (number of keys <= given value)|$O(\log n)$|
|OUTPUT in SORTED ORDER|$O(n)$|
|INSERT|? $O(n)$ 太慢了|
|DELETE|? $O(n)$ 太慢了|

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
