student_info = input("Student information: ") #students1.csv
exercise_data = input("Exercises completed: ") #exercises1.csv
exam_data = input("Exam points: ") #exam_points1.csv
course_info  = input("Course information: ") #course1.txt
course_credit = []
with open(course_info) as course_file:
    for line in course_file:
        parts = line.split(": ")
        course_credit.append(parts[1].strip())

student_name = {}
with open(student_info) as student_file:
    for line in student_file:
        parts = line.split(";")
        # ignore the header line
        if parts[0] == "id":
            continue
        student_name[parts[0]] = parts[1].strip()+ " " + parts[2].strip()

exercise_nbr = {}
with open(exercise_data) as exer_file:
    for line in exer_file:
        parts = line.split(";")
         # ignore the header line
        if parts[0] == "id":
            continue
        point_list = []
        for points in parts[1:]:
            point_list.append(int(points.strip()))
        exercise_nbr[parts[0]] = sum(point_list)
#print(exercise_nbr)

exercise_points = {}
for id, points in exercise_nbr.items():
    exercise_points[id] = int(points*100/40/10)
#print(exercises_points)

exam_points = {}
with open(exam_data) as exam_file:
    for line in exam_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exam_pt = []
        for points in parts[1:]:
            exam_pt.append(int(points.strip()))
        exam_points[parts[0]] = int(sum(exam_pt))
#print(exam_points)

total_points = {}
for exam_id, point_list in exam_points.items():
    if exam_id in exercise_points:
        point = exercise_points[exam_id] + exam_points[exam_id]
        total_points[exam_id] = point
#print(total_points)

final_grade = {}
for id, point in total_points.items():
    grade = 0
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
    final_grade[id] = grade

with open("results.txt", "w") as new_file:
    new_file.write(f"{course_credit[0]}, {course_credit[1]} credits\n")
    new_file.write("======================================\n")
    new_file.write(f"name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
    for id, name in student_name.items():
        if id in exercise_nbr:
            exec_nbr = exercise_nbr[id]
        if id in exercise_points:
            exec_pts = exercise_points[id]
        if id in exam_points:
            exm_pts = exam_points[id]
        if id in total_points:
            point = total_points[id]
        if id in final_grade:
            grade = final_grade[id]
        new_file.write(f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{point:<10}{grade:<10}\n")

with open("results.csv", "w") as my_file:
    line = ""
    for id, name in student_name.items():
        if id in final_grade:
            g = final_grade[id]
        line += f"{id};{name};{g}\n"
    my_file.write(line)