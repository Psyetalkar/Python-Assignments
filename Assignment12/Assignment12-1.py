


def EvenOdd():

    char= input("Enter a character : ")

    vowels=["A","a","E","e","I","i","O","o","U","u"]    
    for i in vowels:
        if char == i :
            return True   
       
    
       
def main():

    Ret=EvenOdd()
    if (Ret==True):
        print("Vowel")

    else:
        print("Consonent")


if __name__ == "__main__":
    main()
 
    