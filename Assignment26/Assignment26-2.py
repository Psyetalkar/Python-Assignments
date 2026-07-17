class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        self.Radius = float(input("Enter Radius of Circle : "))

    def CalculateArea(self):
        self.Area = self.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print("Radius of circle is : ",self.Radius)
        print("Area of circle is : ",self.Area)
        print("circumference of circle is : ",self.Circumference)

obj1 = Circle()
obj1.Accept()
print("------ Object 1 ------")
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2 = Circle()
obj2.Accept()
print("------ Object 2 ------")
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
