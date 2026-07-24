#2: Write a Python program that monitors the size of a specified file every 30 seconds.

import os
import schedule
import datetime
import time
import sys

def MonitorFile(FilePath):

    LogFileName = "FileSizeLog.txt"
    get_Size = os.path.getsize(FilePath)
    fobj = open(LogFileName,"a")
    fobj.write(f"File Path: {os.path.abspath(FilePath)}\n")
    fobj.write(f"File size in bytes is: {get_Size}\n")
    fobj.write(f"Date and time: {datetime.datetime.now()}\n")
    print("Log file is created.")
    fobj.close()

def main():
    FileName1 = input("Enter a file name:   ")

    if not os.path.isfile(FileName1):
        print("File does not exist")
        sys.exit(1)

    MonitorFile(FilePath=FileName1)
    schedule.every(30).seconds.do(MonitorFile,FilePath = FileName1)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    
