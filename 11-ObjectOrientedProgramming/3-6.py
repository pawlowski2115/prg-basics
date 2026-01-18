class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def display(self):
        print(f"Bank account No: {self.account_number} \nBalance: PLN {self.balance:.2f}")
    def deposit(self,dep_amount):
        self.balance += dep_amount
    def withdraw(self,wtd_amount):
        if wtd_amount > self.balance:
            print("Insufficient funds on the account")
        else:
            self.balance -= wtd_amount


def main():
    bank = BankAccount("12 3456 5555 9090 1111 0000 7722")
    bank.display()
    bank.deposit(25.30)
    bank.display()
    bank.withdraw(31.70)
    bank.display()
    bank.withdraw(14)
    bank.display()


if __name__=="__main__":
    main()


        