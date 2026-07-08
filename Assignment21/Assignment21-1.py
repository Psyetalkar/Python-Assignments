import threading

def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def Prime(Data):
    print("Prime Numbers :")

    for i in Data:
        if ChkPrime(i):
            print(i)


def NonPrime(Data):
    print("Non Prime Numbers :")

    for i in Data:
        if not ChkPrime(i):
            print(i)


def main():

    size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")

    for i in range(size):
        Data.append(int(input()))

    T1 = threading.Thread(target=Prime, args=(Data,))
    T2 = threading.Thread(target=NonPrime, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()