'''ques6-Write a program to calculate the area of circle using the formula'''

def area_circle(pi=3.14,radius=1):
    area=pi*radius*radius
    print('radius=',radius)
    print('the area of circle =',area)
area_circle()
area_circle(radius=5)