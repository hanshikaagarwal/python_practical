'''ques 10-Create two lists and marks.create a dictionary from these two lists using dictionary comprehension.use names as keys and marks as value'''

lstnames=['sunil','sachin','rahul','kapil','rohit']
lstmarks=[54,65,45,67,78]
d={k:v for (k,v) in zip(lstnames,lstmarks)}
print(d)