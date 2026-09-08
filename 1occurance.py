def one_occurance(n,target):
    for i in range(len(n)):
        if n[i] == target:
            return i
    return -1
n = list(map(int, input("Enter list of numbers: ").split()))
target = int(input("Enter number to find: "))
print(one_occurance(n, target))
