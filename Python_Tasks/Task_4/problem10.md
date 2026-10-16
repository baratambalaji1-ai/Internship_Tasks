# HackerRank - Find a String

## Problem Statement

Given a string and a substring, find how many times the substring occurs in the original string.

String traversal must take place from left to right. The search is case-sensitive.

**Note:** Overlapping occurrences must also be counted.

## Input Format

- The first line contains the original string.
- The second line contains the substring.

## Output Format

Print the total number of occurrences of the substring in the original string.

## Sample Input

```text
ABCDCDC
CDC
```

## Sample Output

```text
2
```

## Explanation

The substring `CDC` occurs twice in `ABCDCDC`:

- First occurrence: `ABCDCDC`
- Second occurrence: `ABCDCDC`

Therefore, the output is `2`.

## Python Solution

```python
def count_substring(string, sub_string):
    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
```

## Concepts Used

- Strings and substrings
- `len()` function
- `for` loop
- String slicing
- Conditional statements
- Counting occurrences

## Problem Link

https://www.hackerrank.com/challenges/find-a-string/problem
