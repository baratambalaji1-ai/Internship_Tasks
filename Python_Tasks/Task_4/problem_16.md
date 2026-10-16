# HackerRank - Nested Lists

## Problem Statement

You are given the names and grades of students in a class.

Store the information in a nested list and print the name or names of students who have the **second-lowest grade**.

If multiple students have the second-lowest grade:
- Sort their names alphabetically.
- Print each name on a separate line.

## Input Format

- The first line contains an integer `n`, the number of students.
- For each student, the first line contains their name and the second line contains their grade.

## Output Format

Print the name or names of students with the second-lowest grade, in alphabetical order, one name per line.

## Sample Input

```text
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

## Sample Output

```text
Berry
Harry
```

## Explanation

The students and their grades are:

- Harry — 37.21
- Berry — 37.21
- Tina — 37.2
- Akriti — 41.0
- Harsh — 39.0

The lowest grade is `37.2`, belonging to Tina.

The second-lowest distinct grade is `37.21`, belonging to Harry and Berry.

After sorting their names alphabetically, the output is:

```text
Berry
Harry
```

## Python Solution

```python
if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = sorted(set(student[1] for student in students))
    second_lowest = grades[1]

    names = []

    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])

    names.sort()

    for name in names:
        print(name)
```

## Concepts Used

- **Nested list:** Stores each student's name and grade together.
- **`append()`:** Adds student information to the list.
- **`set()`:** Removes duplicate grades.
- **`sorted()`:** Sorts grades or names.
- **`float()`:** Converts the grade input into a decimal number.
- **List comprehension:** Extracts grades from student records.

## Time Complexity

Approximately `O(n log n)`, where `n` is the number of students, because sorting is required.

## HackerRank Problem Link

https://www.hackerrank.com/challenges/nested-list/problem

