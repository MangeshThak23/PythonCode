"""5:Write a program that accepts a directory name from the user and
counts the number of files inside it every five minutes.Write the result into:
DirectoryCountLog.txt
Each entry should contain:
• Directory path
• Number of files
• Date and time"""

import os
import time
import datetime
import schedule
import sys

def DirectoryScanner(DirectoryPath):
    fcount = 0
    TimeStamp = time.ctime()

    if not os.path.exists(DirectoryPath):
        print("Directory not exists")
        sys.exit(1)

    LogFile = "DirectoryCountLog.txt"
  
    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        
        for fname in FileName:
            fcount += 1
            
            
    fobj = open(LogFile,"a")
    fobj.write(f"\nDirectory Name: {os.path.abspath(DirectoryPath)}\n")
    fobj.write(f"Number of files: {fcount} \n")
    fobj.write(f"Date and time of scanning: {TimeStamp} \n")

    print("\nLog file is created")
    fobj.close()
    

def main():

    DirName = input("Enter directory name:  ")

    schedule.every(1).minute.do(DirectoryScanner,DirectoryPath=DirName)
    DirectoryScanner(DirectoryPath=DirName)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()