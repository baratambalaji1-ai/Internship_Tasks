# CamelCase

## Problem Statement

There is a sequence of words in CamelCase as a string of letters, `s`, having the following properties:

- It is a concatenation of one or more words consisting of English letters.
- All letters in the first word are lowercase.
- For each of the subsequent words, the first letter is uppercase and the rest of the letters are lowercase.

Given `s`, determine the number of words in `s`.

## Function Description

Complete the `camelcase` function.

### Parameter
- `s`: The string to analyze.

### Returns
- `int`: The number of words in `s`.

## Input Format

A single line containing the string `s`.

## Constraints

- `1 ≤ length of s ≤ 10⁵`

## Output Format

Print the number of words in the string.

## Sample Input

```text
saveChangesInTheEditor
```

## Sample Output

```text
5
```

## Explanation

The string contains five words:

1. save
2. Changes
3. In
4. The
5. Editor
