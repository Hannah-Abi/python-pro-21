# Write your solution here
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
print("Number of groups formed: ", end="")
if students%group_size == 0:
    print(students/group_size)
if students%group_size != 0:
    print(students//group_size+1)