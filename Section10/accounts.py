import datetime
import pytz

class Account:
    """ Simple account class with ballance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print(f"Account created for {self.name}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.balance}")

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{amount:6} {tran_type} on {date} (local time was {date.astimezone()})")


if __name__ == "__main__":
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)

    tim.withdraw(50000)



