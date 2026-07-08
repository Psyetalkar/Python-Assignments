def SumList(arr):
    total = 0

    for i in arr:
        total = total + i

    return total


def main():
    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    result = SumList(data)

    print("Addition is :", result)


if __name__ == "__main__":
    main()