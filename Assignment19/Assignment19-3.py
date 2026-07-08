from functools import reduce

def main():

    size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")

    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(lambda no: no >= 70 and no <= 90, Data))

    MData = list(map(lambda no: no + 10, FData))

    RData = reduce(lambda x, y: x * y, MData)

    print("Input List :", Data)
    print("List after filter :", FData)
    print("List after map :", MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()