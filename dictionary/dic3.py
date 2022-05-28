#ques3-write a program to pass alist into function .calv=culate the total number of positive and negative numbers from the list 
#and then display the count in terms of dictionary.
def abc(L):
    D={}
    D['Pos']=0
    D['neg']=0
    for x in L:
            if x>0:
                D['Pos']+=1
            else:
                D['neg']+=1
    print(D)
L={1,-2,-3,4}
abc(L)
