# Copy here code of line function from previous exercise and use it in your solution
def line(number, text):
    if len(text) == 0:
        print("*" * number)
    else:
        print(text[0]*number)
def shape(n1, s1, n2, s2):
    c = 1
    while c <= n1:
        line(c, s1)
        c += 1
    i = 1
    while i <= n2:
        line(n1, s2)
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
    shape(2, "o", 4, "+")