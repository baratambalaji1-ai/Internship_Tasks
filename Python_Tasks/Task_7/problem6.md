# Pangrams

## Problem
A pangram is a string that contains every letter of the English alphabet (`a` to `z`). Given a sentence, determine whether it is a pangram. Ignore uppercase and lowercase differences.

Return `pangram` if the string contains every letter of the alphabet. Otherwise, return `not pangram`.

## Function Description
Complete the function `pangrams(s)`.

**Parameter:**
- `s`: A string to test.

**Returns:**
- `pangram` or `not pangram`

## Sample Input 0
```text
We promptly judged antique ivory buckles for the next prize
```

## Sample Output 0
```text
pangram
```

## Sample Input 1
```text
We promptly judged antique ivory buckles for the prize
```

## Sample Output 1
```text
not pangram
```

## Explanation
- **Sample 0:** All 26 letters of the English alphabet are present.
- **Sample 1:** The letter `x` is missing.
