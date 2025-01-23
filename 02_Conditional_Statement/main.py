# Conditional Statement

mario_age: int = 20
john_age: int = 25

# Adding user input
mario_age = int(input("Enter Mario's age: "))
john_age = int(input("Enter John's age: "))


# if, elif and else statement
if mario_age > john_age:
    print("Mario is older than John")
elif mario_age == john_age:
    print("Mario and John are of the same age")
else:
    print("John is older than Mario")