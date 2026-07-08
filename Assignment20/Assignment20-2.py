import threading

def EvenFactor(no):

    Sum = 0

    print("Even Factors :")

    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i)
            Sum = Sum + i

    print("Sum of Even Factors :", Sum)


def OddFactor(no):

    Sum = 0

    print("Odd Factors :")

    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i)
            Sum = Sum + i

    print("Sum of Odd Factors :", Sum)


def main():

    value = int(input("Enter number : "))

    T1 = threading.Thread(target=EvenFactor, args=(value,), name="EvenFactor")
    T2 = threading.Thread(target=OddFactor, args=(value,), name="OddFactor")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()