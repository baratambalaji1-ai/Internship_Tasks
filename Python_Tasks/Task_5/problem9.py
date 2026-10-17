# https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
freq = {}
for word in range(n):
    word = input()
    freq[word] = freq.get(word, 0) + 1


print(len(freq))
print(*freq.values())
    

