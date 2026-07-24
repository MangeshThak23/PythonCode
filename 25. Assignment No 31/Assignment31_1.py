"""1: Write a program that accepts:
• A message from the user
• A time interval in seconds
Schedule the program to display the message repeatedly after the specified interval."""

import schedule
import time

def Display(message):
    print(message)

def main():

    try:
        msg = input("Enter a message:   ")
        
        Intervals = int(input("Enter a time interval in seconds:    "))
    
        schedule.every(Intervals).seconds.do(Display,message=msg)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as ex:
        print("Kindly enter correct seconds",ex)

if __name__ == "__main__":
    main()



