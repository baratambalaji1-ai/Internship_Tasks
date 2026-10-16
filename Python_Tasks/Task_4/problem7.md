# HackerRank - String Split and Join

## Problem Statement

In Python, a string can be split using a delimiter and joined using another delimiter.

Given a string containing space-separated words, split the string using spaces and join the words using a hyphen (`-`).

## Function Description

Complete the `split_and_join(line)` function.

**Parameter:**
- `line`: A string containing space-separated words.

**Returns:**
- A string with the words joined using hyphens.

## Input Format

One line containing a string consisting of space-separated words.

## Sample Input

```text
this is a string
```

## Sample Output

```text
this-is-a-string
```

## Explanation

The input string is:

`this is a string`

First, split it into a list:

`['this', 'is', 'a', 'string']`

Then, join the words using a hyphen:

`this-is-a-string`

## Python Solution

```python
def split_and_join(line):
    words = line.split()
    result = '-'.join(words)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
```

## Concepts Used

- Strings
- `split()` method
- `join()` method
- Functions and return values

## Problem Link

https://www.hackerrank.com/challenges/python-string-split-and-join/problem
