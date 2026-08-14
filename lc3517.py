s = "babab"
n=len(s)
m=n//2
ans=" "
for i in range(n-1,0,-1):
    if(ord(s[i])>ord(s[i+1])):
        ans = ans + str(s[i])
print(ans)