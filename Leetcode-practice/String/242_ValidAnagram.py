def anagram(s,t):
    a=sorted(s)
    b=sorted(t)
    return a==b
s=input("Enter 1st string")
t=input("Enter 2nd string")
print(anagram(s,t))