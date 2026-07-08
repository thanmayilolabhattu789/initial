li=[8,4,8,1,5,1,8,2,3,4,5,6,7,8]
ans = 0
for i in range(len(li)):
    if ((li[i] % 2 == 0) and (li[i] % 3 == 0)):
         ans = ans+1
print(ans)