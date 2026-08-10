def greater_than_five(n):
   number = 0
   while n > 0:
      digit = n % 10
      if digit > 5:
         number += 1
      n = n // 10
   return number
n = int(input("Enter number: "))
answer = greater_than_five(n)
print(answer)