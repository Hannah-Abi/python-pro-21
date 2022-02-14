# Write your solution here
year = int(input("YEAR: "))
t = 0
while True:
    t += 1
    if ((year + t)%4 == 0):
        if (year + t)%100 != 0:
            print(f"The next leap year after {year} is {year+t}")
            break
        else:
            if (year + t)%400 == 0:
                print(f"The next leap year after {year} is {year+t}")
                break
            else:
                print(f"The next leap year after {year} is {year+t+4}")
                break

        
            
