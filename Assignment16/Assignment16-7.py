def ChkNum(no):
    if no % 5 == 0:
        return True
    else:
        return False


def main():
    value = int(input("Enter number: "))

    result = ChkNum(value)
    print(result)


if __name__ == "__main__":
    main()