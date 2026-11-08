# James Harcourt
# Think of at least five places in the world you’d like to visit.
poi = ['USA', 'Mexico', 'Egypt', "Iceland", "Finland"]


def print_items():
    print("\nItems: ")
    for item in poi:
        print(item)

def sort():
    print('\nSorted: ')
    for item in sorted(poi):
        print(item)

print_items()
sort()

print_items()
poi.reverse()
print_items()
poi.reverse()
print_items()

poi.sort()
print_items()
poi.sort(reverse = True)
print_items()

print(poi)