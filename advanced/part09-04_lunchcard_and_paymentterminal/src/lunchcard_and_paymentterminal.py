# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
            return True
        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        self.funds += 2.5
        # increase the number of lunches sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        if payment >= 2.5:
            payment -= 2.5
            self.lunches += 1
        return payment

    def eat_special(self, payment: float):
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        self.funds += 4.3
        # increase the number of specials sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        if payment >= 4.3:
            payment -= 4.3
            self.specials += 1
        return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        if card.balance >= 2.5:
            card.balance -= 2.5
            self.lunches += 1
            check = True

        else:
            check = False
        # and return True. If not, return False.
        return check

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        if card.balance >= 4.3:
            card.balance -= 4.3
            self.specials += 1
            check = True
        else:
            check = False
        # and return True. If not, return False.
        return check

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount
        self.funds += 100
        return card.balance

if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(500)
    print("Balance", card.balance)
    result = card.subtract_from_balance(100)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(200)
    print("Payment successful:", result)
    result = card.subtract_from_balance(200)
    print("Payment successful:", result)
    result = card.subtract_from_balance(100)
    print("Payment successful:", result)
    print("Balance", card.balance)