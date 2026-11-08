# James Harcourt
# Q6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

people = [
    {'first_name':"Matthew","last_name":'Dover', 'age':17, 'city':'Dublin'},
    {'first_name':"Mark","last_name":'Byrne', 'age':22, 'city':'Dublin'},
    {'first_name':"Paul","last_name":'Delany', 'age':43, 'city':'Dublin'},
    {'first_name':"John","last_name":'Paul', 'age':13, 'city':'Dublin'}
    ]

for person in people:
    
    first = person['first_name']
    last = person['last_name']
    age = person['age']
    city = person['city']
    
    print(f"First Name: {first}, Last Name: {last}, Age: {age}, City: {city}")