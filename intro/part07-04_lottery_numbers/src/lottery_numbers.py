# Write your solution here
from random import randint
def lottery_numbers(amount: int, lower: int, upper: int):
    part = []
    i = 1
    while i <= amount:
        p = randint(lower,upper)
        if p not in part:
            part.append(p)
            i += 1
    part.sort()
    return part
if __name__=="__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
