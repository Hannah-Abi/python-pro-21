# Write your solution here
def anagrams(a1,a2):
    order_a1 = sorted(a1)
    order_a2 = sorted(a2)
    if order_a1 == order_a2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False