# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, tuote: str, maara: int):
        self.products.append((tuote, maara))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

    def add_item(self, tuote: str, maara: int):
        self.products.append((tuote, maara))

# -------------------------
# Write your solution here:
def total_units(my_list: ShoppingList):
    total = 0
    for i in range(1, my_list.number_of_items()+1):
        total += my_list.amount(i)
    return total

if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add_item("bananas", 10)
    my_list.add_item("apples", 5)
    my_list.add_item("pineapple", 1)

    print(total_units(my_list))
# -------------------------
