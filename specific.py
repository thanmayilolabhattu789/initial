def specific(n):
    specific_digits = 0
    while n > 0:
        digit = n % 10
        if digit == d:
            specific_digits += 1
        n = n // 10
    return specific_digits
n = int(input("Enter number: "))
d = int(input("Enter specific digit to count: "))
answer = specific(n)
print(answer)