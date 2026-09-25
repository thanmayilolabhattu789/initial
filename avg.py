def average(n):
    total = 0
    for i in range(len(n)):
        total += n[i]
    average = total / len(n)
    return average
n = list(map(int, input("Enter list of numbers: ").split()))
answer = average(n)
print(answer)