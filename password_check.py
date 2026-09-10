password = (input("Enter your password: "))
#Rule
at_least_8_characters = len("password") >= 8
contains_a_digit = any(char.isdigit() for char in password)
contains_an_uppercase_letter = any(char.isupper() for char in password)


if at_least_8_characters and contains_a_digit and contains_an_uppercase_letter:
    print("Valid password!")
else:
    print("Invalid password")
    if not at_least_8_characters:
        print("- Must contain at least 8 characters")
    if not contains_a_digit:
        print("- Must contain a digit (0-9)")
    if not contains_an_uppercase_letter:
        print("- Must cntain an  uppercase letter")





count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")