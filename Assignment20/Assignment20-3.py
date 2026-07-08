import threading

def EvenList(Data):

    Sum = 0

    print("Even Elements :")

    for i in Data:
        if i % 2 == 0:
            print(i)
            Sum = Sum + i

    print("Sum of Even Elements :", Sum)


def OddList(Data):

    Sum = 0

    print("Odd Elements :")

    for i in Data:
        if i % 2 != 0:
            print(i)
            Sum = Sum + i

    print("Sum of Odd Elements :", Sum)


def main():

    size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")

    for i in range(size):
        Data.append(int(input()))

    T1 = threading.Thread(target=EvenList, args=(Data,))
    T2 = threading.Thread(target=OddList, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()