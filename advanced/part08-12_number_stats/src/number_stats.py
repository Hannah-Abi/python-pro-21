# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.avg = 0

    def add_number(self, number:int):
        self.numbers += number
        self.count += 1

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        return self.numbers
    
    def average(self):
        if self.count != 0:
            self.avg = self.numbers/self.count
        else:
            self.avg = 0
        return self.avg

# Test the scr
stats = NumberStats()
sum_even = 0
sum_odd = 0
while True:
    ipt_number = int(input("Please type in integer numbers:"))
    if ipt_number != -1:
        stats.add_number(ipt_number)
        if ipt_number%2 == 0:
            sum_even += ipt_number
        else:
            sum_odd += ipt_number
    else:
        break
    #print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)    