from abc import abstractmethod
from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    credit_sum = reduce(lambda total, course: course.credits + total, attempts, 0)
    return credit_sum

def sum_of_passed_credits(attempts: list):
    passed_credits = filter(lambda course: course.grade > 0, attempts)
    passed_credits_sum = reduce(lambda total, course: course.credits + total, passed_credits, 0)
    return passed_credits_sum

def average(attempts: list):
    passed_credits = list(filter(lambda course: course.grade >= 1, attempts))
    passed_credits_avg = reduce(lambda total, course: (course.grade + total), passed_credits, 0)
    return passed_credits_avg/len(passed_credits)

if __name__=="__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

    ag = average([s1, s2, s3])
    print(ag)