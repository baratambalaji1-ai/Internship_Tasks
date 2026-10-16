# HackerRank - Mutations

## Problem Statement

Strings in Python are immutable, which means their characters cannot be changed directly.

Given a string, an index position, and a character, change the character at the specified position and print the modified string.

## Function Description

Complete the `mutate_string(string, position, character)` function.

**Parameters:**
- `string`: The original string.
- `position`: The index of the character to change.
- `character`: The new character.

**Returns:**

The modified string.

## Input Format

- The first line contains a string.
- The second line contains an integer `position` and a character, separated by a space.

## Sample Input

```text
abracadabra
5 k
```

## Sample Output

```text
abrackdabra
```

## Explanation

The original string is `abracadabra`.

The character at index `5` is `a`. We replace it with `k`.

The modified string becomes `abrackdabra`.

## Python Solution

```python
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
```

## Concepts Used

- Strings and immutability
- String slicing
- Function parameters and return values
- `input()` and `split()`
- String concatenation

## Problem Link

https://www.hackerrank.com/challenges/python-mutations/problem
