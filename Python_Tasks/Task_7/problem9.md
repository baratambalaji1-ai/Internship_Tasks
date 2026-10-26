# Beautiful Binary String

## Problem Statement

Alice has a binary string. She thinks a binary string is beautiful if and only if it does not contain the substring `010`.

In one step, Alice can change a `0` to a `1` or vice versa.

Given a binary string, count and print the minimum number of steps needed to make the string beautiful.

## Function Description

Complete the `beautifulBinaryString` function.

### Parameters
- `b`: A string of binary digits.

### Returns
- `int`: The minimum number of moves required.

## Input Format

- The first line contains an integer `n`, the length of the binary string.
- The second line contains a single binary string `b`.

## Constraints

- `1 ≤ n ≤ 100`

## Output Format

Print the minimum number of steps needed to make the string beautiful.

## Sample Input 0

```text
7
0101010
```

## Sample Output 0

```text
2
```

## Explanation 0

The string `0101010` contains the substring `010` multiple times.

By changing two characters, we can remove all occurrences of `010` and make the string beautiful.

## Sample Input 1

```text
5
01100
```

## Sample Output 1

```text
0
```

## Explanation 1

The substring `010` does not occur in `01100`. Therefore, the string is already beautiful, and no moves are required.

## Sample Input 2

```text
10
0100101010
```

## Sample Output 2

```text
3
```

## Explanation 2

The minimum number of changes required to remove all occurrences of `010` from the string is `3`.
