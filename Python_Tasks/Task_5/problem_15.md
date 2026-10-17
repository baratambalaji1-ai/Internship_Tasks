# Lists

## Problem Statement

Consider an empty list `my_list = []`. You can perform the following commands:

- `insert i e`: Insert integer `e` at position `i`.
- `print`: Print the list.
- `remove e`: Remove the first occurrence of integer `e`.
- `append e`: Add integer `e` to the end of the list.
- `sort`: Sort the list in ascending order.
- `pop`: Remove the last element from the list.
- `reverse`: Reverse the order of the list.

Initialize an empty list and read an integer `N`, followed by `N` lines of commands. Iterate through each command in order and perform the corresponding operation on the list.

## Input Format

- The first line contains an integer `N`, denoting the number of commands.
- Each of the next `N` lines contains one of the commands described above.

## Constraints

- All elements added to the list must be integers.

## Output Format

For each command of type `print`, print the list on a new line.

## Sample Input 0

```text
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```

## Sample Output 0

```text
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```
