# Designer Door Mat

## Problem

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

- The mat size must be `N × M`, where `N` is an odd natural number and `M` is `3` times `N`.
- The design should have `WELCOME` written in the center.
- The design pattern should only use `|`, `.` and `-` characters.

## Sample Designs

**Size: 7 × 21**

```text
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
```

**Size: 11 × 33**

```text
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
```

## Input Format

A single line containing the space-separated values of `N` and `M`.

## Constraints

- `N` is an odd natural number.
- `M` is `3` times `N`.

## Output Format

Output the designed door mat pattern.

## Sample Input

```text
9 27
```

## Sample Output

```text
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
```
