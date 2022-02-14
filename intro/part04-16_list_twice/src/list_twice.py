# Write your solution here
l = []
while True:
    item = int(input("New item: "))
    if (item != 0):
        l.append(item)
        print("The list now: ", end = "")
        print(l)
        print("The list in order: ", end = "")
        print(sorted(l))
    else:
        print("Bye!")
        break

