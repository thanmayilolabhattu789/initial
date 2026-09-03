def count_element(a, target):
    n = len(a)
    count = 0
    for i in range(n):
        if a[i] == target:
            count += 1
        i += 1
    return count
target = int(input("Enter number to count: "))
a = [1,2,3,4,5,1,2,1]
answer = count_element(a, target)
print(answer)