# https://www.hackerrank.com/challenges/py-the-captains-room/problem
k = int(input()) # number of rooms
rooms = list(map(int, input().split())) # room number
a = set()
b = set()
for room in rooms:
    if room not in a:
        a.add(room)
        b.add(room)
    else:
        b.discard(room)
for i in b:
    print(i)

