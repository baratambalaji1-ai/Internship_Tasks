
HackerRank Home
|
Prepare
Certify
Compete
Search

1
|
Switch to..

baratambalaji1
PrepareAlgorithmsStringsGame of Thrones - I
Game of Thrones - I
215 more points to get your next star!
Rank: 927899|Points: 260/475
Problem Solving
Problem
Submissions
Leaderboard
Discussions
Editorial
Topics
Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.

door

But, to lock the door he needs a key that is an anagram of a palindrome. He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome. Given a string, determine if it can be rearranged into a palindrome. Return the string YES or NO.

Example

One way this can be arranged into a palindrome is . Return YES.

Function Description
Complete the gameOfThrones function below.

gameOfThrones has the following parameter(s):

string s: a string to analyze
Returns

string: either YES or NO
Input Format

A single line which contains .

Constraints

 |s| 
 contains only lowercase letters in the range 
Sample Input 0

aaabbbb
Sample Output 0

YES
Explanation 0

A palindromic permutation of the given string is bbaaabb.

Sample Input 1

cdefghmnopqrstuvw
Sample Output 1

NO
Explanation 1

Palindromes longer than 1 character are made up of pairs of characters. There are none here.

Sample Input 2

cdcdcdcdeeeef
Sample Output 2

YES
Explanation 2

An example palindrome from the string: ddcceefeeccdd.

Language
Python 3
More
12345678910111213141516171819

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

Line: 29 Col: 1

Test against custom input
Authoramititkgp
DifficultyEasy
Max Score30
Submitted By123545
Need Help?
View discussions
View editorial
View top submissions
RESOURCES
Palindrome
Dictionary
Anagram
rate this challenge

MORE DETAILS
Download problem statement
Download sample test cases
Suggest Edits
Share on XShare on LinkedIn
BlogScoringEnvironmentFAQAbout UsHelpdeskCareersTerms Of ServicePrivacy Policy



