def Maximum(arr):
    max_no = arr[0]

    for i in arr:
        if i > max_no:
            max_no = i

    return max_no


def main():
    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    result = Maximum(data)

    print("Maximum number is :", result)


if __name__ == "__main__":
    main()