def smallest(a):
    n = len(a)
    smallest=a[0]
    i = 1
    while(i<n):
        if a[i]<smallest:
            smallest = a[i]
        i = i + 1
    return smallest
a = [1,2,3,4,5]
answer = smallest(a)
print(answer)
