# Write your solution here
import string
alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)
print(alphabet_list)

n = int(input("Layers: "))
# To access rows of the square
for i in range(n*2):
    # To access columns of the square
    for j in range(n*2):
        if (i == 0 or i == (n*2-1) or j == 0 or j == (n*2-1)):
            print(alphabet_list[n-1], end='')
        else:  
            print(" ", end='')
    print()


