# Write your solution here:
def order_by_price(item: tuple):
    # Return the price, which is the second item within the tuple
    return item[2]

def sort_by_remaining_stock(items: list):
    return sorted(items, key=order_by_price)

if __name__ == "__main__":
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[2]} pcs")