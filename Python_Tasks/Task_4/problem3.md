# HackerRank - Python: Division

## Problem Statement

The program reads two integers, `a` and `b`, from standard input.

Print two lines:

1. The result of integer division (`a // b`).
2. The result of float division (`a / b`).

No rounding or formatting is necessary.

## Input Format

- The first line contains integer `a`.
- The second line contains integer `b`.

## Output Format

Print the integer division result on the first line and the float division result on the second line.

## Sample Input

```text
4
3
```

## Sample Output

```text
1
1.33333333333
```

## Python Solution

```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)
```

## Concepts Used

- `input()` and `int()`
- Integer division (`//`)
- Float division (`/`)

## Problem Link

https://www.hackerrank.com/challenges/python-division/problem
