# Write your solution here
def chessboard(x):
    t1 = "1"
    t2 = "0"
    s = 0
    if (x%2 == 0):
        s = int(x/2)
        print(((t1+t2)*s + "\n" + (t2+t1)*s+"\n")*s)
    else:
        s = int((x-1)/2)
        print(((t1+t2)*s +t1 + "\n" + (t2+t1)*s+ t2+"\n")*s + (t1+t2)*s +t1 + "\n" )
    


# Testing the function
if __name__ == "__main__":
    chessboard(3)
