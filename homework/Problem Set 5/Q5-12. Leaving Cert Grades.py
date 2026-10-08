# James Harcourt
# Q5-12. Leaving Cert Grades: This program will take in a percentage mark and return a grade and corresponding Leaving Cert points.
#
# Write a program in which the user is asked did they take an exam at Higher or Ordinary level; then ask them to enter their percentage mark.  The program will let them know what their grade is, e.g., H2, O3 etc. as well as the Leaving Cert points they get for that subject.  This will require the use of: input function, changing data types, string comparison, string methods, if statements.
#
# Make sure your instructions and output to the user are clear and well formatted.
#
# Remember:
#
# Break down the problem
# Complete the program in stages, testing every step of the way
# Use comments and blank lines to separate the different parts of your program. At a minimum, have three sections: 
# Input (giving the user instructions and gathering values)
# Processing (don't print anything at this stage, store any needed values)
# Output (once all processing is complete, print the results to the user)
#
# Points at Higher Level	Grade
#
# Higher Level
#
# 	Percentage
#
# %
#
# 	Grade Ordinary Level	Points at Ordinary Level
# 100	H1	90 – 100	O1	56
# 88	H2	80 -89	    O2	46
# 77	H3	70 -79	    O3	37
# 66	H4	60 -69	    O4	28
# 56	H5	50 -59	    O5	20
# 46	H6	40 -49	    O6	12
# 37	H7	30 -39	    O7	0
# 0	H8	0 -29	O8	    0


level = input("Level - H/O: ").lower()
points = 0

while level.lower().strip() not in ("h", "o"):
    level = input("Please enter only L or H: ").strip().lower()

while True:
    try:
        grade = int(input("Grade: "))
        break
    except:
        print('Please enter just the number')

points_table = {
    "h": {
        range(90, 101): 100,
        range(80, 90): 88,
        range(70, 80): 77,
        range(60, 70): 66,
        range(50, 60): 56,
        range(40, 50): 46,
        range(30, 40): 37,
        range(0, 30): 0
    },
    "o": {
        range(90, 101): 56,
        range(80, 90): 46,
        range(70, 80): 37,
        range(60, 70): 28,
        range(50, 60): 20,
        range(40, 50): 12,
        range(30, 40): 0,
        range(0, 30): 0
    }
}

for grade_range, value in points_table[level].items():
    if grade in grade_range:
        points = value
        break

print(f"{grade}% = {points}")




