import os
import time
import subprocess
from mailer import generateHtml, myServers


a = raw_input("want to rescan and send on email instead ? (y/n) : ")
# myServers is a list defined in my_config.py file with the IP addresses of the servers
if a == 'n':
    print("{} choosed, Printing on terminal instead").format(a)
    print("===================now printing HDD space status=====================================")
    for i in myServers:
        print("Status for %s: ") % i
        os.system("ssh" + " " + i + " df -h")
        print("....................................................................................")
        time.sleep(2)

elif a == 'y':
    # print("Ignore errors like 'df: `/media/SECUPD': Input/output error'")
    generateHtml()
    print("Email sent, Check your inbox(Spam too)")
