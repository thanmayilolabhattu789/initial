def divisible(n):
    if n % 2 == 0:
        return f"{n} is divisible by 2"
    else:
        return f"{n} is not divisible by 2"
n = int(input("Enter a number: "))
answer = divisible(n)
print(answer)