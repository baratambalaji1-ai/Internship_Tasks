# Check Strict Superset

## Problem Statement

You are given a set `A` and `n` other sets.

Your task is to determine whether set `A` is a **strict superset** of each of the `n` other sets.

Print `True` if set `A` is a strict superset of every one of the other sets. Otherwise, print `False`.

A strict superset contains all the elements of another set and has at least one additional element that is not present in that set.

## Input Format

- The first line contains the space-separated elements of set `A`.
- The second line contains an integer `n`, the number of other sets.
- The next `n` lines contain the space-separated elements of the other sets.

## Constraints

As specified in the HackerRank problem.

## Output Format

Print `True` if set `A` is a strict superset of all the other `n` sets. Otherwise, print `False`.

## Sample Input 0

```text
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
```

## Sample Output 0

```text
False
```

## Explanation

Set `A` is a strict superset of the first set because it contains all its elements and has additional elements.

However, set `A` is not a strict superset of the second set because the element `100` is not present in set `A`.

Therefore, the output is `False`.

**Language:** Python 3

**Difficulty:** Easy
