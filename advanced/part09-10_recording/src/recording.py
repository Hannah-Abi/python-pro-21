# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length: float):
        self.__length = length
        if length < 0:
            raise ValueError("Sorry, no numbers below zero")
    
    @property
    def length(self):
        return self.__length 
    
    @length.setter
    def length(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The amount must not be below zero")

if __name__ == "__main__":
    the_wall = Recording(-1)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)