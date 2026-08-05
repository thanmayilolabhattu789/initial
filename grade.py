def grade(n):
    if n >= 90:
        return "A"
    elif n >= 70:
        return "B"
    elif n >= 50:
        return "C"
    elif n >= 35:
        return "D"
    else:
        return "Fail"
n = int(input("Enter your score: "))
answer = grade(n)
print(answer)
