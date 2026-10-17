
HackerRank Home
|
Prepare
Certify
Compete
Search

|
Switch to..

baratambalaji1
PreparePythonSetsNo Idea!
No Idea!
15 more points to get your gold badge!
Rank: 409646|Points: 385/400
Python
Problem
Submissions
Leaderboard
Discussions
Editorial
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.

Hence, the total happiness is .

Language
Python 3
More
12345678910111213141516171819

for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)

Line: 19 Col: 1

Test against custom input
Authorsandyeep
DifficultyMedium
Max Score50
Submitted By291686
Need Help?
View discussions
View editorial
View top submissions
rate this challenge

MORE DETAILS
Download problem statement
Download sample test cases
Suggest Edits
Share on XShare on LinkedIn
BlogScoringEnvironmentFAQAbout UsHelpdeskCareersTerms Of ServicePrivacy Policy




