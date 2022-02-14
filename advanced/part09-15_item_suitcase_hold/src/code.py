# Write the class "Item"
class Item:
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight

    @property
    def name(self):
        return self.__name
    
    @property
    def weight(self):
        return self.__weight
        
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"

#Write the class"Suitcase":
class Suitcase:
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight
        self.__item_list = []
        self.__current_weight = 0
    
    def add_item(self, item: Item):
        w = item.weight()
        n = item.name()
        if self.__current_weight + w <= self.__max_weight:
            self.__item_list.append(item)
            self.__current_weight += w
    
    def print_items(self):
        for item in self.__item_list:
            print(f"{item.name()} ({item.weight()} kg)")
    
    def weight(self):
        return self.__current_weight

    def heaviest_item(self):
        if not self.__item_list:
            return None
        else:
            heaviest_item = self.__item_list[0]
            for item in self.__item_list:
                if item.weight() >= heaviest_item.weight():
                    heaviest_item = item
            return heaviest_item
                

    def __str__(self) -> str:
        list_item = ""
        if len(self.__item_list) == 0:
            list_item = f"0 items (0 kg)"
        elif len(self.__item_list) == 1:
            list_item = f"{len(self.__item_list)} item ({self.__current_weight} kg)"
        else:
            list_item = f"{len(self.__item_list)} items ({self.__current_weight} kg)"
        return list_item

# Write the class "CargoHold":
class CargoHold:
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight
        self.__suitcase_list = []
        self.__current_w = 0
    
    def add_suitcase(self, suitcase: Suitcase):
        w = suitcase.weight()
        if self.__current_w + w <= self.__max_weight:
            self.__suitcase_list.append(suitcase)
            self.__current_w += w

    def print_items(self):
        for suitcase in self.__suitcase_list:
            suitcase.print_items()
            
    def __str__(self) -> str:
        suitcase_str = ""
        if len(self.__suitcase_list) == 0:
            suitcase_str = f"0 suitcases, space for {self.__max_weight} kg"
        elif len(self.__suitcase_list) == 1:
            suitcase_str = f"1 suitcase, space for {self.__max_weight - self.__current_w} kg"
        else:
            suitcase_str = f"{len(self.__suitcase_list)} suitcases, space for {self.__max_weight - self.__current_w} kg"
        return suitcase_str
if __name__=="__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()