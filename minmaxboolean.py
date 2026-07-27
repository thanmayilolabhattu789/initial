def thanu():
    valid = True
    n = int(input("Enter  2 or 3 digit number: "))
    s =[int(d) for d in str(n)]
    minimum=min(s)
    maximum=max(s)
    product = minimum * maximum
    print(product)
    if product > 20:
        valid = False
    print(valid)
    
thanu()