def get_grade(result):
    grade = "Unsuccessful"
    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    elif result >= 50:
        grade = "Lower Merit"
    elif result >= 40:
        grade = "Pass"
    return grade

results = [39, 32, 62, 88, 51, 62, 64, 81, 77]
total = 0
for result in results:
    total += result

arithmetic_mean = total / len(results)
print("The mean percentage mark is", round(arithmetic_mean))

for result in results:
    
    grade = get_grade(result)
    print(f"Grade: {grade}")
