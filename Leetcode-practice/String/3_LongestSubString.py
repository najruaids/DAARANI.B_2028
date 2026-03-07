s=input()
max_len=0
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        if s[j] in temp:
            break
        temp+=s[j]
    max_len=max(max_len,len(temp))
print(max_len)