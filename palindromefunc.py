def palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if original == reverse:
        return True
    else:
        return False
n = int(input("Enter number: "))
answer = palindrome(n)
if answer:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")    