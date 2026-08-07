def funn(n):
    total=0
    while n>0:
        digit=n%10
        total = total + digit
        n = n//10
    return (total)
n = int(input("enter number="))
answer = funn(n)
print(answer)
