# A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is €10; and if they are over age 12, the ticket is €15.
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

prices = {
    range(3) : "Free",
    range(3,13) : "$10"
}

while True:
    age = int(input("What age are you?: "))

    price = "$15"

    for ages, cost in prices.items():
        if age in ages:
            price = cost
            break

    print(f"Price: {price}")