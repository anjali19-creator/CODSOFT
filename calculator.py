a=int(input("enter first number "))
b=int(input("enter second number "))
operation=input("enter one operator +,-,*,/ ")
if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation=="/":
    if b==0:
        print("not defined")
    else:
        print(a/b)
else:
    print("invalid operation")