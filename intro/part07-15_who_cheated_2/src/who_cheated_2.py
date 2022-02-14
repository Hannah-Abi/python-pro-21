import datetime
import csv
from typing import final
def final_points():
    start_time= {}
    final_points = {}
    
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            time_str = line[1].split(":")
            time = datetime.timedelta(hours= int(time_str[0]) , minutes= int(time_str[1]))
            start_time[line[0]] = time
        #print(start_time)
    with open("submissions.csv") as sub_file:
        for line in csv.reader(sub_file, delimiter=";"):
            time_str = line[3].split(":")
            time = datetime.timedelta(hours= int(time_str[0]) , minutes= int(time_str[1]))
            if line[0] in start_time.keys():
                diff_hour = (time-start_time[line[0]]).total_seconds()/3600
                if diff_hour <= 3:
                    if line[0] not in final_points.keys():
                        final_points[line[0]] = [(line[1], int(line[2]))]
                    else:
                        for key in final_points.keys():
                            if line[0] == key:
                                if (line[1],line[2]) not in final_points[key]:
                                    final_points[key].append((line[1], int(line[2])))
        for name, tasks in final_points.items():
            d = dict()
            for k,v in tasks:
                if k in d.keys():
                    d[k] = max(v,d[k])
                else:
                    d[k] = v
            final_points[name] = d
        for name, tasks in final_points.items():
            total_point = 0
            for v in tasks.values():
                total_point += v
            final_points[name] = total_point
                

    return final_points

if __name__=="__main__":
    print(final_points())