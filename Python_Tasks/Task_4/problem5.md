# HackerRank - Print Function

## Problem Statement

The program reads an integer `n` from standard input.

Without using string methods, print the integers from `1` through `n` consecutively, without spaces between them.

## Input Format

The first line contains an integer `n`.

## Constraints

- \(1 \leq n \leq 150\)

## Output Format

Print the integers from `1` through `n` as a single string, without spaces.

## Sample Input

```text
3
```

## Sample Output

```text
123
```

## Explanation

The integers from `1` through `3` are `1`, `2`, and `3`.

Print them consecutively without spaces to get `123`.

## Python Solution

```python
if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        print(i, end='')
```

## Concepts Used

- `input()` and `int()`
- `for` loop
- `range()`
- `print()` with the `end` parameter

## Problem Link

https://www.hackerrank.com/challenges/python-print/problem
