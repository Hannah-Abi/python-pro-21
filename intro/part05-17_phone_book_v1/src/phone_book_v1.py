# Write your solution here
my_dic = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 2:
        name = input("name: ")
        number = input("number: ")
        print("ok!")
        if name not in my_dic:
            my_dic[name] = ""
        my_dic[name] = number
    if command == 1:
        search_name = input("name: ")
        if search_name in my_dic:
            print(my_dic[search_name])
        else:
            print("no number")
    if command == 3:
        print("quitting...")
        break



