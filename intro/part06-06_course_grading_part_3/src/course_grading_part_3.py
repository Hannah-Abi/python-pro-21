# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    
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

exec_nbrs = {}
for id, exec in exercises.items():
    exec_nbr = int(sum(exec))
    exec_nbrs[id] = exec_nbr
#print(exec_nbrs) #21,27,35

exercise_point = {}
for id, exercise_list in exercises.items():
    total = int(sum(exercise_list)*100/40/10)
    exercise_point[id] = total
#print(exercise_point) # 5, 6, 8

#Find exam point
exams = {}
with open(exam_data) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        name = parts[0]
        exams[name] = []
        for exam in parts[1:]:
            exams[name].append(int(exam))

#print(exercises)
exam_point = {}
for name, exam_list in exams.items():
    total_point = sum(exam_list)
    exam_point[name] = total_point
#print(exam_point) #9, 11, 14

tot_pts = {}
for exam_id, exam_list in exam_point.items():
    grade = 0
    if exam_id in exercise_point:
        point = exercise_point[exam_id] + exam_point[exam_id]
    tot_pts[exam_id] = point
#Sprint(tot_pts) #14, 17,25

total_list = {}
for exam_id, exam_list in exam_point.items():
    grade = 0
    if exam_id in exercise_point:
        point = exercise_point[exam_id] + exam_point[exam_id]
    if point in range (0,15):
        grade = 0
    elif point in range (15,18):
        grade = 1
    elif point in range (18,21):
        grade = 2
    elif point in range (21,24):
        grade = 3
    elif point in range (24,28):
        grade = 4
    elif point > 28:
        grade = 5 
    total_list[exam_id] = grade
#print(total_list) #0,1,3

print(f"name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for id, name in names.items():
    if id in exec_nbrs:
        exec_nbr = exec_nbrs[id]
    if id in exercise_point:
        exec_pts = exercise_point[id]
    if id in exam_point:
        exm_pts = exam_point[id]
    if id in tot_pts:
        point = tot_pts[id]
    if id in total_list:
        grade = total_list[id]
    print(f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{point:<10}{grade:<10}")
