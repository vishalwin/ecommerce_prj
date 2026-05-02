

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = amount

    def withdraw(self, amount):
        raise NotImplementedError

    def get_balance(self):
        raise NotImplementedError

def test_deposit():
    account = BankAccount()
    account.deposit(100)
    assert account.balance == 100