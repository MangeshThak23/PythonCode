"""4: Write a program that creates a new log file after every ten minutes."""

import datetime
import time
import os
import schedule
import sys

def Display(DirectoryPath):

    print("Automation started.")

    timestamp = time.ctime()

    TextFile = "Marvellous%s.log"%(timestamp)
    TextFile = TextFile.replace(":","_")
    TextFile = TextFile.replace(" ","_")


    fobj = open(TextFile,"w")
    fobj.write(f"Log file created successfully.\n Creation time: {TextFile}")

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")
    
    print(f"Log File is created with name: {TextFile}")
    fobj.close

def main():
    try:
        if(len(sys.argv) == 2):
            if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
                print("This automation script is used to travel the directory")
                print("For better usage, please check --u flag")

            elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
                print("This automation script is used to travel the directory")
                print("Kindly enter the argument post the .py file while running the program")

            else:

                
                schedule.every(10).minutes.do(Display,sys.argv[1])
                while True:
                    schedule.run_pending()
                    time.sleep(1)

    except Exception as ex:
        print("Exception is: ",ex) 

if __name__ == "__main__":
    main()   

        