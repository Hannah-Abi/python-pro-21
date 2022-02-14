# Write your solution here
hw = float(input("Hourly wage: "))
h = float(input("Hours worked: "))
d = input("Day of the week: ")
condition = d =="Sunday"
dw = 0
if condition:
    dw = hw * h*2
if (condition == False):
    dw = hw * h
print(f"Daily wages: {dw} euros")