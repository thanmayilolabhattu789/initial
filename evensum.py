def sum_even_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            total += digit
        n = n // 10
    return total
n = int(input("Enter number: "))
answer = sum_even_digits(n)
print(answer)