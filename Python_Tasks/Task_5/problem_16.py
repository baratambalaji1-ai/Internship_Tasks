# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

n = int(input())
my_list = list(map(int, input().split()))

shoe_count = Counter(my_list)

x = int(input())
total = 0

for i in range(x):
    size, price = map(int, input().split())

    if shoe_count[size] > 0:
        total += price
        shoe_count[size] -= 1

print(total)

