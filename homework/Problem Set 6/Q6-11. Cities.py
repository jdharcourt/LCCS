# James Harcourt
# Q6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'Dublin': {
        'country': 'Ireland',
        'population': 600000,
        'fact': 'The River Liffey flows through Dublin.'
    },
    'Paris': {
        'country': 'France',
        'population': 2100000,
        'fact': 'Paris is home to the Eiffel Tower.'
    },
    'Rome': {
        'country': 'Italy',
        'population': 2700000,
        'fact': 'Rome is home to the Colosseum.'
    }
}

for city, information in cities.items():
    print(city)
    for key, value in information.items():
        print(f"{key.title()}: {value}")
    print()

