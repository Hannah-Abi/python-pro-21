# Write your solution here
def add_student(students: dict, name: str):
    if name not in students:
        students[name] = {}
    students[name] = {}
    return students

def print_student(students: dict, name: str):
    sum = 0
    check = {}
    if name in students:
        print(f"{name}:")
        if students[name] == check  :
            print(" no completed courses")
        else:
            sum = 0
            print(f" {len(students[name])} completed courses:")
            for k,v in students[name].items():
                print(f"  {k} {v} ")
                sum  += v
            avg = sum/len(students[name])
            print(f" average grade {avg:.1f}")
            
    else:
        print(f"{name}: no such person in the database")  

def add_course(students: dict, name:str, course: tuple):
    k,v = course[0], course[1] # k,v = "Introduction to Programming", 3
    d = students[name]
    if  v != 0:
        if k in d.keys():
            d[k] = max(v,d[k])
        else:
            d[k] = v
    #print(students[name])
    return students

def summary(students):
    print(f"students {len(students)}")
    final_sum = []
    for name, course in students.items():
        sum = 0
        for k,v in students[name].items():
            sum  += v
        avg = sum/len(students[name])
        com = (name, len(course), avg) 
        final_sum.append(com)
    max_cNo = final_sum[0][1]
    cos_person = final_sum[0][0]
    max_avg = final_sum[0][2]
    avg_person = final_sum[0][0]
    for student in final_sum:
        if student[1] > max_cNo:
            max_cNo = student[1]
            cos_person = student[0]
        if student[2] > max_avg:
            max_avg = student[2]
            avg_person = student[0]
    print(f"most courses completed {max_cNo} {cos_person}")
    print(f"best average grade {max_avg} {avg_person}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)

