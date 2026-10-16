# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    res = list(set(array))
    add = 0
    count = 0
    for num in res:
        add += num
        count += 1
    result = add/count
    return result
        
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
