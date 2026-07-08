def main():
    Mult = lambda no1, no2: no1 * no2

    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    print("Output :", Mult(value1, value2))

if __name__ == "__main__":
    main()