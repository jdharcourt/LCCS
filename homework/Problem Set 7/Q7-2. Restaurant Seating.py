#Q7-2.
# Restaurant Seating: Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready.

try:
    people = int(input("How many people are in your group?: "))
except:
    print("Please only enter a number")

if people > 8:
    print("You will need to wait for a table")
else:
    print("Your table is ready")