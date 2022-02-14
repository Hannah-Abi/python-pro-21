# tee ratkaisu tänne
# Write your solution here
import math
def get_station_data(filename: str):
    names = {}
    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(";")
            # ignore the header line
            if parts[0] == "Longitude":
                continue
            names[parts[3]] = (float(parts[0]),float(parts[1]))
    return names

def distance(stations: dict, station1: str, station2: str):
    for k in stations:
        if (station1 in stations) and (station2 in stations):
            x_km = (stations[station2][0] - stations[station1][0]) * 55.26
            y_km = (stations[station2][1] - stations[station1][1]) * 111.2
        distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    d_list = {}
    for k1 in stations:
        for k2 in stations:
            d = distance(stations, k2, k1)
            if d not in d_list:
                d_list[d] = ''
            d_list[d] = [k2,k1]
    d_max = 0
    for k in d_list:
        if k>d_max:
            d_max = k
    return (d_list[d_max][0], d_list[d_max][1], d_max)

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    #print(stations)
    #d = distance(stations, "Designmuseo", "Hietalahdentori")
    #print(d)
    #d = distance(stations, "Viiskulma", "Kaivopuisto")
    #print(d)
    d = distance(stations, "Kaivopuisto", "Laivasillankatu")
    print(d)