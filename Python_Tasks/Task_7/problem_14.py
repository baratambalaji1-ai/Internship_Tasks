# https://www.hackerrank.com/challenges/anagram/problem
import os
from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    half = len(s) // 2
    first = Counter(s[:half])
    second = Counter(s[half:])

    changes = 0

    for ch in first:
        if first[ch] > second[ch]:
            changes += first[ch] - second[ch]

    return changes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()


