# Set .discard(), .remove() & .pop()

## Problem Statement

You have a non-empty set `s`, and you have to execute `N` commands given in `N` lines.

The commands will be `pop`, `remove` and `discard`.

### Input Format

- The first line contains an integer `n`, the number of elements in set `s`.
- The second line contains `n` space-separated elements of set `s`. All elements are non-negative integers less than or equal to 9.
- The third line contains an integer `N`, the number of commands.
- The next `N` lines contain either `pop`, `remove` or `discard` commands, followed by their associated value when required.

### Constraints

As specified in the HackerRank problem.

### Output Format

Print the sum of the elements of set `s` on a single line.

### Sample Input

```text
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
```

### Sample Output

```text
4
```

### Explanation

After completing these 10 operations on the set, we get the final set. The sum of its elements is `4`.

**Note:** Convert the elements of set `s` to integers while assigning them. The first two lines of code are provided in the editor to ensure the proper input of the set.

**Language:** Python 3

**Difficulty:** Easy
