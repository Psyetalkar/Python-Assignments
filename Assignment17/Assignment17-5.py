def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True

def main():
    value = int(input("Enter number : "))

    result = ChkPrime(value)

    if result == True:
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__ == "__main__":
    main()