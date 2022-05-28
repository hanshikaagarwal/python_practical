'''ques10-Write a program using the global statement'''

a=20
def display():
    global a
    a=30
    print('the value of a in function:',a)
display()
print('the value of an outside function:',a)