name = input("Enter your name: ")
birth_year = int(input("What year were you born? "))
age = 2026 - birth_year

if birth_year > 2026:
    print("Error: birth year cannot be in the future")
else:
    age = 2026 - birth_year
    print("Hello", name, "you are", age , "years old.")