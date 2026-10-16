# HackerRank - Set .add()

## Problem Statement

Rupal has a collection of country stamps. She wants to find the total number of **distinct countries** represented in the collection.

Given the names of the countries on the stamps, use a Python set to count the distinct countries.

## Input Format

- The first line contains an integer `n`, the total number of stamps.
- The next `n` lines contain the country names.

## Output Format

Print the total number of distinct countries.

## Sample Input

```text
7
UK
China
USA
France
New Zealand
UK
France
```

## Sample Output

```text
5
```

## Explanation

The country names are:

UK, China, USA, France, New Zealand, UK, France

UK and France appear more than once.

A Python set stores only unique values, so the distinct countries are:

UK, China, USA, France, New Zealand

Therefore, the answer is `5`.

## Python Solution

```python
n = int(input())
countries = set()

for _ in range(n):
    country = input()
    countries.add(country)

print(len(countries))
```

## Concepts Used

- **Set:** Stores unique elements and automatically removes duplicates.
- **`set.add()`:** Adds one element to a set.
- **`len()`:** Returns the number of elements in a set.
- **Loop:** Reads each country name.

## Time Complexity

`O(n)` average time, where `n` is the number of stamps.

## HackerRank Problem Link

https://www.hackerrank.com/challenges/py-set-add/problem

