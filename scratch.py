class banking():
    def __init__(self,name,account_no,balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def balance_inquriy(self):
        print("Accouont Holder name : ..... " + self.name.title())
        print("Youe balance:")
        print(str(self.account_no) + " : ........... " + str(self.balance))

    def withdraw(self):
        amount = int(input("Enter Amount for withdraw : "))
        if amount <= self.balance:
            self.balance -= amount
            print(str(amount) + " is suceesfully withdrwa.... Thank you for banking .")
        else:
            print("you Don't have sufficient balance. plese check your balance.")

    def deposite(self):
        amount = int(input("Enter Amount for deposite : "))
        self.balance += amount
        print(str(amount) + " is suceesfully Deposite.... Thank you for banking .")


class Saving_account(banking):
    def __init__(self,name, account_no, balance):
        super().__init__(name, account_no, balance)

    def deposite(self):
        super(Saving_account, self).deposite()
        self.balance += (self.balance * 0.06)