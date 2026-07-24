"""5: Schedule a task that executes every five minutes."""

import schedule
import time
import datetime

def Display(FileName):

    CurrentTime = datetime.datetime.now()
    
    fobj = open(FileName,"a")
    fobj.write(f"Task executed at: {CurrentTime}\n")
    
    print("Time printed in text file")
    fobj.close()
   

def main():
    File = "Marvellous.txt"
    schedule.every(5).minute.do(Display,File)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()