# Write your solution here
def same_chars(str, i1,i2):
    if (i1 >= len(str) or i2 >= len(str)):
        return False
    else:
        if (str[i1] == str[i2]):
            return True
        else:
            return False
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("coder", 1, 10))