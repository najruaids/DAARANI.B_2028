def dis_num(n):
    for i in range(len(n)):
        ind=abs(n[i])-1
        n[ind]=-abs(n[ind])
    r=[]
    for i in range(len(n)):
        if n[i]>0:
            r.append(i+1)
    return r
n=list(map(int,input().split()))
print(dis_num(n))