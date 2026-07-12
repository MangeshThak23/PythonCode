"""4: Design a Python application that creates three threads named Small, Capital, and
Digits.
• All threads should accept a string as input.
• The Small thread should count and display the number of lowercase characters.
• The Capital thread should count and display the number of uppercase characters.
• The Digits thread should count and display the number of numeric digits.
• Each thread must also display:
◦ Thread ID
◦ Thread Name"""

import threading

def Small(small):
    tid = threading.get_ident()
    tname = threading.current_thread().name

    Sum = 0
    for char in small:
        if char.islower():
            Sum += 1
    print(f"The thread id is: {tid} and thread name is: {tname}")
    print("The number of lowercase characters are:  ",Sum)

def Capital(cap):
    tid = threading.get_ident()
    tname = threading.current_thread().name

    Sum = 0 
    for char in cap:
        if char.isupper():
            Sum += 1
    print(f"The thread id is: {tid} and thread name is: {tname}")
    print("The number of uppercase characters are:  ",Sum)

def Digits(dig):
    tid = threading.get_ident()
    tname = threading.current_thread().name

    Sum = 0
    for num in dig:
        if num.isdigit():
            Sum += 1
    print(f"The thread id is: {tid} and thread name is: {tname}")
    print("The numbers:  ",Sum)    

def main():
    
    Data = "Python Programming Assignment 20 Question 4"

    t1 = threading.Thread(target=Small,args=(Data,))
    t2 = threading.Thread(target=Capital,args=(Data,))
    t3 = threading.Thread(target=Digits,args=(Data,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    tid = threading.get_ident()
    tname = threading.current_thread().name
    print(f"The thread id is: {tid} and thread name is: {tname}")

    print("Exit from main")

if __name__ == "__main__":
    main()



