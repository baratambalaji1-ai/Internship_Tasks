# Check Subset

## Problem Statement

You are given two sets, `A` and `B`.

Your task is to determine whether set `A` is a subset of set `B`.

- If set `A` is a subset of set `B`, print `True`.
- If set `A` is not a subset of set `B`, print `False`.

## Input Format

- The first line contains the number of test cases, `T`.
- The first line of each test case contains the number of elements in set `A`.
- The second line of each test case contains the space-separated elements of set `A`.
- The third line of each test case contains the number of elements in set `B`.
- The fourth line of each test case contains the space-separated elements of set `B`.

## Constraints

As specified in the HackerRank problem.

## Output Format

Print `True` or `False` for each test case on separate lines.

## Sample Input

```text
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
```

## Sample Output

```text
True
False
False
```

## Explanation

**Test Case 1**

Set `A = {1, 2, 3, 5, 6}`

Set `B = {9, 8, 5, 6, 3, 2, 1, 4, 7}`

All elements of set `A` are present in set `B`. Therefore, `A` is a subset of `B`, and the output is `True`.

**Language:** Python 3

**Difficulty:** Easy
