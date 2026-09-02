def linear_search(a,target):
    n = len(a)
    i = 0
    while(i<n):
        if a[i]==target:
            return True
        i = i + 1
    return False
a = [1,2,3,4,5]
target = int(input("Enter number to search: "))
answer = linear_search(a,target)
if answer:
    print("Found")
else:
    print("Not Found")

