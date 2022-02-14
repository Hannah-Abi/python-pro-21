# Write your solution here\
from datetime import datetime
from datetime import date
def is_it_valid(pic: str):
    full_month = [1,3,5,7,8,10,12]
    miss_month = [4,6,9,11]
    valid_markers = ["-","+","A"]
    control_cha_list = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    day = int(pic[:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    cent_marker = pic[6]
    #find remainder 
    r = int(pic[:6] + pic[7:10])%31
    check_valid = False
    #print(int(cha_str))
    if len(pic) == 11:
        if cent_marker in valid_markers:
            if pic[-1] == control_cha_list[r]:
                if day in range(1,32) and month in full_month:
                        check_valid = True 
                if day in range(1,31) and month in miss_month:
                        check_valid = True
                if month == 2:
                    day_range = (date(2012, 3, 1) - date(2012, 2, 1))
                    if cent_marker == "-":
                        full_y = int("19") + year
                        dif = datetime(full_y,3, 1) - datetime(full_y,2,1)
                        if day in range(1,int(dif.days) +1):
                            check_valid = True
                    if cent_marker == "+":
                        full_y = int("18") + year
                        dif = datetime(full_y,3, 1) - datetime(full_y,2,1)
                        if day in range(1,int(dif.days) +1):
                            check_valid = True
                    if cent_marker == "A":
                        full_y = int("20") + year
                        dif = datetime(full_y,3, 1) - datetime(full_y,2,1)
                        if day in range(1,int(dif.days) +1):
                            check_valid = True
    return check_valid
if __name__=="__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
    print(is_it_valid('140216+523M'))

