"""3: Write a program that reads and displays the contents of a specified 
text file every minute."""

import sys
import time
import datetime
import os
import schedule

def DisplayContent(fname):

    if not os.path.exists(fname):
        print("file does not exist in directory")
        return
        
    if os.path.getsize(fname)==0:
        print("The file is empty.")
        return
    try:    
        print("File have below content:\n")
        fobj = open(fname,"r")
        content = fobj.read()
        print(content)
        fobj.close()
        
    except PermissionError as pe:
        print("Access denied")
        return
    except Exception as ex:
        print("File cannot opened")
        return
def main():

   if(len(sys.argv) == 2 ):
        
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage, please check --u flag")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")    
                
        else:
            
            schedule.every(1).minute.do(DisplayContent,sys.argv[1])
            #DisplayContent(sys.argv[1])   
            while True:
                schedule.run_pending()
                time.sleep(1)
   
if __name__ == "__main__":
    main()  

