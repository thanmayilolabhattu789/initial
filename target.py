def element_exists(a, target):
    for i in range(len(a)):
        if a[i] == target:
            return True
    return False
a = list(map(int, input("Enter list of numbers: ").split()))
target = int(input("Enter number to check existence: "))
if element_exists(a, target):
    print("Element exists in the list.")
else:
    print("Element does not exist in the list.")