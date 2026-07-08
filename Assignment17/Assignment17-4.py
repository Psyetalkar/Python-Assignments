def AddFactors(no):
    sum = 0

    for i in range(1, no):
        if no % i == 0:
            sum = sum + i

    return sum

def main():
    value = int(input("Enter number : "))

    result = AddFactors(value)

    print("Addition of factors is :", result)

if __name__ == "__main__":
    main()