class Accont():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner: {self.owner} and Account Balance: {self.balance}"

    def deposit(self,amount):

        self.balance = self.balance + amount
        return f"Deposit accepted and balance is {self.balance}"


    def withdraw(self, amount):

        self.balance = self.balance - amount
        if self.balance < 0:
            self.balance = self.balance + amount
            return f"withdraw not accepted and balance is {self.balance}"
        else:

            return f"withdraw accepted and balance is {self.balance}"


a = Accont("Ruchir", 100)

print(a.balance)
print(a.owner)
print(a.deposit(100))
print(a.withdraw(50))
print(a)
print(a.withdraw(1000))



