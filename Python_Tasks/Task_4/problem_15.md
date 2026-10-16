# HackerRank - Word Order

## Problem Statement

You are given `n` words. Some words may appear more than once.

Your task is to:
1. Count the number of distinct words.
2. Count how many times each distinct word appears.
3. Print the occurrence counts in the order in which each word first appeared.

## Input Format

- The first line contains an integer `n`, the number of words.
- The next `n` lines each contain one word.

## Output Format

- The first line contains the number of distinct words.
- The second line contains the occurrence count of each distinct word, in order of first appearance.

## Sample Input

```text
4
bcdef
abcdefg
bcde
bcdef
```

## Sample Output

```text
3
2 1 1
```

## Explanation

The words appear in this order:

- `bcdef` — appears 2 times.
- `abcdefg` — appears 1 time.
- `bcde` — appears 1 time.

There are 3 distinct words.

Therefore, the output is:

```text
3
2 1 1
```

## Python Solution

```python
n = int(input())
freq = {}

for _ in range(n):
    word = input()
    freq[word] = freq.get(word, 0) + 1

print(len(freq))
print(*freq.values())
```

## Concepts Used

- **Dictionary:** Stores words as keys and their frequencies as values.
- **`get()`:** Returns the current count, or `0` if the word is not present.
- **`len()`:** Counts the distinct dictionary keys.
- **`values()`:** Retrieves the occurrence counts in insertion order.
- **`*` unpacking:** Prints the counts separated by spaces.

## Time Complexity

`O(n)` average time for processing `n` words, assuming dictionary operations take constant average time.

## HackerRank Problem Link

https://www.hackerrank.com/challenges/word-order/problem

