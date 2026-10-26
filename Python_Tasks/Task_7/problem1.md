# Set .symmetric_difference() Operation

## Problem Statement

Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set contains the roll numbers of students who have subscribed to the English newspaper, and the other contains the roll numbers of students who have subscribed to the French newspaper.

Your task is to find the total number of students who have subscribed to either the English or the French newspaper, but not both.

### Input Format

- The first line contains the number of students who have subscribed to the English newspaper.
- The second line contains the space-separated list of student roll numbers who have subscribed to the English newspaper.
- The third line contains the number of students who have subscribed to the French newspaper.
- The fourth line contains the space-separated list of student roll numbers who have subscribed to the French newspaper.

### Constraints

As specified in the problem.

### Output Format

Output the total number of students who have subscriptions to the English or the French newspaper, but not both.

### Sample Input
```text
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

### Sample Output
```text
8
```

### Explanation

The students who subscribed to only the English newspaper or only the French newspaper are counted.

Students who subscribed to both newspapers are excluded.

The total number of students who subscribed to either newspaper, but not both, is **8**.
