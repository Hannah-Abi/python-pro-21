# Write your solution here
def longest(strings: list):
    longest_item = strings[0]
    for item in strings:
        if len(item) > len(longest_item):
            longest_item = item
    return longest_item
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))