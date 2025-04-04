class BankAccount:

    def __init__(self, acc_holder, balance=0):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited INR {amount}\n Current balance is INR {self.balance}")

    def withdraw(self,amount): #instance method and variable (self)
        if self.balance < amount:
            print(f"Current balance is INR {self.balance}")
        else:
            self.balance -= amount
        print(f"Current balance is INR {self.balance}")

    def set_intrest_rate(cls, new_rate):  # class method (cls)
        cls.intrest = new_rate
        print()

    set_intrest_rate = classmethod(set_intrest_rate) 

    def validate_account_number(account_number):   
        return len(str(account_number)) == 10 and str(account_number).isdigit()
    
    validate_account_number = staticmethod(validate_account_number)
    


if __name__ == "__main__":
    acc1 = BankAccount("Anvi", 5000)

    if BankAccount.validate_account_number('1234567890'):
        acc1.deposit(5000)
        acc1.withdraw(3000)

        BankAccount.set_intrest_rate(8)

    