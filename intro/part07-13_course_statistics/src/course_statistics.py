# Write your solution here
import urllib.request
import json
def retrieve_all():
    url_link = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    my_request = urllib.request.urlopen(url_link)
    data = my_request.read()
    courses = json.loads(data)
    #print(courses)
    active_courses = []
    for course in courses:
        if course['enabled'] == True:
            active_courses.append((course['fullName'],course['name'], course['year'],sum(course['exercises'])))
    return active_courses

def retrieve_course(course_name: str):
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats"
    adr_course = address.replace("****", course_name)
    my_request = urllib.request.urlopen(adr_course)
    data = my_request.read()
    courses = json.loads(data)
    #print(courses)
    students = []
    hours = []
    exercises = []
    for k in courses:
        students.append(courses[k]['students'])
        hours.append(courses[k]['hour_total'])
        exercises.append(courses[k]['exercise_total'])
    # add course info to a dictionary
    dict = {}
    dict['weeks'] = len(courses)
    dict['students'] = max(students)
    dict['hours'] = sum(hours)
    dict['hours_average'] = int(sum(hours)/max(students))
    dict['exercises'] = sum(exercises)
    dict['exercises_average'] = int(sum(exercises)/max(students))
    return dict

if __name__=="__main__":
    #print(retrieve_all())
    print(retrieve_course("docker2019"))
