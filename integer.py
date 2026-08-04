def integer(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
n = int(input("Enter number: "))
result = integer(n)
print(result)