# James Harcourt
# Q6-10. Favourite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favourite number (use a list as each of the dictionary's values).
#
# Then print each person’s name along with their favourite numbers (use a "nested for loop", the outer loop iterates the dictionary and the inner loop iterates the value's list)

names = {'matthew':[5,12],'mark':[23,43],'luke':[53, 56],'john':[1,28],'paul':[12,18]}

for key,value in names.items():
    for number in value:
        print(number)