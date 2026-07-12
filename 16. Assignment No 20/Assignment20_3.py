"""3: Design a Python application that creates two threads named EvenList and OddList.
• Both threads should accept a list of integers as input.
• The EvenList thread should:
◦ Extract all even elements from the list.
◦ Calculate and display their sum.
• The OddList thread should:
◦ Extract all odd elements from the list.
◦ Calculate and display their sum.
• Threads should run concurrently."""

import threading

def EvenList(List1):
    Sum = 0
    for i in List1:
        if i % 2 == 0:
            print("Even list:   ",i)
            Sum = Sum + i
    print("Sum of Even: ",Sum)

def OddList(List1):
    Sum = 0
    for i in List1:
        if i % 2 != 0:
            print("Odd list:   ",i)
            Sum = Sum + i
    print("Sum of odd:   ",Sum)

def main():
        Mylist = [10,20,12,13,14,33,55,66,88,89,101]

        t1 = threading.Thread(target=EvenList,args=(Mylist,))
        t2 = threading.Thread(target=OddList,args=(Mylist,))

        t1.start()
        t2.start()     
        t2.join()
        t1.join()

        print("Exit from main")

if __name__ == "__main__":
     main()







