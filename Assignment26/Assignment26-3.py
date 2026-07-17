class Arithmatic:

    def __init__(self):
        Value1 = 0
        Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter First value : "))
        self.Value2 = int(input("Enter Second value : "))

    def Addition(self):
        self.Addition = self.Value1 + self.Value2
        return self.Addition

    def Subtraction(self):
        self.Subtraction = self.Value1 - self.Value2
        return self.Subtraction

    def Multiplication(self):
        self.Multiplication = self.Value1 * self.Value2
        return self.Multiplication

    def Division(self):
        self.Division = self.Value1 / self.Value2
        return self.Division
    
print("------ Object 1 ------")
obj1 = Arithmatic()
obj1.Accept()

print("Addition       :", obj1.Addition())
print("Subtraction    :", obj1.Subtraction())
print("Multiplication :", obj1.Multiplication())
print("Division       :", obj1.Division()) 


print("------ Object 2 ------")
obj2 = Arithmatic()
obj2.Accept()

print("Addition       :", obj2.Addition())
print("Subtraction    :", obj2.Subtraction())
print("Multiplication :", obj2.Multiplication())
print("Division       :", obj2.Division())
 



    
    