# !/usr/bin/python3

import sys
import os
import pathlib
import shutil
import smtplib
from datetime import datetime
from backupcfg import jobs, dstPath, logPath, smtp

# writes a message to a log file.
def logging(message, dateTimeStamp):
    try:
        file = open(logPath, "a")
        file.write(f"{message} {dateTimeStamp}\n")
        file.close()
    
    except FileNotFoundError:
        print("ERROR: File does not exit.")
    except IOError:
        print("ERROR: File is not accessible.")
        
# prints an error message to the console, logs the error message, and sends
def error(errorMessage, dateTimeStamp):
    print(errorMessage)
    logging (errorMessage, dateTimeStamp)
    sendEmail(errorMessage, dateTimeStamp)


    #email error message to administrator
def sendEmail(message, dateTimeStamp):
    
    """
Send an email message to the specified recipient.
Parameters:
message (string): message to send.
dateTimeStamp (string): Date and time when program was run.
"""
    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")
#print("ERROR: Send email failed: " + str(e), file=sys.stderr)


    
def main():
        dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        argCount = len(sys.argv)
        if argCount != 2:
            error("FAILEAR: jobname missing from commend line", dateTimeStamp)
        else:
            jobName = sys.argv[1] #nmhbjnnm
            if jobName not in jobs:
                error(f"FAILEAR; jobname {jobName} not defined.", dateTimeStamp)
            else:
                srcPath = jobs[jobName]
                if not os.path.exists(srcPath):
                    error(f"FAILEAR: source path {srcPath} does not exit.", dateTimeStamp)
                else:
                    if not os.path.exists(dstPath):
                        print(f"FAILEAR: Destination path {dstPath} does not exit.", dateTimeStamp)
                    else:
                        
                        srcDetails = pathlib.PurePath(srcPath)
                        dstLoc = f"{dstPath}/{srcDetails.name}-{dateTimeStamp}"
                        
                        if pathlib.Path(srcPath).is_dir():
                            shutil.copytree(srcPath, dstLoc)
                        else:
                            shutil.copy2(srcPath, dstLoc)
                            
                        #Write success to log file
            
                    
if __name__ == "__main__":
    main()               
