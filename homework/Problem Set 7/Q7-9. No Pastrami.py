# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['Ham', 'Ham and cheese', 'Tuna','Cheese', 'Chicken Mayo', 'Pastrami', 'Cheese and Pastrami', 'Pure pastrami']

finished_sandwiches = []


print("The deli has run out of pastrami.")




while sandwich_orders:
    sandwich = sandwich_orders.pop(0)

    if 'pastrami' in sandwich.lower():
        continue

    print(f"Your {sandwich} is ready")
    finished_sandwiches.append(sandwich)


print("\nReady: ")
for sandwich in finished_sandwiches:
    print(sandwich)