# Write your solution here
l = [1, 2, 3, 4, 5]
while True:
    ind = int(input("Index: "))
    if (ind == -1):
        break
    new_val = int(input("New value: "))
    l[ind] = new_val
    print(l)