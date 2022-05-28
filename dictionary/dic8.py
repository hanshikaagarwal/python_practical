'''ques8-Write a program to assign grades to students and display all the grades using keys() and gets() method of dictionary'''

grades={'tamana':'A','pranav':'B','summit':'C'}
for key in grades.keys():
    print(key,'',grades.get(key,0))