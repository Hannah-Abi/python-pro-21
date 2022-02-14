# Write your solution here
def oldest_person(people: list):
    year = people[0][1]
    oldest_person = people[0][0]
    for i in range(len(people)):
        if people[i][1] < year:
            year = people[i][1]
            oldest_person = people[i][0]
        i += 1
    return oldest_person
if __name__ == "__main__":
    people_list = [('Emily', 2014), ('Arthur', 1977), ('Ernest', 1985), ('Mary', 1953), ('Ellen', 1997)]
    result = oldest_person(people_list)
    print(oldest_person(people_list))

