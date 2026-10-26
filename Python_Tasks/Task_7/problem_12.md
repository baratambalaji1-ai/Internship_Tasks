# Making Anagrams

## Problem Statement

We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters with the same frequency.

For example, `bacdc` and `dcbac` are anagrams, but `bacdc` and `dcbad` are not.

Alice is taking a cryptography class and finding anagrams to be very useful. She decides on an encryption scheme involving two large strings where encryption depends on the minimum number of character deletions required to make the two strings anagrams.

Given two strings, `s1` and `s2`, that may not be of the same length, determine the minimum number of character deletions required to make them anagrams. Any characters can be deleted from either string.

## Function Description

Complete the `makingAnagrams` function.

### Parameters
- `s1`: A string.
- `s2`: Another string.

### Returns
- `int`: The minimum number of deletions needed.

## Input Format

- The first line contains a single string, `s1`.
- The second line contains a single string, `s2`.

## Constraints

- `s1` and `s2` consist of lowercase English letters, `ascii[a-z]`.

## Output Format

Print the minimum number of character deletions required to make the two strings anagrams.

## Sample Input

```text
cde
abc
```

## Sample Output

```text
4
```

## Explanation

Delete the following characters from the two strings to make them anagrams:

- Remove `d` and `e` from `cde` to get `c`.
- Remove `a` and `b` from `abc` to get `c`.

A total of **4 characters** must be deleted to make both strings anagrams.
