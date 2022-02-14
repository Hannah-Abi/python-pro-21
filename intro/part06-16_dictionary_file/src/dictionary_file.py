# add transalted word into dictionary
#with open("dictionary.txt", "w") as new_file:
    #pass
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    f = int(input("Function: "))
    if f == 1:
        fin_word = input("The word in Finnish: ")
        eng_word = input("The word in English: ")
        with open("dictionary.txt", "a+") as my_file:
            found = False
            for line in my_file:
                if fin_word in line:
                    found = True
            if found == False:
                my_file.write(f"{fin_word}: {eng_word}\n")
                print("Dictionary entry added")
    if f == 2:
        search_term = input("Search term: ")
        with open("dictionary.txt") as new_file:
            for line in new_file:
                line = line.replace("\n", "").split(": ")
                if search_term in line[0] or search_term in line[1]:
                    print(f"{line[0]} - {line[1]}")     
    if f == 3:
        print("Bye!")
        break
    
