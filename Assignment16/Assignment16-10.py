def DisplayLength(name):
    return len(name)


def main():
    value = input("Enter name: ")

    result = DisplayLength(value)
    print("Length is:", result)


if __name__ == "__main__":
    main()