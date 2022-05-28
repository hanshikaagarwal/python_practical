'''ques8- write a program to return a multiple value from a function'''

def compute(num1):
    print('number =',num1)
    return num1*num1, num1*num1*num1
square,cube=compute(4)
print('swquare =',square,'cube=',cube)