'''ques3-A pallindrone is a word or phrase which reads the same in both directions.given below are some palindromic strings:
deed
level
malayalam
rats live on no evil star
murder for a jar of red rum
Write a program that defines a function ispalindrome() which checks weather a given string is pallindrone or not.Ignore spaces while checking 
for pallindrone'''

def ispalindrome(s):
    t=s.lower()
    left=0
    right=len(t)-1
    while right>=left:
        if t[left]=='':
            left+=1
        if t[right]=='':
            right-=1
        if t[left]!=t[right]:
            return False
        left+=1
        right-=1
    return True
print(ispalindrome('malayalam'))
print(ispalindrome('Rats live on no evil star'))
print(ispalindrome('Murder for a jar of red rum'))