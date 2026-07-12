"""2: Design a Python application that creates two threads.
• Thread 1 should calculate and display the maximum element from an list.
• Thread 2 should calculate and display the minimum element from the same list.
• The list should be accepted from the user."""

import threading

def MaxElement(No1):
    if not No1:
        return
    
    MaxNum = No1[0]
    for i in No1:
        if i>MaxNum:
            MaxNum = i
    print("Max Num.:    ",MaxNum)
    

def MinElement(No1):
    if not No1:
        return
    
    MinNum = No1[0]
    for i in No1:
        if i<MinNum:
            MinNum = i
    print("Min Num: ",MinNum)

def main():
    Mylist = []

    NumElements = int(input("Enter the number of elements:  "))

    for i in range(NumElements):
        Elements = int(input("Enter the elements:   "))
        Mylist.append(Elements)

    print("The entered list is: ",Mylist)

    t1 = threading.Thread(target=MaxElement,args=(Mylist,))
    t2 = threading.Thread(target=MinElement,args=(Mylist,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()