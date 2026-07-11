s= "abcdeffedcbh"
n=len(s)//2
m=len(s)
valid = True
for i in range(n):
    l = s[i]
    r = s[m-1-i]
    print(l,r)
    if l != r:
        valid = False
        break
if valid :
    print("yes")
else:
    print("no")