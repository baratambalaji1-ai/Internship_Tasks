# Anagram

## Problem Statement

Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string `s`, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings anagrams of one another.

## Function Description

Complete the `anagram` function.

### Parameter
- `s`: A string.

### Returns
- `int`: The minimum number of characters to change, or `-1` if it is impossible.

## Input Format

- The first line contains an integer `q`, the number of test cases.
- Each test case contains a string `s`.

## Constraints

- `s` consists only of characters in the range `ascii[a-z]`.

## Output Format

For each test case, print the minimum number of characters that must be changed to make the two substrings anagrams of one another. If it is impossible, print `-1`.

## Sample Input

```text
6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx
```

## Sample Output

```text
3
1
-1
2
0
1
```

## Explanation

**Test Case 1:** Split `aaabbb` into `aaa` and `bbb`. We must replace all three characters in the first substring with `b` to make the two substrings anagrams.

**Test Case 2:** Split `ab` into `a` and `b`. Change `a` to `b` to make the substrings anagrams.

**Test Case 3:** The string `abc` has an odd length, so it cannot be split into two equal-length substrings. The answer is `-1`.

**Test Case 4:** Split `mnop` into `mn` and `op`. Change both characters in the first substring to match the character frequencies of the second substring. The answer is `2`.

**Test Case 5:** Split `xyyx` into `xy` and `yx`. They are already anagrams, so the answer is `0`.

**Test Case 6:** Split `xaxbbbxx` into `xaxb` and `bbxx`. Change `a` to `b` in the first substring to make them anagrams. The answer is `1`.
