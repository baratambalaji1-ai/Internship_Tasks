
# HackerRank - Python If-Else

## Problem Statement

Given a positive integer `n`, perform the following conditional actions:

- If `n` is odd, print `Weird`.
- If `n` is even and in the inclusive range of 2 to 5, print `Not Weird`.
- If `n` is even and in the inclusive range of 6 to 20, print `Weird`.
- If `n` is even and greater than 20, print `Not Weird`.

## Input Format

A single line containing a positive integer, `n`.

## Constraints

- \(1 \leq n \leq 100\)

## Output Format

Print `Weird` if the number is weird. Otherwise, print `Not Weird`.

## Sample Input 0

```text
3
```

## Sample Output 0

```text
Weird
```

### Explanation 0

The number `3` is odd, so we print `Weird`.

## Sample Input 1

```text
24
```

## Sample Output 1

```text
Not Weird
```

### Explanation 1

The number `24` is even and greater than 20, so we print `Not Weird`.

## Python Solution

```python
n = int(input())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
```

## Concepts Used

- `input()` and `int()`
- `if`, `elif`, and `else`
- Modulus operator (`%`)
- Conditional statements and comparison operators

## Platform

[HackerRank - Python If-Else](https://www.hackerrank.com/challenges/py-if-else/problem)
