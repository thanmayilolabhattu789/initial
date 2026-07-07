li=[0,8,4,8,1,5,1,8,2,3,4,5,6,7,8]
n=len(li)
ans = 0
for i in range(n):
    if li[i] == 8:
        ans = ans+1
print(ans)