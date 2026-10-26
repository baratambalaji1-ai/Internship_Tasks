# Sherlock and the Valid String

## Problem Statement

Sherlock considers a string to be valid if all characters of the string appear the same number of times.

It is also valid if Sherlock can remove just one character at one index in the string, and the remaining characters will occur the same number of times.

Given a string `s`, determine if it is valid. If so, return `YES`; otherwise, return `NO`.

## Function Description

Complete the `isValid` function.

### Parameter
- `s`: A string.

### Returns
- `string`: Either `YES` or `NO`.

## Input Format

A single string `s`.

## Constraints

- `1 ≤ length of s ≤ 10⁵`
- Each character of `s` is a lowercase English letter (`a-z`).

## Output Format

Print `YES` if the string is valid. Otherwise, print `NO`.

## Sample Input 0

```text
aabbcd
```

## Sample Output 0

```text
NO
```

## Explanation 0

Given the string `aabbcd`, we would need to remove two characters, both `c` and `d`, to make it valid as `aabb`.

Alternatively, removing `a` and `b` would leave `abcd`, but this would still not make all character frequencies equal.

We are limited to removing only one character, so the string is invalid.

## Sample Input 1

```text
aabbccddeefghi
```

## Sample Output 1

```text
NO
```

## Explanation 1

The character frequencies are:

```text
{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}
```

There are two ways to make the string valid:

- Remove all characters with a frequency of `1`.
- Remove enough occurrences of characters with a frequency of `2`.

Neither option can be achieved by removing just one character. Therefore, the string is invalid.

## Sample Input 2

```text
abcdefghhgfedecba
```

## Sample Output 2

```text
YES
```

## Explanation 2

All characters occur twice except for `e`, which occurs three times.

We can delete one occurrence of `e` to make every character appear exactly twice. Therefore, the string is valid.
