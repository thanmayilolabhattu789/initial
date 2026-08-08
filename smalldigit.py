def smallest_digit(n):
    smallest = 9
    while n > 0:
        digit = n % 10
        if digit < smallest:
            smallest = digit
        n = n // 10
    return smallest

n = int(input("Enter number: "))
answer = smallest_digit(n)
print(answer)       
 