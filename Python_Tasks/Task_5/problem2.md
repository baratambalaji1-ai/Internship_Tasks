# String Split and Join

In Python, a string can be split using a delimiter.

**Example:**

```python
a = "this is a string"
a = a.split(" ")
print(a)
```

Output:

```text
['this', 'is', 'a', 'string']
```

Joining a string is simple:

```python
a = "-".join(a)
print(a)
```

Output:

```text
this-is-a-string
```

## Task

You are given a string. Split the string on a space (`" "`) delimiter and join the words using a hyphen (`-`).

## Function Description

Complete the `split_and_join` function in the editor below.

`split_and_join` has the following parameter:

- `string line`: a string of space-separated words

**Returns**

- `string`: the resulting string

## Input Format

One line containing a string consisting of space-separated words.

## Sample Input

```text
this is a string
```

## Sample Output

```text
this-is-a-string
```
