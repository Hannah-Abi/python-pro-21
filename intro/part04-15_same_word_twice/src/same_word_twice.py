# Write your solution here
l = []
count = 0
while True:
    word = input("Word: ")
    Found = False
    for i in range(len(l)):
        if (word == l[i]):
            Found = True
            break
    if Found == True:
        print(f"You typed in {count} different words")
        break
    else:
        l.append(word)
        count += 1




