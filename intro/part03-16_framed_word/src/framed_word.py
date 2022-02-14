# Write your solution here
s = input("Please type in a string: ")
print("*" * 30)
line = ""
if len(s)%2 == 0:
    line = " " * int((30-2-len(s))/2)
    print(f"*{line}{s}{line}*")
else:
    line = " " * int((30-3-len(s))/2)
    print(f"*{line}{s}{line} *")

print("*" * 30)