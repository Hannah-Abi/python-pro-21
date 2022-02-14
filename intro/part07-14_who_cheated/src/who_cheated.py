# Write your solution here
import datetime
import csv
def cheaters():
    start_dict = {}
    cheater = []
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            time_str = line[1].split(":")
            time = datetime.timedelta(hours= int(time_str[0]) , minutes= int(time_str[1]))
            start_dict[line[0]] = time
        #print(start_dict['matti'])
    with open("submissions.csv") as sub_file:
        for line in csv.reader(sub_file, delimiter=";"):
            time_str = line[3].split(":")
            time = datetime.timedelta(hours= int(time_str[0]) , minutes= int(time_str[1]))
            if line[0] in start_dict:
                diff_hour = (time-start_dict[line[0]]).total_seconds()/3600
                if diff_hour > 3 and line[0] not in cheater:
                    cheater.append(line[0])
    return cheater

if __name__=="__main__":
    print(cheaters())