def eo(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Enter number: "))
answer = eo(n)
print(answer)