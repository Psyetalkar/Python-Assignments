def Binary(num):
    print("Binary equivalent:", bin(num)[2:])

def main():
    number = int(input("Enter a decimal number: "))
    Binary(number)


if __name__ == "__main__":
    main()