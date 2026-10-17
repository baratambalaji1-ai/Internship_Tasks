# Symmetric Difference

## Objective

Today, we're learning about a new data type: sets.

## Concept

If inputs are given on one line separated by a delimiter, use `split()` to get the separate values in the form of a list. The default delimiter is a space.

```python
a = input()
lis = a.split()
print(lis)
```

If the list values are integers, use `map()` to convert the strings to integers.

```python
newlis = list(map(int, lis))
print(newlis)
```

Sets are unordered collections of unique values. A single set contains values of immutable data types.

## Creating Sets

```python
myset = {1, 2}
myset = set()
myset = set(['a', 'b'])
```

## Modifying Sets

Using `add()`:

```python
myset.add('c')
myset.add('a')
```

Using `update()`:

```python
myset.update([1, 2, 3, 4])
myset.update({1, 7, 8})
```

## Removing Items

The `discard()` and `remove()` functions remove a value from a set. If the value is absent, `discard()` does nothing, whereas `remove()` raises a `KeyError`.

```python
myset.discard(10)
myset.remove(13)
```

## Common Set Operations

```python
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
```

- `a.union(b)`: Values that exist in either set.
- `a.intersection(b)`: Values that exist in both sets.
- `a.difference(b)`: Values
