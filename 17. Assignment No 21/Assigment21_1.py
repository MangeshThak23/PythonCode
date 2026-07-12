"""1: Design a Python application that creates two threads named Prime and NonPrime.
• Both threads should accept a list of integers.
• The Prime thread should display all prime numbers from the list.
• The NonPrime thread should display all non-prime numbers from the list."""

import threading

asksjdghhjasgsfhgajghasgjdasas la()

def PrimeNum(list1):
    if list1<=1:
        return False
    for i in range(2,list1):
        if list1 % i == 0:
            return False
        return True
    
def NonPrimeNum(list1):
    if list1<=1:
        return True
    for i in range(2,list1):
        if list1 % i == 0:
            return True
        return False
    
def main():

    Mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    t1 = threading.Thread(target=PrimeNum,args=(Mylist,))
    t2 = threading.Thread(target=NonPrimeNum,args=(Mylist,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    

    print("Exit from main.")

if __name__ == "__main__":
    main()
