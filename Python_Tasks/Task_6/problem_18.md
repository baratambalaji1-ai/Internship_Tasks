# Set Mutations

## Problem Statement

We have seen the applications of union, intersection, difference, and symmetric difference operations. However, these operations do not make any changes to the original set.

We can use the following operations to modify a set:

- **`update()` or `|=`**: Adds elements from another set or iterable.
- **`intersection_update()` or `&=`**: Keeps only the elements common to both sets.
- **`difference_update()` or `-=`**: Removes elements found in another set.
- **`symmetric_difference_update()` or `^=`**: Keeps elements found in either set, but not in both.

## Task

You are given a set `A` and `N` other sets. These `N` sets must perform specific mutation operations on set `A`.

Your task is to execute the given operations in order and print the sum of the elements remaining in set `A`.

## Input Format

- The first line contains the number of elements in set `A`.
- The second line contains the space-separated elements of set `A`.
- The third line contains an integer `N`, the number of other sets.
- The next `N` operations are divided into two lines each:
  - The first line contains the operation name and the number of elements in the other set.
  - The second line contains the space-separated elements of the other set.

## Constraints

As specified in the HackerRank problem.

## Output Format

Print the sum of the elements in set `A` after performing all the operations.

## Sample Input

```text
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
```

## Sample Output

```text
38
```

## Explanation

After performing all four mutation operations in the given order, the sum of the elements remaining in set `A` is `38`.

**Language:** Python 3

**Difficulty:** Easy
