# Write your solution here
def palindromes(word):
    palin = word[::-1]
    if palin == word:
        return True
    else:
        return False
def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word) == True:
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")
    
# Note, that at this time the main program should not be written inside
#if __name__ == "__main__":
    #main()
# block!
main()
