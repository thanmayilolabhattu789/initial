def last_occurance(n,target):
    last_index = -1
    for i in range(len(n)):
        count = 0
        if n[i] == target:
            last_index = i
    return last_index
n = list(map(int, input("Enter list of numbers: ").split()))
target = int(input("Enter number to find: "))
answer = last_occurance(n, target)
print(answer)
