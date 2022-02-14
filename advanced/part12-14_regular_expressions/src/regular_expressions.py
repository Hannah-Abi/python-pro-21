# Write your solution here
import re
def is_dotw(my_string: str):
    if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string):
        return True
    return False

def all_vowels(my_string: str):
    if re.search("^[aeiouy]*$", my_string):
        return True
    return False

def time_of_day(my_string: str):
    if re.search("^(2[0-3]|1[0-9]|0[1-9]):(0[1-9]|[0-5][0-9]):(0[1-9]|[0-5][0-9])$", my_string):
        #$:^([0-5]\d){1}$:^([0-5]\d){1}$
        #
        return True
    return False

if __name__=="__main__":
    #Test 1
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))
    print("----------------------------------")
    #Test 2
    print(all_vowels("eioueioieoieouyyyy"))
    print(all_vowels("autooo"))
    print("----------------------------------")
    #Test 3
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("119:59:xx"))
    print(time_of_day("33:66:77"))     
