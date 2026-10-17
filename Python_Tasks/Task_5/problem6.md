# Introduction to Sets

A set is an unordered collection of elements without duplicate entries.

When printed, iterated over, or converted into a sequence, its elements may appear in any order.

## Example

```python
print(set())
print(set('HackerRank'))
print(set([1, 2, 1, 2, 3, 4, 5, 6, 0, 9, 12, 22, 3]))
print(set((1, 2, 3, 4, 5, 5)))
```

Sets are used for membership testing and eliminating duplicate entries.

## Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

**Formula:**

Average = Sum of distinct heights / Number of distinct heights

## Function Description

Complete the `average` function in the editor below.

`average` has the following parameter:

- `int arr`: an array of integers representing plant heights.

**Returns**

- `float`: the resulting average, rounded to 3 decimal places.

## Input Format

The first line contains the integer `N`, the size of the array.

The second line contains `N` space-separated integers representing the plant heights.

## Constraints

## Sample Input

```text
10
161 182 161 154 176 170 167 171 170 174
```

## Sample Output

```text
169.375
```

## Explanation

The set contains only the distinct plant heights. Using the `sum()` and `len()` functions, we can compute the average of those distinct heights.
