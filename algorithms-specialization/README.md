# Algorithms Specialization (Coursera)
## Lecture
[https://www.coursera.org/specializations/algorithms](https://www.coursera.org/specializations/algorithms)

## Courses
1. Divide and Conquer, Sorting and Searching, and Randomized Algorithms
    - [Week1](notes/course1_week1.md): Intro, Merge Sort, Guiding, Notations ($O, \Omega,\Theta$)
    - [Week2](notes/course1_week2.md): Counting Inversions, Strassen's Subcubic Matrix Multiplication, Cloeset Pair, Master Method
    - [Week3](notes/course1_week3.md): Quick Sort
    - [Week4](notes/course1_week4.md): Linear-Time Selection, Graphs, Contraction Algorithm
2. Graph Search, Shortest Paths, and Data Structures
    - [Week1](notes/course2_week1.md): Graph Search, Topological Sort, Strongly Connected Component
    - [Week2](notes/course2_week2.md): Dijkstra's Shortest Path Algorithm
    - [Week3](notes/course2_week3.md): Heaps, Balanced Binary Search Trees
    - [Week4](notes/course2_week4.md): Hashing, Bloom Filters
3. Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
    - [Week1](notes/course3_week1.md): Greedy Algorithms, Scheduling Application, Prim's Minimum Spanning Tree
    - [Week2](notes/course3_week2.md): 
    - [Week3](notes/course3_week3.md): 
    - [Week4](notes/course3_week4.md): 
4. Shortest Paths Revisited, NP-Complete Problems and What To Do About Them

## Usage
Run pytest in each subfolder in `./codes`.
1. Karatsuba Multiplication
    ```bash
    cd algorithms-specialization/codes/course1_week1
    pytest
    ```
2. Counting Inversion
    ```bash
    cd algorithms-specialization/codes/course1_week2
    pytest
    ```
3. Quick Sort
    ```bash
    cd algorithms-specialization/codes/course1_week3
    pytest
    # or
    python3 quick_sort.py
    ```
4. Minimum Cut (Random)
    ```bash
    cd algorithms-specialization/codes/course1_week4
    pytest
    # or
    # iteration is set to 100, the final answer should be 17
    python3 mincut.py
    ```
5. Strongly Connected Component  
    You should download dataset and place at `algorithms-specialization/codes/course2_week1/SCC.txt`.  
    [dataset](http://www.algorithmsilluminated.org/datasets/problem8.10.txt)
    ```bash
    # this might take some time due to large dataset `SCC.txt`
    cd algorithms-specialization/codes/course2_week1
    wget http://www.algorithmsilluminated.org/datasets/problem8.10.txt -O SCC.txt
    pytest
    # or
    python3 scc.py
    ```
6. Dijkstra's Shortest Path  
    ```bash
    cd algorithms-specialization/codes/course2_week2
    pytest
    # or
    python3 dijkstra.py
    ```
7. Median Maintenance  
    ```bash
    cd algorithms-specialization/codes/course2_week3
    python3 median_maintenance.py
    ```
8. 2 Sum
    You should download dataset and place at `algorithms-specialization/codes/course2_week4/algo1-programming_prob-2sum.txt`.  
    [dataset](http://www.algorithmsilluminated.org/datasets/problem12.4.txt)
    ```bash
    cd algorithms-specialization/codes/course2_week4
    wget http://www.algorithmsilluminated.org/datasets/problem12.4.txt -O algo1-programming_prob-2sum.txt

    # take long time to compute the answer (427)
    python3 two_sum.py
    ```
