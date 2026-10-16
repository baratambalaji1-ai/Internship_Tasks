# HackerRank - What's Your Name?

## Problem Statement

You are given the first name and last name of a person on two different lines.

Read both names and print the following message:

`Hello firstname lastname! You just delved into python.`

Replace `firstname` and `lastname` with the given first and last names.

## Function Description

Complete the `print_full_name(first, last)` function.

**Parameters:**
- `first`: The person's first name.
- `last`: The person's last name.

**Output:**

Print the greeting with the first name and last name.

## Input Format

- The first line contains the first name.
- The second line contains the last name.

## Sample Input

```text
Ross
Taylor
```

## Sample Output

```text
Hello Ross Taylor! You just delved into python.
```

## Explanation

The first name is `Ross` and the last name is `Taylor`.

The function combines both names in the required greeting.

## Python Solution

```python
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first = input()
    last = input()
    print_full_name(first, last)
```

## Concepts Used

- Strings
- Functions
- Function parameters
- `input()`
- f-strings

## Problem Link

https://www.hackerrank.com/challenges/whats-your-name/problem
