"""5: Write a program that deletes all empty files from a specified
directory every hour.
The program should:
• Scan the directory recursively
• Detect files whose size is zero bytes
• Delete the empty files
• Store deleted file paths in a log file
• Handle permission errors
Test the program only on a sample directory."""

import schedule
import sys
import os
import time
import datetime

def DirectoryScanner(DirectoryPath):

    LogFileName = "DirectoryScanner_Delete_Log.txt"

    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print(f"{DirectoryPath} is not available on location, kindly select correct directory\n")
        return

    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print(f"Automation Error: it is not directory with name ",DirectoryPath)
        return

    print("Log file gets created with name: ",LogFileName)

    fobj = open(LogFileName,"a")
    fobj.write(f"\nBelow are the log details generated at:{datetime.datetime.now()}\n")

    TotalFiles = 0
    EmptyFiles = 0

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            TotalFiles += 1
            FilePath = os.path.join(FolderName,fname)
            
            try:
                FileSize= os.path.getsize(FilePath)
                if(FileSize == 0):
                    os.remove(FilePath)    
                    EmptyFiles += 1
                    fobj.write(f"Deleted file: {FilePath}\n")
                else:
                    fobj.write(f"Skipped ({FileSize} bytes): {FilePath}\n")
                    
            except PermissionError as pe:
                print(f"You do not have permission to delete the file: {pe}\n")
                fobj.write(f"Permission denied: {FilePath}\n")
            except FileNotFoundError:
                pass
            except Exception as e:
                print(f"Unexpected error with '{FilePath}': {e}\n")

    fobj.write(f"total files scanned: {TotalFiles} \n")
    fobj.write(f"total empty files found and deleted: {EmptyFiles} \n")
    fobj.write(f"Log file is created at:{datetime.datetime.now()}\n")
    print(f"Scan completed. Total files: {TotalFiles} | Empty files deleted: {EmptyFiles}\n")
    print("Automation started.")

    fobj.close()

def main():

    if(len(sys.argv) == 2):
        

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H" ):
            print("For usage help kindly use argument as --u or --U")
            

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U" ):
            print("Please enter the directory name in argument first")

        else:
            DirectoryScanner(sys.argv[1])
            schedule.every(1).hours.do(DirectoryScanner,sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid arguments.")
        sys.exit(0)

if __name__ == "__main__":
    main()    