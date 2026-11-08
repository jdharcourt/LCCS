# James Harcourt
# Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

things = ['Car', "Plane", "Truck", "Computer", "Phone", "Laptop"]

def print_things():
    for thing in things:
        print(thing)
    print()


print_things()
things.sort()
print_things()
things.sort()
print_things()
things.sort(reverse = True)
print_things()
things.append("Van")
print_things()
things.pop()
print_things()
things.remove("Plane")
print_things()