# HackerRank - Find the Runner-Up Score!

## Problem Statement

Given the scores of participants in a University Sports Day, find the runner-up score.

You are given `n` scores. Store them in a list and print the second-highest **distinct** score.

## Input Format

- The first line contains an integer `n`, the number of scores.
- The second line contains `n` integers separated by spaces.

## Constraints

- \(2 \leq n \leq 10\)
- Each score is between \(-100\) and \(100\).

## Output Format

Print the runner-up score.

## Sample Input

```text
5
2 3 6 6 5
```

## Sample Output

```text
5
```

## Explanation

The scores are `2, 3, 6, 6, 5`.

- Highest score: `6`
- Second-highest distinct score: `5`

Therefore, the runner-up score is `5`.

## Python Solution

```python
if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    unique_scores = list(set(scores))
    unique_scores.sort()

    print(unique_scores[-2])
```

## Concepts Used

- Lists
- `input()` and `split()`
- `map()` and `int()`
- Sets to remove duplicate scores
- `sort()` to arrange scores
- Negative indexing

## Problem Link

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
