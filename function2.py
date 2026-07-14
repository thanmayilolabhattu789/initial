def thanu(min,max):
    total = 0
    for i in range(min,max+1):
        total += i
        if i< max:
            print(i,end=" + ")
        else:
            print(i,end=" = ")
    print("",total)
thanu(1,8)

