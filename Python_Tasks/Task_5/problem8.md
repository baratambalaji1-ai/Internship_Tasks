# Set .add()

If we want to add a single element to an existing set, we can use the `.add()` operation.

It adds the element to the set and returns `None`.

## Example

```python
s = set('HackerRank')
s.add('H')
print(s)

print(s.add('HackerRank'))
print(s)
```

## Task

Apply your knowledge of the `.add()` operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help.

You pick the stamps one by one from a stack of `n` country stamps.

Find the total number of distinct country stamps.

## Input Format

- The first line contains an integer, `n`, the total number of country stamps.
- The next `n` lines contain the name of the country where each stamp is from.

## Constraints

## Output Format

Output the total number of distinct country stamps on a single line.

## Sample Input

```text
7
UK
China
USA
France
New Zealand
UK
France
```

## Sample Output

```text
5
```

## Explanation

UK and France each appear twice. Therefore, the total number of distinct country stamps is five.
