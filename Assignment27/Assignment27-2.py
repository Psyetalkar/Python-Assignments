class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("----------------------------")
        print("Account Holder :", self.Name)
        print("Balance        :", self.Amount)
        

    def Deposit(self, Money):
        print("----------------------------")
        self.Amount += Money
        print("Deposited :", Money)

    def Withdraw(self, Money):
        print("----------------------------")

        if Money <= self.Amount:
            self.Amount -= Money
            print("Withdrawn :", Money)
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):

        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


 

Obj1 = BankAccount("Rahul", 50000)

Obj1.Display()

Obj1.Deposit(10000)
Obj1.Display()

Obj1.Withdraw(15000)
Obj1.Display()

print("Interest =", Obj1.CalculateInterest())

print()

Obj2 = BankAccount("Priya", 75000)

Obj2.Display()

Obj2.Deposit(5000)
Obj2.Withdraw(20000)
Obj2.Display()

print("Interest =", Obj2.CalculateInterest())


 