# The Captain's Room

## Problem Statement

Mr. Anant Asankhya is the manager of the INFINITE hotel. The hotel has an infinite number of rooms.

One fine day, a finite number of tourists come to stay at the hotel.

The tourists consist of:
- A Captain.
- An unknown number of families, each consisting of **K** members, where **K ≠ 1**.

The Captain is given a separate room, and the rest of the tourists are given one room per family.

Mr. Anant has an unordered list of randomly arranged room entries. The list contains the room numbers of all the tourists. Each family's room number appears **K** times, while the Captain's room number appears only once.

Help Mr. Anant find the Captain's room number.

You are given the value of **K** and the list of room numbers.

## Input Format

- The first line contains an integer **K**, the size of each family group.
- The second line contains the unordered list of room numbers.

## Constraints

As specified in the problem.

## Output Format

Print the Captain's room number.

## Sample Input
```text
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
```

## Sample Output
```text
8
```

## Explanation

The list contains the room numbers of all tourists.

Since **K = 5**, each family consists of five members. Every family's room number appears five times in the list, except for the Captain's room number.

Room number **8** appears only once.

Therefore, the Captain's room number is **8**.
