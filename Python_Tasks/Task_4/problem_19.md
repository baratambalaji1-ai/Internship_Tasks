# HackerRank - collections.Counter()

## Problem Statement

A shoe shop owner has a collection of shoes of different sizes. Customers arrive and offer a price for a particular shoe size.

A customer can purchase a shoe only if their requested size is available.

Calculate the total money earned by the shop owner.

## Input Format

- The first line contains an integer `n`, the number of shoes.
- The second line contains `n` space-separated shoe sizes.
- The third line contains an integer `x`, the number of customers.
- The next `x` lines each contain two integers: the desired shoe size and the price offered.

## Output Format

Print the total money earned.

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

- Customer 1 buys size 6 for 55.
- Customer 2 buys size 6 for 45.
- Customer 3 cannot buy size 6 because both size 6 shoes have been sold.
- Customer 4 buys size 4 for 40.
- Customer 5 buys size 18 for 60.
- Customer 6 cannot buy size 10 because it is unavailable.

Total earnings = `55 + 45 + 40 + 60 = 200`.

## Python Solution

```python
from collections import Counter

n = int(input())
shoe_sizes = list(map(int, input().split()))

shoe_count = Counter(shoe_sizes)

x = int(input())
total = 0

for _ in range(x):
    size, price = map(int, input().split())

    if shoe_count[size] > 0:
        total += price
        shoe_count[size] -= 1

print(total)
```

## Concepts Used

- **`Counter`:** Counts how many times each shoe size appears.
- **Dictionary-style access:** `shoe_count[size]` gives the remaining count for a shoe size.
- **Condition:** Checks whether the requested shoe is available.
- **Accumulation:** `total += price` adds the purchase price to the earnings.
- **Decrement:** `shoe_count[size] -= 1` reduces the available quantity after a sale.

## Time Complexity

`O(n + x)` average time, where `n` is the number of shoes and `x` is the number of customers.

## HackerRank Problem Link

https://www.hackerrank.com/challenges/collections-counter/problem

