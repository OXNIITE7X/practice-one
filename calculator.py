num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter an operator (*, /, +, - ): ")

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
        print(num1 /  num2)
else:
    print("Error: Invalid operator")