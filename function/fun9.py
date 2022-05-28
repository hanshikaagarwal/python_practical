'''ques9- Write a program without using the global statement'''

a=20
def display():
    a=30
    print('the value of a in function:',a)
display()
print('the value of an outside functon:',a)