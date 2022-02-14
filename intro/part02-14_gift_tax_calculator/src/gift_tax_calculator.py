# Write your solution here
gift = int(input("Value of gift: "))
tax= 0
if (gift < 5000):
    print("No tax!")
if (gift > 5000):
    if (5000 <= gift < 25000):
        tax = 100 + (gift - 5000)*0.08
    if (25000 <= gift < 55000):
        tax = 1700 + (gift - 25000)*0.1
    if (55000 <= gift < 200000):
        tax = 4700 + (gift - 55000)*0.12
    if (200000 <= gift < 1000000):
        tax = 22100 + (gift - 200000)*0.15  
    if (gift > 1000000):
        tax = 142100 + (gift - 1000000)*0.17 
    print(f"Amount of tax: {tax}")

