a = "ADDA"
n = len(a)
ans = "" 
for i in range (n-1,-1,-1):
    ans = ans + str(a[i])
if ans == a:
    print("It is a palindrome")
else:
    print("It is not a palindrome")