# Write your solution here
def factorials(n: int):
    i = 1
    f = 1
    factorial_dic = {}
    while i < n+1:
        f = f*i
        factorial_dic[int(i)] = f
        i += 1
    return factorial_dic

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])