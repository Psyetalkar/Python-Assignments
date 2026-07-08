import Assignment17_1_1

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    print("Addition :", Assignment17_1_1.Add(value1, value2))
    print("Subtraction :", Assignment17_1_1.Sub(value1, value2))
    print("Multiplication :", Assignment17_1_1.Mult(value1, value2))
    print("Division :", Assignment17_1_1.Div(value1, value2))

if __name__ == "__main__":
    main()