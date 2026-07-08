import threading

def Maximum(Data):
    print("Maximum element :", max(Data))


def Minimum(Data):
    print("Minimum element :", min(Data))


def main():

    size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")

    for i in range(size):
        Data.append(int(input()))

    T1 = threading.Thread(target=Maximum, args=(Data,))
    T2 = threading.Thread(target=Minimum, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()