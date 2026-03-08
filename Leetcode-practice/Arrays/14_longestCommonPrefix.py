def longestCommonPrefix (str):
    if not str:
        return ""
    p=str[0]
    for i in str[1:]:
        while not i.startswith(p):
            p=p[:-1]
            if p=="":
                return ""
    return p
s=input().split()
print(longestCommonPrefix(s))