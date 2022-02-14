# Write your solution here:
from datetime import datetime, timedelta
class Clock():
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 00
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.minute == 60 and self.second == 60:
            self.minute = 0
            self.second = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0
    
    def set(self, h:int, minute: int):
        self.hour = h
        self.minute = minute
        self.second = 0

    def __str__(self):
        set_time = f"{self.hour}:{self.minute}:{self.second}"
        time_format_str = "%H:%M:%S"
        time = datetime.strptime(set_time, time_format_str).time()
        return str(time)
    
if __name__=="__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.set(12, 5)
    print(clock)

