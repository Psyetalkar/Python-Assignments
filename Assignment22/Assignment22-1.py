import multiprocessing

def SumSquare(no):

    Sum = 0

    for i in range(1, no + 1):
        Sum = Sum + (i * i)

    return Sum


def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    Result = p.map(SumSquare, Data)

    p.close()
    p.join()

    print(Result)


if __name__ == "__main__":
    main()