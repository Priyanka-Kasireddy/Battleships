def separate(s):
    l=len(s)
    temp= s[0:l:4],s[1:l:2]
    return temp[0]+temp[1]

print(separate("a-c-e-g-i-"))

