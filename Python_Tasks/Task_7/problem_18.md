# String Construction

## Problem Statement

Amanda has a string of lowercase letters that she wants to copy to a new string. She can perform the following operations to construct the new string `p`:

1. Append a character to the end of `p` at a cost of 1 dollar.
2. Choose any substring of `p` and append it to the end of `p` at no cost.

Given `n` strings, find and print the minimum cost of copying each string to a new string.

## Function Description

Complete the `stringConstruction` function.

### Parameter
- `s`: A string to copy.

### Returns
- `int`: The minimum cost of constructing the string.

## Input Format

- The first line contains a single integer `n`, the number of strings.
- Each of the next `n` lines contains a single string `s`.

## Constraints

- `1 ≤ n ≤ 5`
- Each string `s` consists of lowercase English letters (`a-z`).

## Output Format

For each string `s`, print the minimum cost of constructing the new string on a new line.

## Sample Input

```text id="j3sh1p"
2
abcd
abab
```

## Sample Output

```text id="7f6e2z"
4
2
```

## Explanation

### Query 0: `abcd`

Initially, the new string is empty.

- Append `a` at a cost of 1 dollar.
- Append `b` at a cost of 1 dollar.
- Append `c` at a cost of 1 dollar.
- Append `d` at a cost of 1 dollar.

The total cost is **4 dollars**.

### Query 1: `abab`

Initially, the new string is empty.

- Append `a` at a cost of 1 dollar.
- Append `b` at a cost of 1 dollar.
- Copy the substring `ab` and append it to the new string at no cost.

The total cost is **2 dollars**.
