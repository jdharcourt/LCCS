# James Harcourt
# Q5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#
# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# If the person is age 65 or older, print a message that the person is an elder.

gen = ""

while True:
    try:
        age = int(input("Enter your age: "))
        break

    except ValueError:
        print("Please enter only a number")

if age < 2:
    gen = "baby"
elif age >= 2 and age < 4:
    gen = "toddler"
elif age >= 4 and age < 13:
    gen = "child"
elif age >=13 and age < 20:
    gen = "teenager"
elif age >= 20 and age < 65:
    gen = "adult"
else:
    gen = "elder"

print(f"You are a {gen}")
