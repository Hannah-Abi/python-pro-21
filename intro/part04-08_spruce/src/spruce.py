# Write your solution here
def spruce(n):
    row = "*"
    print("a spruce!")
    while n > 0:
        print(" " * (n-1) + row + " " * (n-1))
        row += "**"
        n -= 1
    l = int((len(row)-3)/2)
    print(" " * l  + "*" + " " * l)
# You can test your function by callil
if __name__ == "__main__":
    spruce(5)
    spruce(4)