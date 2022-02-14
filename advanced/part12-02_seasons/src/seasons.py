# Write your solution here:
# Write your solution here:
def order_by_price(item: dict):
    # Return the price, which is the second item within the tuple
    return item["seasons"]

def sort_by_seasons(items: list):
    return sorted(items, key=order_by_price)

if __name__ == "__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    for show in sort_by_seasons(shows):
        print(f"{show['name']} {show['seasons']} seasons")