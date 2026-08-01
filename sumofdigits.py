
n = int(input("Enter number: "))
digit_sum = 0

while n>0:
    digit = n%10
    digit_sum = digit_sum + digit
    n = n//10
print("Sum of digits is:", digit_sum)
