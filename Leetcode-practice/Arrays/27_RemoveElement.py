arr=list(map(int,input().split()))
val=int(input())
k=[]
for i in arr:
    if i!=val:
        k.append(i)
print(k)