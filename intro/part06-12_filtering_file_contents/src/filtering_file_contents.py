# Write your solution here
import operator
def filter_solutions():
    ops = {
        '+' : operator.add,
        '-' : operator.sub}
    with open("solutions.csv") as new_file:
        correct = []
        incorrect = []
        for line in new_file:
            s_line = line.replace("\n", "").split(";")
            if len(line) > 1:
                if s_line[1].find("+") != -1:
                    l = s_line[1].split("+")
                    if int(l[0]) + int(l[1]) == int(s_line[2]):
                        correct.append(line)
                    else:
                        incorrect.append(line)
                elif s_line[1].find("-") != -1:
                    l = s_line[1].split("-")
                    if int(l[0]) - int(l[1]) == int(s_line[2]):
                        correct.append(line)
                    else:
                        incorrect.append(line)      
        with open("correct.csv", "w") as my_file:
            for value in correct:
                my_file.write(value)
        with open("incorrect.csv", "w") as my_file:
            for value in incorrect:
                my_file.write(value)
if __name__ == "__main__":
    filter_solutions()