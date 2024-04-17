# !/usr/bin/python3

import sys
import os
import pathlib
import shutil
from datetime import datetime
from backupcfg import jobs, dstPath

def main():
        dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        argCount = len(sys.argv)
        if argCount != 2:
            print("ERROR: jobname missing from commend line")
        else:
            jobName = sys.argv[1] #nmhbjnnm
            if jobName not in jobs:
                print(f"ERROR; jobname {jobName} not defined.")
            else:
                srcPath = jobs[jobName]
                if not os.path.exists(srcPath):
                    print(f"ERROR: source path {srcPath} does not exit.")
                else:
                    if not os.path.exists(dstPath):
                        print(f"ERROR: Destination path {dstPath} does not exit.")
                    else:
                        
                        srcDetails = pathlib.PurePath(srcPath)
                        
                        dstLoc = dstPath + "/" + srcDetails.name + "-" + dateTimeStamp
                        
                        if pathlib.Path(srcPath).is_dir():
                            shutil.copytree(srcPath, dstLoc)
                        else:
                            shutil.copy2(srcPath, dstLoc)
            
                    
if __name__ == "__main__":
    main()               
