# HackerRank - Introduction to Sets

## Problem Statement

A set is an unordered collection of unique elements. It automatically removes duplicate values.

Ms. Gabriel Williams, a botany professor, asks Mickey to calculate the average height of all plants using only their distinct heights.

Complete the `average(array)` function to calculate the average of the distinct heights, rounded to three decimal places.

## Function Description

Complete the `average(array)` function.

**Parameter:**
- `array`: A list of integers representing plant heights.

**Returns:**
- A float representing the average of the distinct heights, rounded to three decimal places.

## Input Format

- The first line contains an integer `N`, the number of plant heights.
- The second line contains `N` space-separated integers representing the heights.

## Sample Input

```text id="b62q5u"
10
161 182 161 154 176 170 167 171 170 174
```

## Sample Output

```text id="x9x4s1"
169.375
```

## Explanation

The distinct plant heights are:

`{161, 182, 154, 176, 170, 167, 171, 174}`

Their sum is `1355`, and there are `8` distinct heights.

Average = `1355 / 8 = 169.375`

Therefore, the output is `169.375`.

## Python Solution

```python
def average(array):
    distinct_heights = set(array)
    return round(sum(distinct_heights) / len(distinct_heights), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
```

## Concepts Used

- Sets and duplicate removal
- `set()` function
- `sum()` function
- `len()` function
- `round()` function
- Lists and `map()`

## Problem Link

https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
