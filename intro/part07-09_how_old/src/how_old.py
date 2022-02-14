# Write your solution here
from datetime import datetime, time
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
time_now = datetime(1999,12,31)
time_born = datetime(year,month,day)
if time_now < time_born:
    print("You weren't born yet on the eve of the new millennium.")
else:
    dif = time_now-time_born
    print(f"You were {dif.days} days old on the eve of the new millennium.")