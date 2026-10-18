# Set .union() Operation

## Problem Statement

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set contains the roll numbers of students who have subscribed to the English newspaper, and the other set contains the roll numbers of students who have subscribed to the French newspaper.

The same student may appear in both sets.

Your task is to find the total number of students who have subscribed to **at least one newspaper**.

## Input Format

- The first line contains an integer, `n`, the number of students who have subscribed to the English newspaper.
- The second line contains `n` space-separated roll numbers of those students.
- The third line contains an integer, `m`, the number of students who have subscribed to the French newspaper.
- The fourth line contains `m` space-separated roll numbers of those students.

## Constraints

As specified in the HackerRank problem.

## Output Format

Output the total number of students who have at least one newspaper subscription.

## Sample Input

```text
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

## Sample Output

```text
13
```

## Explanation

The students who subscribed to at least one newspaper have the following roll numbers:

`1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 55`

Roll numbers `1, 2, 3, 6, 8` appear in both sets, so each is counted only once.

Hence, the total number of students is `13`.

**Language:** Python 3

**Difficulty:** Easy
