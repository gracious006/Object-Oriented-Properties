from account import Account


class currentAccount(Account):
    def __init__(self):
        Account.__init__(self)


currentAccount = currentAccount()
currentAccount.deposit(5000)
currentAccount.withdraw(1500)
