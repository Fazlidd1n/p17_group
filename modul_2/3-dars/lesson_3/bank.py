class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def transform(self , amount):
        if amount > 0:
            self._balance += amount
            print("Successfully transform !")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if not 0 < amount < self._balance:
            print("Mablag' yetarli emas !")
            return
        self._balance -= amount





acc1 = BankAccount("123456", 50000)
print(acc1.get_account_number())
print(acc1.get_balance())
acc1.transform(10000)
print(acc1.get_balance())
acc1.withdraw(70000)
print(acc1.get_balance())


