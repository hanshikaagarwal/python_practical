'''ques5-Suppose a dictionary contains roll numbers and names of students .Write a program to receive roll numbers,extract the names corresponding
to the roll number and displau message congratilation the student by his names.I f the roll number doesn't exit in the dictionary
the message should be 'congratulation students' '''

students={554:'Ajay',350:'Ramesh',395:'Rakesh'}
rollno=int(input('enter the roll number:'))
name=students.get(rollno,'student')
print(f'congratulation {name}')
rollno=int(input('enter roll number:'))
name=students.get(rollno,'student')
print(f'congatulations {name}')