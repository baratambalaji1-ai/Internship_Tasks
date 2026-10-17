# String Validators

Python has built-in string validation methods for checking whether a string contains alphabetical characters, alphanumeric characters, digits, lowercase characters, uppercase characters, etc.

## `str.isalnum()`

Checks if all characters are alphanumeric (`a-z`, `A-Z`, and `0-9`).

```python
'ab123'.isalnum()   # True
'ab123#'.isalnum()  # False
```

## `str.isalpha()`

Checks if all characters are alphabetical (`a-z` and `A-Z`).

```python
'abcD'.isalpha()   # True
'abcd1'.isalpha()  # False
```

## `str.isdigit()`

Checks if all characters are digits (`0-9`).

```python
'1234'.isdigit()   # True
'123edsd'.isdigit()  # False
```

## `str.islower()`

Checks if all cased characters are lowercase.

```python
'abcd123#'.islower()  # True
'Abcd123#'.islower()  # False
```

## `str.isupper()`

Checks if all cased characters are uppercase.

```python
'ABCD123#'.isupper()  # True
'Abcd123#'.isupper()  # False
```

## Task

You are given a string `s`.

Your task is to find out if the string contains:

1. Alphanumeric characters
2. Alphabetical characters
3. Digits
4. Lowercase characters
5. Uppercase characters

## Input Format

A single line containing a string, `s`.

## Constraints

## Output Format

Print five lines:

1. `True` if `s` contains at least one alphanumeric character; otherwise, print `False`.
2. `True` if `s` contains at least one alphabetical character; otherwise, print `False`.
3. `True` if `s` contains at least one digit; otherwise, print `False`.
4. `True` if `s` contains at least one lowercase character; otherwise, print `False`.
5. `True` if `s` contains at least one uppercase character; otherwise, print `False`.

## Sample Input

```text
qA2
```

## Sample Output

```text
True
True
True
True
True
```
