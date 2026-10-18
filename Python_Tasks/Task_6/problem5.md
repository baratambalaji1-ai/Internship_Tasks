# Write a function

## Problem Statement

An extra day is added to the calendar almost every four years as February 29. This day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the Sun. A year containing a leap day is called a leap year.

In the Gregorian calendar, three conditions are used to identify leap years:

1. If the year is evenly divisible by 4, it is a leap year, unless:
2. The year is evenly divisible by 100, in which case it is NOT a leap year, unless:
3. The year is also evenly divisible by 400. Then it is a leap year.

For example, 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are not leap years.

## Task

Given a year, determine whether it is a leap year.

If it is a leap year, return the Boolean value `True`; otherwise, return `False`.

The provided code stub reads the year from STDIN and passes it to the `is_leap` function. Complete only the `is_leap` function.

## Input Format

Read an integer, `year`, representing the year to test.

## Constraints

- \(1900 \leq year \leq 10^5\)

## Output Format

The function must return a Boolean value (`True` or `False`). Output is handled by the provided code stub.

## Sample Input 0

```text
1990
```

## Sample Output 0

```text
False
```

## Explanation 0

1990 is not a multiple of 4, so it is not a leap year.
