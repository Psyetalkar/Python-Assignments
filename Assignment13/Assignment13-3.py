
def factors(No):
    val=[]
    for i in range(1,No+1):
        if (No%i==0):

          val.append(i)

    return val



def main():
    No = int(input("Enter a number : "))
    sum =0
    Ret=factors(No)

    for i in Ret[:-1]:
         sum = sum + i

    if (sum==No):
        print("perfect number")

if __name__ == "__main__":
    main()