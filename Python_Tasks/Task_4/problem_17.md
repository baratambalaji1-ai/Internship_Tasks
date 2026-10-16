# HackerRank - Finding the Percentage

## Problem Statement

You are given the names and marks of students. Store each student's marks in a dictionary.

Given a student's name, calculate the average of their marks and print it with exactly two decimal places.

## Input Format

- The first line contains an integer `n`, the number of students.
- The next `n` lines contain a student's name followed by their marks, separated by spaces.
- The final line contains `query_name`, the name of the student whose average must be calculated.

## Output Format

Print the student's average marks, formatted to exactly two decimal places.

## Sample Input

```text
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

## Sample Output

```text
56.00
```

## Explanation

Malika's marks are `52`, `56`, and `60`.

Total marks:

`52 + 56 + 60 = 168`

Number of marks: `3`

Average:

`168 / 3 = 56`

Formatted to two decimal places, the answer is `56.00`.

## Python Solution

```python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *marks = input().split()
        student_marks[name] = list(map(float, marks))

    query_name = input()

    marks = student_marks[query_name]
    average = sum(marks) / len(marks)

    print(f"{average:.2f}")
```

## Concepts Used

- **Dictionary:** Stores each student's name and marks.
- **`input().split()`:** Reads a line and separates it into values.
- **`map(float, marks)`:** Converts marks into numbers, including decimal values.
- **`sum()`:** Calculates the total marks.
- **`len()`:** Counts the number of marks.
- **f-string formatting:** `:.2f` prints exactly two digits after the decimal point.

## Time Complexity

`O(n × m)` to read and store all marks, where `n` is the number of students and `m` is the average number of marks per student. Calculating the queried student's average takes time proportional to their number of marks.

## HackerRank Problem Link

https://www.hackerrank.com/challenges/finding-the-percentage/problem

