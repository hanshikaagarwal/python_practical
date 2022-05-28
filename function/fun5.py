'''ques 5-Write a program to find the maximum of two numbers'''

def calc_factorial(num):
    fact=1
    print('entered number is:',num)
    for i in range(1,num+1):
        fact=fact*i
    print('factorial of number',num,' is =' ,fact)
number=int(input('enter the number:'))
calc_factorial(number)