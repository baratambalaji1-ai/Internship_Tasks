# HackerRank - Loops

## Problem Statement

The provided code reads an integer `n` from standard input.

For all non-negative integers `i` less than `n`, print the square of `i`, (`i * i`), on a separate line.

## Input Format

The first and only line contains the integer `n`.

## Constraints

- \(1 \leq n \leq 20\)

## Output Format

Print `n` lines, one corresponding to each integer `i` from `0` to `n - 1`.

## Sample Input

```text
5
```

## Sample Output

```text
0
1
4
9
16
```

## Explanation

The non-negative integers less than `5` are `0, 1, 2, 3, 4`.

Their squares are:

- `0 * 0 = 0`
- `1 * 1 = 1`
- `2 * 2 = 4`
- `3 * 3 = 9`
- `4 * 4 = 16`

## Python Solution

```python
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i * i)
```

## Concepts Used

- `input()` and `int()`
- `for` loop
- `range()`
- Multiplication and squaring

## Problem Link

https://www.hackerrank.com/challenges/python-loops/problem
