def smallest_average(person1: dict, person2: dict, person3: dict):
    person_list = [person1,person2,person3]
    smallest_avg_person = {}
    min_avg = sum([person1['result1'],person1['result2'],person1['result3']])/3
    print(min_avg)
    for person in person_list:
        avg = sum([person['result1'],person['result2'],person['result3']])/3
        print(avg)
        if avg <= min_avg:
            min_avg = avg
            smallest_avg_person['name'] = person['name']
            smallest_avg_person['result1'] = person['result1']
            smallest_avg_person['result2'] = person['result2']
            smallest_avg_person['result3'] = person['result3']
    return smallest_avg_person

if __name__=="__main__":
    person1 = {"name": "Mary", "result1": 9, "result2": 9, "result3": 9}
    person2 = {"name": "Gary", "result1": 7, "result2": 7, "result3": 7}
    person3 = {"name": "Larry", "result1": 8, "result2": 8, "result3": 8}
    print(smallest_average(person1, person2, person3))