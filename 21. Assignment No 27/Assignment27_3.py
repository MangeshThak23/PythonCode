"""3: Write a Python program to implement a class named Numbers with the following
specifications:
• The class should contain one instance variable:
◦ Value
• Define a constructor (__init__) that accepts a number from the user and initializes Value.
• Implement the following instance methods:
◦ ChkPrime() - returns True if the number is prime, otherwise returns False
◦ ChkPerfect() - returns True if the number is perfect, otherwise returns False
◦ Factors() - displays all factors of the number
◦ SumFactors() - returns the sum of all factors
• Create multiple objects and call all methods."""

class Numbers:

    def __init__(self,Value):
        self.Value = Value
        

    def ChkPrime(self):

        if self.Value <= 1:
            return False
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        return True
    
    def Factors(self):
        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                print("Factors: ",i)

    def ChkPerfect(self):
        if self.Value <= 1:
            return False
        SumD = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                SumD += i
        return SumD == self.Value

    def SumFactors(self):
        SumF = 0
        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                SumF += i
        return SumF     

Num = int(input("Enter a number:    "))
nobj1 = Numbers(Num)
print("Number is prime: ",nobj1.ChkPrime())
nobj1.Factors()
print("Number is perfect: ",nobj1.ChkPerfect())
print("Sum of factors: ", nobj1.SumFactors())

