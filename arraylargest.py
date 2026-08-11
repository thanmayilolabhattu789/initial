def largest(a):
    n = len(a)
    largest=a[0]
    i = 1
    while(i<n):
        if a[i]>largest:
            largest = a[i]
        i = i + 1
    return largest
a = [1,2,3,4,5]
answer = largest(a)
print(answer)
