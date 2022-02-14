class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list):
    passed_student = filter(lambda t: t.grade >= 1, attempts)
    return list(passed_student)

def attempts_with_grade(attempts: list, grade: int):
    accepted_students = filter(lambda t: t.grade == grade, attempts)
    return list(accepted_students)

def passed_students(attempts: list, course: str):
    passed_stu = list(filter(lambda c : True if (c.grade > 0 and c.course_name == course) else False, attempts))
    def sort_students(student: CourseAttempt):
        return student.student_name
    pass_student_list = sorted(passed_stu, key=sort_students)
    return list(map(lambda t : t.student_name, pass_student_list))

if __name__=="__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
    s4 = CourseAttempt("Niles Nerd", "Networking", 3)
    for attemp in passed_students([s1, s2, s3, s4], "Introduction to Programming"):
        print(attemp)