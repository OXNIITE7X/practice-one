name = input("Enter your name: ")
dob = input("What year were you born? ")

if not name.isdigit() and dob.isdigit():
    birth_year = int(dob)
    age = 2026 - (birth_year)
    if birth_year > 2026:
        print("Error: birth year cannot be in the future")
    else:
        age = 2026 - birth_year
        print("Hello", name, "you are", age , "years old.")
else:
    print("Invalid input")