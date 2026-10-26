# Funny String

## Problem Statement

In this challenge, you will determine whether a string is funny or not.

To determine whether a string is funny:

1. Create a copy of the string in reverse.
2. Calculate the absolute difference between the ASCII values of every pair of adjacent characters in the original string.
3. Calculate the absolute difference between the ASCII values of every pair of adjacent characters in the reversed string.
4. If both lists of differences are the same, the string is `Funny`. Otherwise, it is `Not Funny`.

Determine whether the given string is funny.

## Function Description

Complete the `funnyString` function.

### Parameter
- `s`: A string to test.

### Returns
- `Funny` if the string is funny.
- `Not Funny` otherwise.

## Input Format

- The first line contains an integer `q`, the number of queries.
- The next `q` lines each contain a string `s`.

## Constraints

- `1 <= q <= 10`
- `2 <= length of s <= 10000`
- The string contains lowercase English letters.

## Sample Input

```text
2
acxz
bcxz
```

## Sample Output

```text
Funny
Not Funny
```

## Explanation

Let `R` be the reverse of string `s`.

### Test Case 0

Original string: `acxz`

Reversed string: `zxca`

The absolute differences between adjacent ASCII values are:

- Original string: `[2, 21, 2]`
- Reversed string: `[2, 21, 2]`

Both lists are the same, so the answer is `Funny`.

### Test Case 1

Original string: `bcxz`

Reversed string: `zxcb`

The absolute differences between adjacent ASCII values are:

- Original string: `[1, 21, 2]`
- Reversed string: `[2, 21, 1]`

The lists are different, so the answer is `Not Funny`.
