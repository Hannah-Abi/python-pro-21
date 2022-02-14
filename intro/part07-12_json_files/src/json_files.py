# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as json_file:
        data = json_file.read()
        student_info = json.loads(data)
    for student in student_info:
        print(f"{student['name']} {student['age']} years ({', '.join(student['hobbies'])})")

if __name__=="__main__":
    print_persons("file1.json")