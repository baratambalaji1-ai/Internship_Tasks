# Two Strings

## Problem Statement

Given two strings, determine if they share a common substring. A substring may be as small as one character.

## Function Description

Complete the `twoStrings` function.

### Parameters
- `s1`: A string.
- `s2`: Another string.

### Returns
- `string`: Either `YES` or `NO`.

## Input Format

- The first line contains a single integer `p`, the number of test cases.
- The following `p` pairs of lines are as follows:
  - The first line contains string `s1`.
  - The second line contains string `s2`.

## Constraints

- `1 ≤ p ≤ 10`
- `1 ≤ length of s1, length of s2 ≤ 10⁵`
- `s1` and `s2` consist of characters in the range `ascii[a-z]`.

## Output Format

For each pair of strings, print `YES` if they share a common substring. Otherwise, print `NO`.

## Sample Input

```text
2
hello
world
hi
world
```

## Sample Output

```text
YES
NO
```

## Explanation

We have two pairs to check:

1. `hello` and `world` share common characters such as `o` and `l`. Therefore, the answer is `YES`.
2. `hi` and `world` share no common characters. Therefore, the answer is `NO`.
