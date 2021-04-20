import threading


class BankAccount:
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = None
        self.active = False

    def get_balance(self):
        self.validate_account()
        return self.balance

    def open(self):
        if not self.active:
            self.active = True
            self.balance = 0
        else:
            raise ValueError('Cannot open an opened account')

    def deposit(self, amount):
        with self.lock:
            self.validate_account()
            self.validate_amount(amount)
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            self.validate_account()
            self.validate_amount(amount)

            if self.balance - amount < 0:
                raise ValueError('Cannot withdraw more than you have')

            self.balance -= amount

    def close(self):
        if self.active:
            self.active = False
            self.balance = None
        else:
            raise ValueError('Cannot close a closed account')
        self.balance = None

    @staticmethod
    def validate_amount(amount):
        if amount < 0:
            raise ValueError('Amount must be positive')

    def validate_account(self):
        if not self.active:
            raise ValueError('Cannot make transaction in a closed account')
