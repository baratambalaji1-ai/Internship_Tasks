# Separate the Numbers

## Problem Statement

A numeric string `s` is beautiful if it can be split into a sequence of two or more positive integers, satisfying the following conditions:

1. Each integer in the sequence is exactly one greater than the previous integer.
2. No integer contains a leading zero. For example, `01` is invalid.
3. The order of the digits in the string cannot be changed.

For example, the string `1234` can be split into `1, 2, 3, 4`, making it beautiful.

Perform `q` queries, where each query consists of an integer string `s`.

For each query, print whether the string is beautiful. If it is beautiful, print `YES x`, where `x` is the first number in the increasing sequence. If multiple values of `x` are possible, choose the smallest. Otherwise, print `NO`.

## Function Description

Complete the `separateNumbers` function.

### Parameter
- `s`: An integer represented as a string.

### Prints
- Print `YES x` if the string is beautiful, where `x` is the first number in the sequence.
- Otherwise, print `NO`.

The function does not return a value.

## Input Format

- The first line contains an integer `q`, the number of strings to evaluate.
- Each of the next `q` lines contains an integer string `s`.

## Constraints

- `1 ≤ q ≤ 10`
- `1 ≤ length of s ≤ 32`

## Output Format

For each query, print the result on a new line:

- `YES x` if the string is beautiful, where `x` is the smallest possible first number.
- `NO` if the string is not beautiful.

## Sample Input 0

```text
7
1234
91011
99100
101103
010203
13
1
```

## Sample Output 0

```text
YES 1
YES 9
YES 99
NO
NO
NO
NO
```

## Explanation 0

The first three strings are beautiful:

- `1234` → `1, 2, 3
