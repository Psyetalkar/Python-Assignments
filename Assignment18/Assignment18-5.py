import Assignment18_5_1


def ListPrime(arr):

    sum = 0

    for i in arr:
        if Assignment18_5_1.ChkPrime(i):
            sum = sum + i

    return sum


def main():

    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    result = ListPrime(data)

    print("Addition of prime numbers is :", result)


if __name__ == "__main__":
    main()