def Minimum(arr):
    min_no = arr[0]

    for i in arr:
        if i < min_no:
            min_no = i

    return min_no


def main():
    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    result = Minimum(data)

    print("Minimum number is :", result)


if __name__ == "__main__":
    main()