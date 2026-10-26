# Caesar Cipher

## Problem Statement

Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of positions in the alphabet. If the shift takes you past the end of the alphabet, rotate back to the beginning.

For example, with a rotation of `3`:

- `w` becomes `z`
- `x` becomes `a`
- `y` becomes `b`
- `z` becomes `c`

Original alphabet:

```text
abcdefghijklmnopqrstuvwxyz
```

Alphabet rotated by `+3`:

```text
defghijklmnopqrstuvwxyzabc
```

The cipher only encrypts letters. Symbols, such as `-`, remain unchanged.

Given a string and a rotation factor, encrypt the string using Caesar's cipher.

## Function Description

Complete the `caesarCipher` function.

### Parameters
- `s`: The unencrypted string.
- `k`: The number of positions to rotate the alphabet.

### Returns
- `string`: The encrypted string.

## Input Format

- The first line contains an integer `n`, the length of the unencrypted string.
- The second line contains the unencrypted string `s`.
- The third line contains an integer `k`, the number of positions to rotate the alphabet.

## Constraints

- `1 ≤ n ≤ 100`
- `0 ≤ k ≤ 100`
- `s` is a valid ASCII string without spaces.

## Output Format

Print the encrypted string.

## Sample Input

```text
11
middle-Outz
2
```

## Sample Output

```text
okffng-Qwvb
```

## Explanation

The alphabet is rotated by `+2`:

```text
abcdefghijklmnopqrstuvwxyz
cdefghijklmnopqrstuvwxyzab
```

Each letter is shifted two positions forward:

```text
m → o
i → k
d → f
d → f
l → n
e → g
- → -
O → Q
u → w
t → v
z → b
```

The encrypted string is `okffng-Qwvb`.
