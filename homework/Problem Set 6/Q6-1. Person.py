# James Harcourt
# Q6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary. Use "square bracket notation" to retrieve the values.

matthew = {'first_name':"Matthew","last_name":'Dunphy', 'age':17, 'city':'Dublin'}

print(f'First Name: {matthew.get('first_name')}')
print(f'Lastname: {matthew.get('last_name')}')
print(f'Age: {matthew.get('age')}')
print(f'City: {matthew.get('city')}')