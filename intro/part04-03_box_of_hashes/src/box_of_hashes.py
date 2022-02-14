# Copy here code of line function from previous exercise
def line(number, text):
    if len(text) == 0:
        print("*" * number)
    else:
        print(text[0]*number)
def box_of_hashes(height):
    # You should call function line here with proper parameters
    count = 1
    while count <= height:
        line(10, "#")
        count += 1
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
