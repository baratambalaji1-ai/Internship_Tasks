# HackerRank: Merge the Tools!

## Problem Statement

You are given a string `s` of length `n` and an integer `k`, where `k` is a factor of `n`.

Split the string `s` into `n/k` substrings, each containing `k` consecutive characters.

For each substring, create a new string by removing repeated occurrences of characters while preserving the original order of the remaining characters.

Print each resulting string on a separate line.

### Input Format
- The first line contains the string `s`.
- The second line contains the integer `k`.

### Constraints
- \(1 \leq k \leq n\)
- \(n\) is a multiple of \(k\).
- The string contains uppercase English letters.

### Sample Input
```text
AABCAAADA
3
```

### Sample Output
```text
AB
CA
AD
```
