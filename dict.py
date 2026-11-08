from pathlib import Path



students = {}


names = Path("names.txt").read_text(encoding="utf-8").splitlines()
subjects = Path("subjects.txt").read_text(encoding="utf-8").splitlines()
ages = [int(age) for age in Path("ages.txt").read_text().splitlines()]

for i, (name, subject, age) in enumerate(zip(names, subjects, ages)):
    students[i] = {'name':name,"subject":subject,"age":age}



for number, info in students.items():
    print(f"Student #{number+1}: {info.get('name')}'s favourite subject is {info.get('subject')}.")


