"""2: Write a Python program to implement a class named BankAccount with the following
requirements:
• The class should contain two instance variables:
◦ Name (Account holder name)
◦ Amount (Account balance)
• The class should contain one class variable:
◦ ROI (Rate of Interest), initialized to 10.5
• Define a constructor (__init__) that accepts Name and initial Amount.
• Implement the following instance methods:
◦ Display() - displays account holder name and current balance
◦ Deposit() - accepts an amount from the user and adds it to balance
◦ Withdraw() - accepts an amount from the user and subtracts it from balance
(Ensure withdrawal is allowed only if sufficient balance exists)
◦ CalculateInterest() - calculates and returns interest using formula:
Interest = (Amount * ROI) / 100
• Create multiple objects and demonstrate all methods."""

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = float(Amount)

    def Display(self):
        print("Account holder name: ",self.Name)
        print("Current balance: ",self.Amount)

    def Deposit(self):
        
        DepAmount = float(input("Enter deposite amount:  "))
        self.Amount += DepAmount
        print(f"Deposited amount is:{DepAmount} and Current balance is: {self.Amount}")

    
    def Withdraw(self):
        
            WitAmount = float(input("Enter withdraw amount: "))
            if WitAmount > self.Amount:
                print("You do not have sufficent balance.")
            else:
                self.Amount -= WitAmount
                print(f"Withdraw amount is:{WitAmount} and Current balance is: {self.Amount}")
        
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI)/100
        return Interest

bobj = BankAccount("Mangesh Thak",5000.0)
bobj.Display()
bobj.Deposit()
bobj.Withdraw()
print("Calculated interest: ",bobj.CalculateInterest())