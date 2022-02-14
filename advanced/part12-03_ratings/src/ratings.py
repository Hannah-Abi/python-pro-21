# TEE RATKAISUSI TÄHÄN:
# Write your solution here:
# Write your solution here:
def order_by_price(item: dict):
    # Return the price, which is the second item within the tuple
    return item["rating"]

def sort_by_ratings(items: list):
    return sorted(items, key=order_by_price, reverse=True)

if __name__ == "__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    print("Rating according to IMDB")
    for show in sort_by_ratings(shows):
        print(f"{show['name']}  {show['rating']}")