# Write your solution here
while True:
    editor = input("Editor: ")
    e = editor.lower()
    if e == "visual studio code":
        print("an excellent choice!")
        break
    elif e == "emacs" or e == "atom":
        print("not good")
    else:
        print("awful")