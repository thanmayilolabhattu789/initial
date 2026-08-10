def digit_by_3(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit % 3 == 0:
            count += 1
        n = n // 10
    return count
n = int(input("Enter number: "))    
answer = digit_by_3(n)
print(answer)