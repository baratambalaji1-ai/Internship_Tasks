# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    winner = float('-inf')
    runner = float('-inf')
    for num in arr:
        if num > winner:
            runner = winner
            winner = num
        elif num > runner and num != winner:
            runner = num
    print(runner)

