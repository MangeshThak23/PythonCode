"""4: Write a program that copies all .txt files from one directory to
another every ten minutes."""

import sys
import schedule
import os
import shutil
import time
import datetime

def CopyFile(SDir,DDir):

    if not os.path.exists(SDir) or not os.path.isdir(SDir):
        print("The source directory is does not exists")
        return
    
    if not os.path.exists(DDir):
        os.makedirs(DDir)

    Count = 0

    TimeStamp = datetime.datetime.now()
    LogFileName = "LogFile_%s.txt"%(TimeStamp)
    LogFileName = LogFileName.replace(":","_")
    LogFileName = LogFileName.replace(" ","_")

    fobj = open(LogFileName,"w")
    fobj.write("The copied files are:  \n")
    

    for FolderName,SubFolder,FileName in os.walk(SDir):
        for fname in FileName:
            if fname.endswith(".txt"):
                source_file_path = os.path.join(FolderName,fname)
                dest_file_path = os.path.join(DDir,fname)
                

                
                try:
                    shutil.copy(source_file_path,dest_file_path)
                    fobj.write(fname+"\n")
                    Count += 1
                except Exception as ex:
                    print("Failed to copy")
    fobj.close()
    print("File has been copied and pasted in the destination folder")

def main():

    if len(sys.argv) != 3:
        print("Invalid arguments.")
        sys.exit(0)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    CopyFile(SDir=source_dir, DDir=dest_dir)
    schedule.every(10).minutes.do(CopyFile,SDir=source_dir, DDir=dest_dir)
       
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()