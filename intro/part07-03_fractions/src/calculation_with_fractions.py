# Write your solution here
import fractions
def fractionate(amount: int):
    frac_list = []
    numerator = 1
    demonerator = amount
    p = fractions.Fraction(numerator,demonerator)
    i = 1
    while i <= amount:
        frac_list.append(p)
        i += 1
    return frac_list

if __name__=="__main__":
    for p in fractionate(3):
        print(p)
    print()
    print(fractionate(5))