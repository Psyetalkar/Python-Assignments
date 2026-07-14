import multiprocessing

def CountOdd(no):

    count = 0

    for i in range(1, no + 1, 2):
        count = count + 1

    print("Process ID :", multiprocessing.current_process().pid)
    print("Input Number :", no)
    print("count of Odd Numbers :", count)
    print()

     


def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    p.map(CountOdd, Data)

    p.close()
    p.join()


if __name__ == "__main__":
    main()