# Merge the Tools! – HackerRank (Python)

## Problem Description

You are given a string `s` and an integer `k`. Divide the string into substrings of length `k`. For each substring, remove duplicate characters while maintaining the original order of the remaining characters.

Print each resulting string on a separate line.

## Example

**Input**
```text
AABCAAADA
3
```

**Output**
```text
AB
CA
AD
```

## Explanation

The string `AABCAAADA` is divided into three substrings of length 3:

- `AAB` → `AB`
- `CAA` → `CA`
- `ADA` → `AD`

Repeated characters are removed from each substring, while the order of distinct characters is preserved.

## Python Solution

```python
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        result = ""

        for char in substring:
            if char not in result:
                result += char

        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
```

## Concepts Practiced

- Python strings
- String slicing
- `for` loops
- Conditional statements
- Removing duplicate characters
- Preserving character order

## Complexity Analysis

- **Time Complexity:** `O(n × k)` for this implementation in the worst case, where `n` is the length of the input string and `k` is the group size.
- **Auxiliary Space Complexity:** `O(k)` for the temporary substring and result.

## Platform

HackerRank – Python – Strings

