# Validating Phone Numbers

## Problem Statement

You are given a list of mobile phone numbers. Your task is to check whether each phone number is valid.

A valid mobile phone number must satisfy the following conditions:

- It must contain exactly **10 digits**.
- The first digit must be **7, 8, or 9**.
- It must contain only digits from `0` to `9`.

Print `YES` if the phone number is valid. Otherwise, print `NO`.

## Input Format

- The first line contains an integer `T`, the number of test cases.
- The next `T` lines contain one phone number each.

## Output Format

For each phone number, print `YES` if it is valid; otherwise, print `NO`.

## Sample Input

```text
2
9587456281
1252478965
```

## Sample Output

```text
YES
NO
```

## Explanation

- `9587456281` is valid because it contains 10 digits and starts with `9`.
- `1252478965` is invalid because it starts with `1`.

## Constraints

- Each phone number is provided as a string.
- A valid phone number contains exactly 10 digits and starts with `7`, `8`, or `9`.

