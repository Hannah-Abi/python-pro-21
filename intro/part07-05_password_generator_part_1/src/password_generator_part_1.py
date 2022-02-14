# Write your solution here
import string
import random
def generate_password(amount:int):
    i = 1
    password = ""
    choice = random.choices(string.ascii_lowercase, k = amount)
    for i in range(len(choice)):
        password += choice[i]
    return password

if __name__=="__main__":
    for i in range(10):
        print(generate_password(8))