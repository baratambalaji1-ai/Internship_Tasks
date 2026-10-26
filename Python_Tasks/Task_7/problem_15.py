# https://www.hackerrank.com/challenges/game-of-thrones/problem
import os
def gameOfThrones(s):
    odd = 0

    for ch in set(s):
        if s.count(ch) % 2 != 0:
            odd += 1

    return "YES" if odd <= 1 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

