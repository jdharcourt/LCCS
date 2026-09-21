# James Harcourt
# Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

# James Harcourt
# Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

names = ["James", "Conor", "Hugo", "Daithi"]

for name in names:
    message = f"How are you, {name}?"
    print(message)
