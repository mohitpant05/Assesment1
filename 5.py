a = int(input("Enter first number : "))
b= int(input("Enter second number : "))

choice = int(input("""Enter the operation you want to perform as given below (Enter number corresponding to symbol)\n
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter you choice from above options: """))


if choice == 1:
    print("Addition of two numbers is : ",a+b)
elif choice == 2:
    print("Subtraction of two numbers is : ",a-b)
elif choice == 3:
    print("Multiplication of two numbers is : ",a*b)
elif choice == 4:
    try:
        print("Division of two numbers is : ",a/b)
    except Exception as e:
        print("cant divide by zero")
else:
    print("Invalid choice")

