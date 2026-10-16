# HackerRank - String Validators

## Problem Statement

Python provides built-in string methods to check whether a string contains alphanumeric characters, alphabetical characters, digits, lowercase characters, and uppercase characters.

Given a string `s`, check whether it contains at least one character of each of the following types:

1. Alphanumeric
2. Alphabetical
3. Digits
4. Lowercase
5. Uppercase

## Input Format

A single line containing a string `s`.

## Output Format

Print five lines:

1. `True` if at least one character is alphanumeric; otherwise, `False`.
2. `True` if at least one character is alphabetical; otherwise, `False`.
3. `True` if at least one character is a digit; otherwise, `False`.
4. `True` if at least one character is lowercase; otherwise, `False`.
5. `True` if at least one character is uppercase; otherwise, `False`.

## Sample Input

```text
qA2
```

## Sample Output

```text
True
True
True
True
True
```

## Explanation

The string `qA2` contains:

- Alphanumeric characters: `q`, `A`, and `2`
- Alphabetical characters: `q` and `A`
- Digits: `2`
- Lowercase characters: `q`
- Uppercase characters: `A`

Therefore, all five outputs are `True`.

## Python Solution

```python
if __name__ == '__main__':
    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
```

## Concepts Used

- String methods: `isalnum()`, `isalpha()`, `isdigit()`, `islower()`, `isupper()`
- `any()` function
- Generator expressions
- Boolean values: `True` and `False`

## Problem Link

https://www.hackerrank.com/challenges/string-validators/problem
