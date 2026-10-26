# https://www.hackerrank.com/challenges/pangrams/problem
def pangrams(s):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for ch in alphabets:
        if ch not  in s.lower():
            return 'not pangram'
    return 'pangram'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

