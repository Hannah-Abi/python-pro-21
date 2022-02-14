# Copy here code of line function from previous exercise
def line(number, text):
    if len(text) == 0:
        print("*" * number)
    else:
        print(text[0]*number)
def triangle(size):
    # You should call function line here with proper parameters
    c = 1
    while c <= size:
        line(c, "#")
        c += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
