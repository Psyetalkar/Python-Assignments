def Add(no1, no2):
    return no1 + no2


def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    result = Add(value1, value2)
    print("Addition is:", result)


if __name__ == "__main__":
    main()