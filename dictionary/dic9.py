'''ques9-Write a program to count the frequency of character using the get() method '''

def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]=d.get(c,0)+1
    return d
h=histogram('applle')
print(h)