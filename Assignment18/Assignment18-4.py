def Frequency(arr, no):
    count = 0

    for i in arr:
        if i == no:
            count = count + 1

    return count


def main():
    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    search = int(input("Enter element to search : "))

    result = Frequency(data, search)

    print("Frequency is :", result)


if __name__ == "__main__":
    main()