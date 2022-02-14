# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name: str, number: str, balance: float):
        self.__name = name
        self.__number = number
        self.__balance = balance
        #self.__service_charge()
    
    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance -= 1/100*self.__balance

    def deposit(self, amount: float):
        if amount >= 0:
            self.__balance += amount
            if self.__balance:
                self.__service_charge()
        else:
            raise ValueError("The amount must not be below zero")
        
    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)




