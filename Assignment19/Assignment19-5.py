from functools import reduce

def ChkPrime(no):

    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def main():

    size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")

    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(ChkPrime, Data))

    MData = list(map(lambda no: no * 2, FData))

    RData = reduce(lambda x, y: x if x > y else y, MData)

    print("Input List :", Data)
    print("List after filter :", FData)
    print("List after map :", MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()