# HackerRank - Symmetric Difference

## Problem Statement

Given two sets of integers, `A` and `B`, print their symmetric difference in ascending order.

The symmetric difference contains elements that exist in either set, but not in both sets.

## Input Format

- The first line contains an integer `M`, the size of set `A`.
- The second line contains `M` space-separated integers.
- The third line contains an integer `N`, the size of set `B`.
- The fourth line contains `N` space-separated integers.

## Output Format

Print the symmetric difference integers in ascending order, with each integer on a separate line.

## Sample Input

```text
4
2 4 5 9
4
2 4 11 12
```

## Sample Output

```text
5
9
11
12
```

## Explanation

Set `A` = `{2, 4, 5, 9}`

Set `B` = `{2, 4, 11, 12}`

Common elements = `{2, 4}`

Elements present in only one set = `{5, 9, 11, 12}`

After sorting in ascending order, the output is:

```text
5
9
11
12
```

## Python Solution

```python
if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))

    n = int(input())
    b = set(map(int, input().split()))

    result = sorted(a.symmetric_difference(b))

    for num in result:
        print(num)
```

## Concepts Used

- Sets
- `set()` and `map()`
- `symmetric_difference()`
- `sorted()`
- `for` loops

## Problem Link

https://www.hackerrank.com/challenges/symmetric-difference/problem
