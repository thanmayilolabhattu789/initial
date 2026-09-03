def sum_of_multiples(d):
    count = 0
    i = 1
    while (i<=50):
        if i%10==d:
            count = count + i
        i+=1
    return count
d = int(input("Enter digit: "))
answer = sum_of_multiples(d)
print(answer)