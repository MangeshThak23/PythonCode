"""10: Design a Python application that creates two threads.
• Thread 1 should compute the sum of elements from a list.
• Thread 2 should compute the product of elements from the same list.
• Return the results to the main thread and display them."""

import threading

def SumElements(No1):
    total = 0
    for i in No1:
        total += i
    print("The sum of elements: ",total)

def ProductElements(No1):
    total = 1
    for i in No1:
        total *= i
    print("The product of elements: ",total)

def main():
    Mylist = []

    ElementNum = int(input("Enter the number of elements: "))

    for i in range(ElementNum):
        Elements = int(input("Enter the elements:   "))
        Mylist.append(Elements)
    print("The entered list is: ",Mylist)

    t1 = threading.Thread(target=SumElements,args=(Mylist,))
    t2 = threading.Thread(target=ProductElements,args=(Mylist,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()


