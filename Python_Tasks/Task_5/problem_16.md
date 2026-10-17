# collections.Counter()

## Problem Statement

A `Counter` is a container that stores elements as dictionary keys, with their counts stored as dictionary values.

### Sample Code

```python
from collections import Counter

myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]

print(Counter(myList))
print(Counter(myList).items())
print(Counter(myList).keys())
print(Counter(myList).values())
```

## Task

A shoe shop owner has a certain number of shoes in the shop. He has a list containing the size of each shoe available.

There are several customers who are willing to pay a certain amount of money only if they get a shoe of their desired size.

Your task is to calculate the total amount of money earned by the shoe shop owner.

## Input Format

- The first line contains an integer `N`, the number of shoes.
- The second line contains `N` space-separated integers representing the sizes of the shoes available in the shop.
- The third line contains an integer `X`, the number of customers.
- Each of the next `X` lines contains two space-separated integers:
  - The shoe size desired by the customer.
  - The price the customer is willing to pay for that shoe.

## Constraints

The input values satisfy the constraints specified in the original HackerRank problem.

## Output Format

Print the total amount of money earned by the shoe shop owner.

## Sample Input

```text
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
```

## Sample Output

```text
200
```

## Explanation

- Customer 1 purchased a size 6 shoe for $55.
- Customer 2 purchased a size 6 shoe for $45.
- Customer 3 could not purchase a size 6 shoe because it was no longer available.
- Customer 4 purchased a size 4 shoe for $40.
- Customer 5 purchased
