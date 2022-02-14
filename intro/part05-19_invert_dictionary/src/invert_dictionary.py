# Write your solution here
def invert(dictionary: dict):
    key_list = []
    val_list = []
    for key in dictionary:
        key_list.append(key)
        val_list.append(dictionary[key])
        #dic_list.append(list)
    print(key_list)
    print(val_list)
    dictionary.clear()
    i = 1
    for i in range(len(key_list)):
        if val_list[i] not in dictionary:
            dictionary[val_list[i]] = ""
        dictionary[val_list[i]] = key_list[i]
        #i += 2
if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
