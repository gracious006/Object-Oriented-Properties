from account import Account


class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def withdrawal(self, amount):
        if amount < 2000:
            super() . withdraw(amount)
        else:
            print("you can not withdraw above your limit")


SavingsAccount = SavingsAccount()
SavingsAccount.withdraw(2000)
