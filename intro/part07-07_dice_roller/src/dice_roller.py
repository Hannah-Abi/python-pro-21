# Write your solution here
import random
import string
def roll(die: str):
    a = [3, 3, 3, 3, 3, 6]
    b = [2, 2, 2, 5, 5, 5]
    c = [1, 4, 4, 4, 4, 4]
    if die == "A":
        dice = random.choice(a)
    if die == "B":
        dice = random.choice(b)
    if die == "C":
        dice = random.choice(c)
    return dice

def play(die1: str, die2: str, times: int):
    times_r1_won = 0
    times_r2_won = 0
    for i in range(times):
        r1 = roll(die1)
        r2 = roll(die2)
        if r1 > r2:
            times_r1_won += 1
        elif r1 <r2:
            times_r2_won += 1
    tup = (times_r1_won,times_r2_won,times-times_r1_won-times_r2_won)
    return tup
if __name__=="__main__":
    #for i in range(10):
        #print(roll("A"), " ", end="")
    result = play("A", "C", 1000)
    print(result)

   