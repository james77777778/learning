# Algorithms Specialization (Coursera)
## Lecture
[https://www.coursera.org/specializations/algorithms](https://www.coursera.org/specializations/algorithms)

## Courses
1. Divide and Conquer, Sorting and Searching, and Randomized Algorithms
    - Week1: Intro, Merge Sort, Guiding, Notations ($O, \Omega,\Theta$)
    - Week2: Counting Inversions, Strassen's Subcubic Matrix Multiplication, Cloeset Pair, Master Method
    - Week3: Quick Sort
    - Week4: Linear-Time Selection, Graphs, Contraction Algorithm
2. Graph Search, Shortest Paths, and Data Structures
3. Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
4. Shortest Paths Revisited, NP-Complete Problems and What To Do About Them

## Codes
- Python3.8
- pytest

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
    cd algorithms-specialization\codes\course1_week4
    pytest
    # or
    # iteration is set to 100, the final answer should be 17
    python3 mincut.py
    ```
