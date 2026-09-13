number = input("Enter a number: ")
if not number.isdigit():
        print("Error:Invalid Input.")
else:
        number = int(number)
        for multipliers in range(1, 12):
                print(f"{number: }*{multipliers: } = {number*multipliers: }")