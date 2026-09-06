def second_smallest(n):
    smallest = n[0]
    second_smallest = float('inf')

    for i in range(1, len(n)):
        if n[i] < smallest:
            second_smallest = smallest
            smallest = n[i]

        elif n[i] < second_smallest and n[i] != smallest:
            second_smallest = n[i]

    return second_smallest
n = list(map(int, input("Enter list of numbers: ").split()))
answer = second_smallest(n)
print(answer)