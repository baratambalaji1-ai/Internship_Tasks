# https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a =set(map(int, input().split()))
N = int(input())
b =set(map(int, input().split()))
result = []
for num in a:
    if num not in b:
        result.append(num)
      
for num in b:
    if num not in a:
        result.append(num)
     
result = sorted(result)

for num in result:
    print(num)

