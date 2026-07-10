s= "abcdef"
n=3
m=n*2
valid = True
for i in range(n):
    l = s[i]
    r = s[m-1-i]
    print(l,r)
    if s[i] != s[m-1-i]:
        valid = False
if valid :
    print("yes")
else:
    print("no")