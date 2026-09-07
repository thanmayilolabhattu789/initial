def second_largest(n):
    largest = n[0]
    second_largest = float('-inf')
    for i in range(len(n)):
        if n[i] > largest:
            second_largest = largest
            largest = n[i]
        elif n[i] > second_largest and n[i] != largest:
            second_largest = n[i]
    return second_largest
n = list(map(int, input("Enter list of numbers: ").split()))
answer = second_largest(n)
print(answer)
