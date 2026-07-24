"""1: Write a program that creates a new text file every minute.
The filename should contain the current timestamp."""

import schedule
import time
import datetime
import os


def FileCreator():

    TimeStamp = time.ctime()

    LogFileName = "File_%s.txt"%(TimeStamp)
    LogFileName = LogFileName.replace(":","_")
    LogFileName = LogFileName.replace(" ","_")

    fobj = open(LogFileName,"w")
    fobj.write(f"File name is: {LogFileName}\n")
    fobj.write(f"Creation date: {TimeStamp} \n")
    fobj.write(f"Creation time: {datetime.datetime.now()}\n")

    print("Log file created.")
    
    fobj.close()

def main():
    print("Automation started.")
    schedule.every(1).minute.do(FileCreator)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()