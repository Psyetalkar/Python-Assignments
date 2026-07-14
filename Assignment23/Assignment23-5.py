import multiprocessing
import math

def Factorial(no):

    Fact = math.factorial(no)

    print("Process ID :", multiprocessing.current_process().pid)
    print("Input Number :", no)
    print("Factorial :", Fact)
    print()

    return Fact


def main():

    Data = [10, 15, 20, 25]

    p = multiprocessing.Pool()

    p.map(Factorial, Data)

    p.close()
    p.join()


if __name__ == "__main__":
    main()