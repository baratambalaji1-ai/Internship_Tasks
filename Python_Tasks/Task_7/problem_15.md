# Game of Thrones - I

## Problem Statement

The Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of this conspiracy from a raven and plans to lock the single door through which the enemy can enter his kingdom.

To lock the door, he needs a key that is an anagram of a palindrome. He starts going through his box of strings, checking whether they can be rearranged into a palindrome.

Given a string `s`, determine whether its characters can be rearranged to form a palindrome. Return `YES` or `NO`.

## Function Description

Complete the `gameOfThrones` function.

### Parameter
- `s`: A string to analyze.

### Returns
- `string`: Either `YES` or `NO`.

## Input Format

A single line containing the string `s`.

## Constraints

- `1 ≤ |s| ≤ 10⁵`
- `s` contains only lowercase English letters (`a-z`).

## Output Format

Print `YES` if the string can be rearranged into a palindrome. Otherwise, print `NO`.

## Sample Input 0

```text
aaabbbb
```

## Sample Output 0

```text
YES
```

## Explanation 0

One possible palindromic arrangement of the given string is:

```text
bbaaabb
```

## Sample Input 1

```text
cdefghmnopqrstuvw
```

## Sample Output 1

```text
NO
```

## Explanation 1

Palindromes longer than one character are made up of pairs of characters, with at most one character appearing an odd number of times.

In this string, multiple characters appear an odd number of times, so it cannot be rearranged into a palindrome.

## Sample Input 2

```text
cdcdcdcdeeeef
```

## Sample Output 2

```text
YES
```

## Explanation 2

One possible palindrome that can be formed from the string is:

```text
ddcceefeeccdd
```
