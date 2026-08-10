def reverse(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse  
n = int(input("Enter number: "))
answer = reverse(n) 
print("Reverse of the number is:", answer)