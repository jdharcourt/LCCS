# James Harcourt
# Q6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#
# Use a loop to print the name of each river included in the dictionary.  # .keys()
# Use a loop to print the name of each country included in the dictionary. # .values()
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.   # .items()

rivers = {'nile':'egypt','shannon':'ireland',"amazon":'brazil'}

for river in rivers.keys():
    print(river.title())
print()

for country in rivers.values():
    print(country.title())

print()

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")