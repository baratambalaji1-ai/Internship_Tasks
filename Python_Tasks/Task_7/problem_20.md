# Super Reduced String

## Problem Statement

Reduce a string of lowercase English letters (`a` to `z`) by performing a series of operations.

In each operation, select a pair of adjacent letters that are identical and delete them.

Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return `Empty String`.

## Function Description

Complete the `superReducedString` function.

### Parameter
- `s`: A string to reduce.

### Returns
- `string`: The reduced string or `Empty String` if the result is empty.

## Input Format

A single string `s`.

## Constraints

- `s` contains lowercase English letters (`a` to `z`).

## Output Format

Print the reduced string. If the string becomes empty, print `Empty String`.

## Sample Input 0

```text
aaabccddd
```

## Sample Output 0

```text
abd
```

## Explanation 0

Perform the following operations to get the final string:

```text
aaabccddd → abccddd → abddd → abd
```

## Sample Input 1

```text
aa
```

## Sample Output 1

```text
Empty String
```

## Explanation 1

```text
aa → Empty String
```

## Sample Input 2

```text
baab
```

## Sample Output 2

```text
Empty String
```

## Explanation 2

```text
baab → bb → Empty String
```
