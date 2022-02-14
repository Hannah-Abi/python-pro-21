# Write your solution here
line = "1"
sum = 1
count = 2
limit = int(input("Limit: "))
while sum < limit:
    sum += count
    line += f" + {count}"
    count += 1
print(f"The consecutive sum: " + line + f" = {sum}")