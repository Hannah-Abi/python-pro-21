# Write your solution here
def prime_numbers():
    n = 1
    while n >= 1:
        n +=1
        for x in range(2,n):
            if n%x == 0:
                break
        else:
            yield n

if __name__=="__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))