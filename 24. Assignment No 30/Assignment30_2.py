"""2: Write a Python program that displays the current date and time
after every one minute."""

import time
import datetime
import schedule

def Display():
    TimeStamp = datetime.datetime.now()
    print("The current date and time is:",TimeStamp)

def main():
   
    schedule.every(1).minute.do(Display)
    while True:
        
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()