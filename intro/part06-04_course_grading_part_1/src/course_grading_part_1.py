# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
names = {}
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        # ignore the header line
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1].strip()+ " " + parts[2].strip()

exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        name = parts[0]
        exercises[name] = []
        for exercise in parts[1:]:
            exercises[name].append(int(exercise))
#print(exercises)
exercise_point = {}
for name, exercise_list in exercises.items():
    total = sum(exercise_list)
    exercise_point[name] = total
print(exercise_point)

for id, name in names.items():
    if id in exercise_point:
        number_exer = exercise_point[id]
        print(f"{name} {number_exer}")
    else:
        print(f"{name}")

#for pic, name in names.items():
