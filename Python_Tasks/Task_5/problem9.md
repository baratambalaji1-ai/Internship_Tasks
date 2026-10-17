# Word Order

You are given `n` words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond to the order in which each word first appears in the input.

**Note:** Each input line ends with a newline character.

## Constraints

The sum of the lengths of all the words does not exceed the specified limit.

All the words are composed of lowercase English letters only.

## Input Format

- The first line contains the integer `n`.
- The next `n` lines each contain a word.

## Output Format

Output two lines:

- On the first line, output the number of distinct words in the input.
- On the second line, output the number of occurrences of each distinct word, in order of first appearance.

## Sample Input

```text id="c85g0v"
4
bcdef
abcdefg
bcde
bcdef
```

## Sample Output

```text id="gq2nps"
3
2 1 1
```

## Explanation

There are three distinct words.

- `bcdef` appears twice.
- `abcdefg` appears once.
- `bcde` appears once.

The order of first appearances is `bcdef`, `abcdefg`, and `bcde`, so the output is `2 1 1`.
