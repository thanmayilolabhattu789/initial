num1=float(input("first number:"))
operator=input("select operator(+ - * /)=")
num2=float(input("second number:"))
if(operator == "+"):
    print("result=",num1+num2)
elif(operator == "-"):
    print("result=",num1-num2)
elif(operator == "*"):
    print("result=",num1*num2)
elif(operator == "/"):
    if(num2 != 0):
        print("result=",num1/num2)
    else:
        print("division is not possible")
else:
    print("invalid operator!")
   