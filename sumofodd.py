def sum_odd_digits(n):
    total = 0
    while n > 0:
        digit = n % 10 
        if digit % 2 == 1:
            total += digit
        n = n // 10
    return total  
n = int(input("Enter number: "))
answer = sum_odd_digits(n)
print(answer)  