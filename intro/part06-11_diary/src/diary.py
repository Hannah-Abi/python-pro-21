# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    f = int(input("Function: "))
    if f == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as my_file:
            my_file.write(f"{entry}\n")
            print("Diary saved")
    if f == 2:
        print("Entries:")
        with open("diary.txt") as new_file:
            content = new_file.read()
            diary_list = content.split("\n")
            for line in diary_list:
                print(line)
                
    if f == 0:
        print("Bye now!")
        break
    