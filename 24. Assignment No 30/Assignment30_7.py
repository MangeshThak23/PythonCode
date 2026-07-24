"""7: Write a Python program that performs a file backup every hour."""

import shutil
import schedule
import datetime
import os
import time
import sys

def FileCopy(SourcePath,DestPath):
    
    Ret1 = os.path.exists(SourcePath)

    Timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    LogFileName = f"Marvellous_{Timestamp}.log"

    if(Ret1 == False):
        print("Marvellous Automation Error : There is no such file with name ",SourcePath)
        return


    Ret2 = os.path.isdir(DestPath)
    if(Ret2 == False):
        print("Marvellous Automation Error : It is not a directory with name ",DestPath)
        return
    dirpath = os.path.join(DestPath)

    fobj1 = open(SourcePath,"r")
    fobj2 = open(LogFileName,"w")
    fobj2.write(fobj1.read())
    fobj1.close()
    fobj2.close()
    shutil.copy(LogFileName, DestPath)
    
    print("Backup completed successfully at ", datetime.datetime.now().strftime("%d_%m_%Y %H_%M_%S"))

def main():
    #FileCopy("Demo.txt","Demo")
    schedule.every(1).hour.do(FileCopy,sys.argv[1],sys.argv[2])
       
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()