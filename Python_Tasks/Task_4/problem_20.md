# HackerRank - No Idea!

## Problem Statement

You are given an array of integers and two disjoint sets, `A` and `B`.

- You like the integers in set `A`.
- You dislike the integers in set `B`.
- Your initial happiness is `0`.

For each integer in the array:
- If it belongs to `A`, increase happiness by `1`.
- If it belongs to `B`, decrease happiness by `1`.
- Otherwise, happiness remains unchanged.

Calculate and print the final happiness.

## Input Format

- The first line contains two integers `n` and `m`, representing the array length and the size of each set.
- The second line contains `n` integers representing the array.
- The third line contains the `m` elements of set `A`.
- The fourth line contains the `m` elements of set `B`.

## Output Format

Print the final happiness as a single integer.

## Sample Input

```text id="3z5j0r"
3 2
1 5 3
3 1
5 7
```

## Sample Output

```text id="x3j44z"
1
```

## Explanation

The array is `[1, 5, 3]`.

Set `A` is `{3, 1}` and set `B` is `{5, 7}`.

- `1` belongs to `A`, so happiness becomes `1`.
- `5` belongs to `B`, so happiness becomes `0`.
- `3` belongs to `A`, so happiness becomes `1`.

Final happiness = `1`.

## Python Solution

```python id="1p4h0n"
n, m = map(int, input().split())

arr = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)
```

## Concepts Used

- **Sets:** Store unique elements and support fast membership checks.
- **`in` operator:** Checks whether an element belongs to a set.
- **Conditional statements:** Decide whether happiness increases or decreases.
- **For loop:** Processes every integer in the array.
- **Accumulator:** Tracks the total happiness.

## Time Complexity

Approximately `O(n + m)` average time for reading the inputs and processing the array, assuming set membership checks take constant average time.

## HackerRank Problem Link

https://www.hackerrank.com/challenges/no-idea/problem

