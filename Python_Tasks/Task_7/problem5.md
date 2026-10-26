# Alternating Characters

## Problem Statement

You are given a string containing only the characters `A` and `B`.

Your task is to change the string so that there are no matching adjacent characters. You are allowed to delete zero or more characters.

Find the minimum number of deletions required to make the string alternate between `A` and `B`.

## Function Description

Complete the `alternatingCharacters` function.

### Parameter
- `s`: A string containing only `A` and `B`.

### Returns
- An integer representing the minimum number of deletions required.

## Input Format

- The first line contains an integer `q`, the number of queries.
- The next `q` lines each contain a string `s` to analyze.

## Constraints

- Each string `s` consists only of the characters `A` and `B`.

## Sample Input

```text
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
```

## Sample Output

```text
3
4
0
0
4
```

## Explanation

- `AAAA`: Delete 3 characters to obtain `A`. Minimum deletions: `3`.
- `BBBBB`: Delete 4 characters to obtain `B`. Minimum deletions: `4`.
- `ABABABAB`: No deletions are needed. Minimum deletions: `0`.
- `BABABA`: No deletions are needed. Minimum deletions: `0`.
- `AAABBB`: Delete 2 `A` characters and 2 `B` characters to obtain `AB`. Minimum deletions: `4`.
