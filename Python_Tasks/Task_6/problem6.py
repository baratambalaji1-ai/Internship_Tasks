if __name__ == '__main__':
    n = int(input())
    n <= 150
    result = 0
    for i in range(1,n+1):
        temp = i
        digits = 1
        while temp >= 10:
            temp //= 10 
            digits *= 10  # 9900+100= 9899100
        result = result*(digits*10) + i
    print(result)
       
    

