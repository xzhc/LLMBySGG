"""
This case demonstrates the design of a Credit Card class using encapsulation
"""

class CreditCard:
    def __init__(self, name):
        self.name = name
        self.__password = None
        self.__balance = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password != "888888":
            print("Incorrect password entered")
        else:
            print("Correct password entered")
            self.__password = password

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            print('Consume reationally, your credit card is overdrawn')
        else:
            print("Payment successful")
            self.__balance = balance

c1 = CreditCard('xzh')
# c1.password = '123456'
c1.password = "888888"
# c1.balance = 100
c1.balance = -100