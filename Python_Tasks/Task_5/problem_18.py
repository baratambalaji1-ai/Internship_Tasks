# https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):

    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        points = n - i

        if string[i] in "AEIOU":
            kevin += points
        else:
            stuart += points

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")


    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)
