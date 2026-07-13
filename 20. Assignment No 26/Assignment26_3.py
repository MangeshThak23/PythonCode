"""3: Write a Python program to implement a class named Arithmetic with the following
characteristics:
• The class should contain two instance variables: Value1 and Value2.
• Define a constructor (__init__) that initializes all instance variables to 0.
• Implement the following instance methods:
◦ Accept() – accepts values for Value1 and Value2 from the user.
◦ Addition() – returns the addition of Value1 and Value2.
◦ Subtraction() – returns the subtraction of Value1 and Value2.
◦ Multiplication() – returns the multiplication of Value1 and Value2.
◦ Division() – returns the division of Value1 and Value2 (handle division by zero
properly).

• Create multiple objects of the Arithmetic class and invoke all the instance methods."""

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter value1:  "))
        self.Value2 = int(input("Enter value2:  "))

    def Addition(self):
        self.Ans = self.Value1 + self.Value2
        return self.Ans

    def Substrtaction(self):
        self.Ans = self.Value1 - self.Value2
        return self.Ans

    def Multiplication(self):
        self.Ans = self.Value1 * self.Value2
        return self.Ans
        
    def Division(self):
        try:
            self.Ans = self.Value1 / self.Value2
        except Exception as ex:
            print("Exception: ",ex)
        return self.Ans
           
        
obj1 = Arithmetic()

obj1.Accept()

print("Addition is: ",obj1.Addition())
print("Substraction is: ",obj1.Substrtaction())
print("Multiplication is: ",obj1.Multiplication())
print("Division is: ",obj1.Division())