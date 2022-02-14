# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__amount = 0
        self.__obs = []

    def add_observation(self, observation: str): 
        self.__obs.append(observation)
        self.__amount += 1

    def latest_observation(self):
        if not self.__obs:
            return ""
        else:
            return self.__obs[-1]
                
    def number_of_observations(self):
        return self.__amount

    def __str__(self) -> str:
        return f"{self.__name}, {self.__amount} observations"

if __name__=="__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)

    

