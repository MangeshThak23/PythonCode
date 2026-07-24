"""3: Write a program that scans a specified directory every minute.
The task should display:
• Directory name
• Number of files
• Number of subdirectories
• Date and time of scanning
Use the os module."""

import os
import time
import schedule
import datetime

def DirectoryScanner(DirectoryPath):
    if not os.path.exists(DirectoryPath):
        print("Directory not exists")
        return

    fcount = 0
    sfcount = 0
    
    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        fcount += len(FileName)
        sfcount += len(SubFolder)

    ScanTime = datetime.datetime.now()

    print("Directory Name: ",os.path.abspath(DirectoryPath))
    print("Number of files: ",fcount)
    print("Number of subdirectory: ",sfcount)
    print("Date and time of scanning: ",ScanTime)

def main():

    try:

        dirPath = input("Enter dir path: ")
        schedule.every(1).minute.do(DirectoryScanner,DirectoryPath=dirPath)
        DirectoryScanner(dirPath)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as ex:
        print("Error occured:",ex)

if __name__ == "__main__":
    main()
    


    
        