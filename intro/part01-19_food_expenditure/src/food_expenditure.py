# Write your solution here
times = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
exp = float(input("How much money do you spend on groceries in a week? "))
total = times*price+exp
avg = total/7
print("Average food expenditure:\n")
print(f"Daily: {avg} euros")
print(f"Weekly: {total} euros")