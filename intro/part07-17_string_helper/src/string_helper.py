# Write your solution here
def change_case(orig_string: str) -> str:
    new_string = ""
    part = list(orig_string)
    for letter in part:
        if letter.islower():
            letter = letter.upper()
        else:
            letter = letter.lower()
        new_string += letter
    return new_string

def split_in_half(orig_string: str) -> tuple:
    length_string = len(orig_string)
    if length_string%2 == 0:
        half = int(length_string/2)
        parts = (orig_string[:half],orig_string[half:])
    else:
        half = int((length_string-1)/2)
        parts = (orig_string[:half],orig_string[half:])
    return parts

def remove_special_characters(orig_string: str):
    new_string = ""
    part = list(orig_string)
    for l in part:
        if l.isalnum() or l == " ":
            new_string += l
    return new_string
if __name__=="__main__":
    my_string = "Well hello there!"
    test_string = "This is a test, lets see how it goes!!!11!"
    print(change_case(my_string))
    print(split_in_half(my_string))
    print(remove_special_characters(test_string))