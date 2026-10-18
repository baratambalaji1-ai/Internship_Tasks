# Company Logo

## Problem Statement

A newly opened multinational brand has decided to base its company logo on the three most common characters in the company name.

Given a string `s`, which is the company name in lowercase letters, your task is to find the **top three most common characters** in the string.

Print the three most common characters along with their occurrence counts.

- Sort the characters in descending order of occurrence count.
- If two or more characters have the same occurrence count, sort them in alphabetical order.

## Input Format

A single line of input containing the string `s`.

## Constraints

The string `s` has at least three distinct characters.

## Output Format

Print the three most common characters along with their occurrence counts, each on a separate line.

Sort the output in descending order of occurrence count. If the occurrence count is the same, sort the characters in alphabetical order.

## Sample Input 0

```text
aabbbccde
```

## Sample Output 0

```text
b 3
a 2
c 2
```

## Explanation

- `b` occurs 3 times, so it is printed first.
- Both `a` and `c` occur 2 times.
- Since `a` comes before `c` alphabetically, `a` is printed second and `c` third.

**Language:** Python 3

**Difficulty:** Medium
