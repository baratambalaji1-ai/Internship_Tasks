# https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    r = s.split(' ')
    result = []
    for word in r:
        if word:
            word = word.capitalize()
            result.append(word)
        else:
            result.append('')
    return ' '.join(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

