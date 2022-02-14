# Write your solution here
def new_person(name: str, age: int):
    x = name.split()
    if (len(x) < 2 or len(name) not in range(2,41) or age not in range(0,151) ):
        raise ValueError("Invalid parameters")
    return (name, age)
if __name__ == "__main__":
    #print(new_person('Andrew', 32))
    print(new_person('James Jameson', 32))