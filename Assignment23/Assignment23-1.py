import multiprocessing

def SumEven(no):

    Sum = 0

    for i in range(2, no + 1, 2):
        Sum = Sum + i

    print("Process ID :", multiprocessing.current_process().pid)
    print("Input Number :", no)
    print("Sum of Even Numbers :", Sum)
    print()

     


def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    p.map(SumEven, Data)

    p.close()
    p.join()


if __name__ == "__main__":
    main()