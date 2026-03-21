def transpose(m):
    n=len(m)
    for i in range(n):
        for j in range(i+1,n):
            m[i][j],m[j][i]=m[j][i],m[i][j]
n = int(input())
mat=[list(map(int,input().split())) for i in range(n)]
transpose(mat)
print("Transpose matrix:")
for row in mat:
    print(*row)