# Write different versions of either Exercise 7-4 or7-5 that do each of the following at least once:

# Use a conditional test in the while statement to stop the loop.
# Use an acive variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value.

import time

start = time.time()

prices = {
    range(3) : "Free",
    range(3,13) : "$10"
}

current = 1

while current < 10:
    age = input("What age are you?\n" \
    "Enter q to quit: ")

    if age == "q":
        break

    price = "$15"

    for ages, cost in prices.items():
        if age in ages:
            price = cost
            break

    print(f"Price: {price}")

    current = time.time() - start
