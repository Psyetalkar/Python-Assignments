import multiprocessing
import math

def Factorial(no):

    pid = multiprocessing.current_process().pid

    fact = math.factorial(no)

    print("Process ID :", pid)
    print("Input Number :", no)
    print("Factorial :", fact)
    print()

    return fact


def main():

    Data = [10, 15, 20, 25]

    p = multiprocessing.Pool()

    p.map(Factorial, Data)

    p.close()
    p.join()


if __name__ == "__main__":
    main()