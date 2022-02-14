# Write your solution here:
from datetime import datetime
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 00
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
    def __str__(self):
        date_format_str = "%M:%S"
        time = f"{self.minutes}:{self.seconds}"
        t = datetime.strptime(time, date_format_str).time()
        return f"{t.minute:02d}:{t.second:02d}"


if __name__=="__main__":
    watch = Stopwatch()
    for i in range(60):
        print(watch)
        watch.tick()
        
