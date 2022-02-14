# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        fruits_dict = {}
        for line in new_file:
            line = line.replace("\n", "")
            fruits = line.split(";")
            if fruits[0] not in fruits_dict:
                fruits_dict[fruits[0]] = ""
            fruits_dict[fruits[0]] = float(fruits[1])
    return fruits_dict

if __name__ == "__main__":
    read_fruits()