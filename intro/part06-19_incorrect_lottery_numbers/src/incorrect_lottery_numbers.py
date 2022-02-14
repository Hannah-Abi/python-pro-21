# Write your solution here
def filter_incorrect():
    try:
        with open("lottery_numbers.csv") as lot_file:
            lottery_list = []
            for line in lot_file:
                s_line = line.strip().split(";")
                week = s_line[0].split(" ")
                lottery_no = s_line[1].split(",")
                #print(week)
                #print(lottet_no)
                found = False
                if len(lottery_no) == 7:
                    try:
                        week_order = int(week[1])
                        check_dup = []
                        for l in lottery_no:
                            lot_no = int(l)
                            if lot_no not in check_dup:
                                check_dup.append(lot_no)
                            if lot_no not in range(1,40):
                                found = True
                    except:
                        pass
                    else:
                        if found == False and len(lottery_no) == len(check_dup):
                            lottery_list.append(line)

        with open("correct_numbers.csv", "w") as my_file:
            for line in lottery_list:
                my_file.write(line)
    except:
        print("There was an error when reading the file.")
if __name__ == "__main__":
    filter_incorrect()



            
    
