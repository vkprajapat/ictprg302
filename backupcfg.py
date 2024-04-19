jobs = {'job17':'/home/ec2-user/environment/ictprg302/file1.dat',
        'job18':'/home/ec2-user/environment/ictprg302/dirl'}
        
dstPath = '/home/ec2-user/environment/ictprg302/backups'

logPath = '/home/ec2-user/environment/ictprg302/backup.log'

# SMTP settings
smtp = {"sender": "virendra1106pra@gmail.com",    # elasticemail.com verified sender
        "recipient": "30021591@students.sunitafe.edu.au", # elasticemail.com verified recipient
        "server": "smtp.elasticemail.com",      # elasticemail.com SMTP server
        "port": 2525,                           # elasticemail.com SMTP port
        "user": "virendra1106pra@gmail.com",      # elasticemail.com user
        "password": "6A0AF8FC334DF404432C1E5B75"}     # elasticemail.com password
        #message = "There was an error during the backup process."
        #sendEmail(message)
