def divisible(n):
    if n % 5 == 0:
        return f"{n} is divisible by 5"
    else:
        return f"{n} is not divisible by 5"
n = int(input("Enter a number: "))
answer = divisible(n)
print(answer)