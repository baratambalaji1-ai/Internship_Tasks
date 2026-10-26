# Weighted Uniform Strings

## Problem Statement

A weighted string is a string of lowercase English letters where each letter has a weight. The weights range from `1` to `26`, corresponding to the letters `a` to `z`.

The weight of a string is the sum of the weights of its characters.

For example:
- `a` has a weight of `1`.
- `b` has a weight of `2`.
- `c` has a weight of `3`.
- `abc` has a weight of `1 + 2 + 3 = 6`.

A uniform string consists of a single character repeated one or more times. For example, `ccc` and `a` are uniform strings, but `bcb` and `cd` are not.

Given a string `s`, consider the set of weights for all possible uniform contiguous substrings of `s`.

You are given `q` queries, each containing a single integer. For each query, return `Yes` if the queried weight exists in the set of uniform substring weights. Otherwise, return `No`.

## Function Description

Complete the `weightedUniformStrings` function.

### Parameters
- `s`: The original string.
- `queries`: An array of integers representing the queried weights.

### Returns
- `string[]`: An array containing `Yes` or `No` for each query.

## Input Format

- The first line contains a string `s`.
- The second line contains an integer `q`, the number of queries.
- Each of the next `q` lines contains an integer `x`, representing a queried weight.

## Constraints

- `s` contains only lowercase English letters (`ascii[a-z]`).
- `1 ≤ length of s ≤ 10⁵`
- `1 ≤ q ≤ 10⁵`
- `1 ≤ x ≤ 10⁷`

## Output Format

For each query, print `Yes` if the queried weight exists among the weights of uniform contiguous substrings of `s`. Otherwise, print `No`.

## Sample Input 0

```text
abccddde
6
1
3
12
5
9
10
```

## Sample Output 0

```text
Yes
Yes
Yes
Yes
No
No
```

## Explanation 0

The weights of uniform substrings in `abccddde` include:

| Substring | Weight |
|---|---:|
| `a` | 1 |
| `b` | 2 |
| `c` | 3 |
| `cc` | 6 |
| `d` | 4 |
| `dd` | 8 |
| `ddd` | 12 |
| `e` | 5 |

The first four queries match weights of uniform substrings, so their answers are `Yes`.

The last two queries, `9` and `10`, do not match any uniform substring weight, so their answers are `No`.

Note that `de` is a substring, but it is not uniform because it contains two different characters.

## Sample Input 1

```text
aaabbbbcccddd
5
9
7
8
12
5
```

## Sample Output 1

```text
Yes
No
Yes
Yes
No
```
