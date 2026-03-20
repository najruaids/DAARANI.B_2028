def rot(mat):
    n=len(mat)
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    for row in mat:
        row.reverse()
n=int(input())
mat=[list(map(int,input().split())) for i in range(n)] 
rot(mat)
for i in mat:
    print(*i)
   