# Write your solution here
def read_input(text: str, start_point: int, end_point: int):
    while True:
        try:
            input_str = input(text)
            number = int(input_str)
            if number in range(start_point, end_point +1):
                return number
        except ValueError:
            pass
        print("You must type in an integer between 5 and 10")


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
