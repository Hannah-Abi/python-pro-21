# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.room = []
    
    def add(self, person: Person):
        self.room.append(person)
    
    def is_empty(self):
        if not self.room:
            return True
        else:
            return False
    
    def print_contents(self):
        total_height = 0
        for room in self.room:
            total_height += room.height
        print(f"There are {len(self.room)} persons in the room, and their combined height is {total_height} cm")
        for room in self.room:
            print(f"{room.name} ({room.height} cm)")
        
    def shortest(self):
        if not self.room:
            return None
        else:
            shortest_person = self.room[0]
            for room in self.room:
                if room.height < shortest_person.height:
                    shortest_person = room
            return shortest_person
    
    def remove_shortest(self):
        if not self.room:
            return None
        else:
            shortest_person = self.shortest()
            for room in self.room:
                if room.name == shortest_person.name:
                    self.room.remove(room)
                    return room
if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()