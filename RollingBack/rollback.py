""" Account Class """
import sqlite3
import pytz
import datetime

DB = sqlite3.connect("RollingBack\\account.sqlite")
DB.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
DB.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, \
    account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account():
    """ Class to represent an Account """

    def __init__(self, name: str, opening_balance: int = 0):
        """ Initialize
        Arguments:
            name {str} -- Name of account holder
        Keyword Arguments:
            opening_balance {int} -- Opening Balance (default: {0.0})
        """

        cursor = DB.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print(f"Retrieved record for {self.name}", end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print(f"Account created for {self.name}", end='')
        self.show_balance()

    def deposit(self, amount: int) -> float:
        """ Deposit into account
        Arguments:
            amount {float} -- Amount to deposit
        Returns:
            float -- Current Balance
        """
        if amount > 0.0:
            new_balance = self._balance + amount
            deposit_time = pytz.utc.localize(datetime.datetime.utcnow())
            DB.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            DB.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            DB.commit()
            self._balance = new_balance
            print(f"{amount/100:.2f} deposited")
        return self._balance/100

    def withdraw(self, amount: int) -> float:
        """ Withdraw from account
        Arguments:
            amount {float} -- Amount to withdraw
        Returns:
            float -- Current Balance
        """
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount/100:.2f} withdrawn")
            return amount / 100
        else:
            print(
                "The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        """ Display Account Balance
        Returns:
            string -- Displaying Current Balance
        """
        print(f"Balance on account {self.name} is {self._balance/100:.2f}")


if __name__ == "__main__":
    JOHN = Account("John")
    JOHN.deposit(1010)
    JOHN.deposit(10)
    JOHN.deposit(10)
    JOHN.withdraw(30)
    JOHN.withdraw(0)
    JOHN.show_balance()

    TERRYJ = Account("TerryJ")
    GRAHAM = Account("Graham", 9000)
    ERIC = Account("Eric", 7000)
    MICHAEL = Account("Michael", 500)
    TERRYG = Account("TerryG")

    DB.close()
