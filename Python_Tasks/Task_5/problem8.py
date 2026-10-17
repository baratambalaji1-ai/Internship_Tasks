# https://www.hackerrank.com/challenges/py-set-add/problem
n = int(input())
countries = set()
for st in range(n):
    country = input()
    countries.add(country)
count = 0
for st in countries:
    count += 1
print(count)

