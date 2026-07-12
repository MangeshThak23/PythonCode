"""2: Design a Python application that creates two threads named EvenFactor and 
OddFactor.
• Both threads should accept one integer number as a parameter.
• The EvenFactor thread should:
◦ Identify all even factors of the given number.
◦ Calculate and display the sum of even factors.
• The OddFactor thread should:
◦ Identify all odd factors of the given number.
◦ Calculate and display the sum of odd factors.
• After both threads complete execution, the main thread should display the message:
“Exit from main”"""

import threading

def EvenFactor(No):
    Sum = 0
    for i in range(2,No+1,2):
        if No % i == 0:
            print("Even Factors:   ",i)
            Sum = Sum + i
    print("Sum of even factors: ",Sum)

def OddFactor(No):
    Sum = 0
    for i in range(1,No+1,2):
        if No % i == 0:
            print("Odd Factors:     ",i)
            Sum = Sum + i
    print("Sum of odd factors:  ",Sum)

def main():
    t1 = threading.Thread(target=EvenFactor,args=(200,))
    t2 = threading.Thread(target=OddFactor,args=(200,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()





