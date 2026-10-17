# HackerRank: Piling Up!

## Problem Statement

There is a horizontal row of cubes, and the length of each cube is given. Your task is to create a vertical pile of cubes following this rule:

If cube `b` is placed on top of cube `a`, then `b <= a`.

You can pick up only the **leftmost or rightmost cube** from the row at each step.

Print `Yes` if it is possible to build the pile according to the rule. Otherwise, print `No`.

## Input Format

- The first line contains an integer `T`, the number of test cases.
- For each test case:
  - The first line contains an integer `n`, the number of cubes.
  - The second line contains `n` space-separated integers representing the side lengths of the cubes.

## Output Format

For each test case, print `Yes` if the cubes can be stacked according to the rule. Otherwise, print `No`.

## Constraints

- The number of test cases, cubes, and cube side lengths follow the constraints given in the problem statement.

## Sample Input

```text
2
6
4 3 2 1 3 4
3
1 3 2
```

## Sample Output

```text
Yes
No
```

## Explanation

**Test Case 1:** The cubes can be selected from the left and right ends in an order that allows each cube placed above another to be no larger than the cube below it.

**Test Case 2:** It is impossible to create a valid pile using only the leftmost or rightmost cube at each step.


