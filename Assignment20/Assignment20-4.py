import threading

def Small(Str):

    Count = 0

    for ch in Str:
        if ch.islower():
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Lowercase letters :", Count)


def Capital(Str):

    Count = 0

    for ch in Str:
        if ch.isupper():
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Uppercase letters :", Count)


def Digits(Str):

    Count = 0

    for ch in Str:
        if ch.isdigit():
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", Count)


def main():

    value = input("Enter string : ")

    T1 = threading.Thread(target=Small, args=(value,), name="Small")
    T2 = threading.Thread(target=Capital, args=(value,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(value,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()