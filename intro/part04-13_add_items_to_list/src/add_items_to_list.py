# Write your solution here
list = []
len = int(input("How many items: "))
i = 1
while i <= len:
    item = int(input(f"Item {i}: "))
    list.append(item)
    i += 1
print(list)