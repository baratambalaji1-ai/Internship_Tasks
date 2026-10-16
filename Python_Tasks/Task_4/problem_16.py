# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    first_lowest = float('inf')
    secound_lowest = float('inf')
    
    for student in students:
        score = student[1]
        if score < first_lowest:
            second_lowest = first_lowest
            first_lowest = score
        elif score < second_lowest and score != first_lowest:
            second_lowest = score
            
    names = []
    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])
    names.sort()
    
    for name in names:
        print(name)

