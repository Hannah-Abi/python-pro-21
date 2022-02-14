# Write your solution here
my_dic = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 2:
        name = input("name: ")
        number = input("number: ")
        print("ok!")
        if name not in my_dic:
            my_dic[name] = []
        my_dic[name].append(number)
    if command == 1:
        search_name = input("name: ")
        
        if search_name in my_dic:
            for key, value in my_dic.items():
                if key == search_name:
                    for no in value:
                        print(no)
        else:
            print("no number")
    if command == 3:
        print("quitting...")
        break

