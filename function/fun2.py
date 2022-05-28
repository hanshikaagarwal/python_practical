'''ques2-write a python function to create and return a list containing tuple of the form(x,x2,x3) for all x between 1 and 20 (both included)'''

def generate_list():
    lst=list()
    for i in range(1,11):
        lst.append((i,i**2,i**3))
    return lst
l=generate_list()
print(l)