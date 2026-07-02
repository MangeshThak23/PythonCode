#7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

LenghtString = lambda St : len(St) > 5

def main():
    Mylist = []
    Num = int(input("Enter how much strings do you want:"))

    for i in range(Num):
        String1 = input("Enter the string:  ")
        Mylist.append(String1)
    print("The list is: ", Mylist)

    FData = list(filter(LenghtString, Mylist))
    print("The string greater than greater than 5: ",FData)

if __name__ == "__main__":
    main()