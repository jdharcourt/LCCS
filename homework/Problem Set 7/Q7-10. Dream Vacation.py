# Write a program that polls users about their dream vacation. Write a prompt similar to "If you could visit one place in the world, where would you go?" 
# Include a block of code that prints the results of the poll. 

## Each time the program asks for input the user inputs results of another person in the poll
## A while loop should be used so the program takes in as many places as the poll requires, until the user decides to quit. 
## You should use a data structure that can easily keep track of both which places were input as well as keeping track of the number of times each place was input; 
# mapping the place to the count


destinations = {}

while True:

    try:
        dest = str(input("If you could visit one place in the world, where would you go: "))
    except:
        print("Please only enter a name of you destination")

    if dest.lower().strip() == "quit":
        break

    destination = dest.lower().strip()

    if destination not in destinations.keys():

        destinations[destination] = 1

    else:
        destinations[destination] += 1

if len(destinations) > 0:
    most_common = next(iter(destinations))
    most_common_val = destinations[next(iter(destinations))]

    for value in destinations.values():
        if value > most_common_val:
            most_common_val = destinations[value]
            most_common = destinations

    print("------ Destinations -----\n")
    print(f"The most common destination was {most_common}, at a whopping {most_common_val} votes")
    
    for destination in destinations.keys():
        print(f"{destination}: {destinations[destination]} votes")
    print("------ Destinations -----\n")

        




