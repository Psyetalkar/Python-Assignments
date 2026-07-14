import multiprocessing  
def ChkPrime(no):

    if no <= 1:
        return False

    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return False

    return True


def CountPrime(no):

    Count = 0

    for i in range(2, no + 1):
        if ChkPrime(i):
            Count = Count + 1

    return Count


def main():

    Data = [10000, 20000, 30000, 40000]

    p = multiprocessing.Pool()

    Result = p.map(CountPrime, Data)

    p.close()
    p.join()

    for i in range(len(Data)):
        print("Prime count up to", Data[i], "=", Result[i])


if __name__ == "__main__":
    main()