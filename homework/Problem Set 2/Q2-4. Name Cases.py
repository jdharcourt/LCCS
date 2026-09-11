# James Harcourt
# Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name = input("Whats your name? ")
iteration = 0

# Yes its over complicated, why not
for i in range(3): # Iterate through name, printing it in Uppercase, Lowercase and Title case
    iteration += 1
    if iteration == 1:
        print(name.lower()) 
    elif iteration == 2:
        print(name.upper())
    else:
        print(name.title())
