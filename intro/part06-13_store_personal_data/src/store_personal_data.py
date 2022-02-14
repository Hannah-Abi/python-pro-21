# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "w") as new_file:
        line = f"{person[0]};{str(person[1])};{float(person[2])}"
        new_file.write(line)
if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))