def thanu(n):
    count = 0
    while n > 0:
        if n % 2 == 0:
            count += 1
        n = n // 10
    return count
n = int(input("Enter number: "))
answer = thanu(n)
print(answer)
