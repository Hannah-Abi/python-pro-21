# Write your solution here
from datetime import datetime, time, timedelta
filename = input("Filename: ")
with open(filename, "w") as time_file:
    date_input = input("Starting date: ")
    no_of_day = int(input("How many days: "))
    date_list = date_input.split(".")
    # get the start date
    start_date = datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]))
    # get the last date
    last_date =start_date + timedelta(days=no_of_day-1)
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    input_list = []
    total = 0
    for i in range(0, no_of_day):
        # input the screen time
        scr_time = input(f"Screen time {start_date + timedelta(days=i)}: ")
        #calculate the total minuties of screen time 
        scr = scr_time.split(" ")
        scr_list = [int(k) for k in scr]
        total += sum(scr_list)
        # add string of date and screen time to a list
        screen_time_str = scr_time.replace(" ", "/")
        date = (start_date + timedelta(days=i)).strftime("%d.%m.%Y")
        input_list.append(f"{date}: {screen_time_str}")
    # add data to the file
    fDate_str = start_date.strftime("%d.%m.%Y")
    lDate_str = last_date.strftime("%d.%m.%Y")
    time_file.write(f"Time period: {fDate_str}-{lDate_str}\n")
    time_file.write(f"Total minutes: {total}\n")
    time_file.write(f"Average minutes: {total/no_of_day}\n")
    for i in range(len(input_list)):
        time_file.write(f"{input_list[i]}\n")
    print("Data stored in file late_june.txt")