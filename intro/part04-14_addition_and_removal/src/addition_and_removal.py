# Write your solution here
l = []
print ("The list is now []")
i = 1
while True:
    opt = input("a(d)d, (r)emove or e(x)it: ")
    if (opt == "d"):
        l.append(i)
        print ("The list is now ", end = "")
        print(l)
        i += 1
    if (opt == "r"):
        l.pop(-1)
        print ("The list is now ", end = "")
        i -= 1
        print(l)
    if (opt == "x"):
        print("Bye!")
        break


