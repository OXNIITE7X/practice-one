num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (*, /, +, - ): ")

if operator == "+":
    print("Result: ", num1 + num2)
elif operator == "-":
    print("Result: ", num1 - num2)
elif operator == "*":
    print("Result: ", num1 * num2)
elif operator == "/":
    print("Result: ", num1 / num2)
    if num2 == 0:
        print("Error: Cannot be divide by zero.")
else:
    print("Error: Invalid operator")