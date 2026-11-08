#  Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
#  As they enter each topping, print a message saying you’ll add that topping to their pizza.

top = []

def toppings(topping):
    topping.strip().lower()
    top.append(topping)

while True:
    topping = str(input("Enter a topping to add, or q to stop: "))
    if topping == 'q' or topping == "quit":
        break
    else:
        toppings(topping)


for topping in top:
    print(f"Adding {topping} to your pizza")
    
