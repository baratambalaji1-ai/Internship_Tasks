# No Idea!

## Problem Statement

There is an array of integers. There are also two disjoint sets, `A` and `B`, each containing distinct integers.

You like all the integers in set `A` and dislike all the integers in set `B`. Your initial happiness is `0`.

For each integer in the array:

- If the integer belongs to set `A`, add `1` to your happiness.
- If the integer belongs to set `B`, subtract `1` from your happiness.
- Otherwise, your happiness remains unchanged.

Since `A` and `B` are sets, they contain no repeated elements. However, the array may contain duplicate elements.

Your task is to calculate and output your final happiness.

## Input Format

- The first line contains two space-separated integers, `n` and `m`, representing the number of elements in the array and the number of elements in each set.
- The second line contains `n` space-separated integers representing the array.
- The third line contains `m` space-separated integers representing set `A`.
- The fourth line contains `m` space-separated integers representing set `B`.

## Constraints

The input values satisfy the constraints specified in the original HackerRank problem.

## Output Format

Output a single integer representing your total happiness.

## Sample Input

```text
3 2
1 5 3
3 1
5 7
```

## Sample Output

```text
1
```

## Explanation

- You gain `1` unit of happiness for each occurrence of `1` and `3` because they belong to set `A`.
- You lose `1` unit of happiness for `5` because it belongs to set `B`.
- The element `7` belongs to set `B` but does not appear in the array, so it does not affect your happiness.

Therefore, the total happiness is `1`.
