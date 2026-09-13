num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operator = input("Enter an operator (*, /, +, - ): ")

if  not num1.isdigit() and not num2.isdigit():
    print("Error: Invalid Input.")
else:
    num1 = int(num1)
    num2 = int(num2)

    if operator == "+":
        print("Result: ", num1 + num2)

    elif operator == "-":
        print("Result: ", num1 - num2)

    elif operator == "*":
        print("Result: ", num1 * num2)

    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot be divide by zero.")
        else:
            print(num1 / num2)
    else:
        print("Error: Invalid operator")