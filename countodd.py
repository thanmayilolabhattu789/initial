def odd_digits(n):
    count = 0
    while n > 0:
        digit = n % 10 
        if digit % 2 != 0:
            count += 1
        n = n // 10
    return count
n = int (input ("Enter number : "))
answer = odd_digits(n)
print(answer)