# The Minion Game – HackerRank (Python)

## Problem Description
Kevin and Stuart play a game using an uppercase string.

- **Stuart** creates substrings that start with consonants.
- **Kevin** creates substrings that start with vowels (`A`, `E`, `I`, `O`, `U`).
- Each occurrence of a substring earns one point.

The task is to calculate each player's score and print the winner.

## Approach
Instead of generating every possible substring, we calculate the score directly.

For each character at index `i`:

- Calculate the number of substrings starting at that position using `len(string) - i`.
- If the character is a vowel, add those points to Kevin.
- Otherwise, add those points to Stuart.

This approach avoids nested loops and is more efficient for long strings.

## Python Solution

```python
def minion_game(string):
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        points = n - i

        if string[i] in "AEIOU":
            kevin += points
        else:
            stuart += points

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
```

## Sample Input

```text
BANANA
```

## Sample Output

```text
Stuart 12
```

## Complexity Analysis
- **Time Complexity:** `O(n)`
- **Auxiliary Space Complexity:** `O(1)`

## Platform
HackerRank – Python – Strings

## Concepts Practiced
- String indexing
- Substrings
- Loops and conditional statements
- String processing
- Time complexity optimization

