import os
import time
import subprocess


# class DiskCheck:
#     def __init__(self):
#         pass

#     def makeHtml(self):


# Original Code below

a = raw_input("want to rescan and send on email instead ? (y/n) : ")

if a == 'y':
    print("Ignore errors like 'df: `/media/SECUPD': Input/output error'")
    email = "abhilash@ipsism.co.jp"

    cmd1 = 'sshpass -f /var/lib/jenkins/workspace/access141scripts/password141  ssh -o strictHostKeyChecking=no root@localhost "python /var/lib/jenkins/workspace/access141scripts/disk_check.py" '
    cmd2 = 'sshpass  -f /var/lib/jenkins/workspace/access141scripts/password023 scp -o strictHostKeyChecking=no /var/www/html/disk_check.html /var/lib/jenkins/workspace/access141scripts/disk_check_mailer* root@c023:/home/abhilash/checklists/'
    cmd3 = 'sshpass -f /var/lib/jenkins/workspace/access141scripts/password023  ssh -o strictHostKeyChecking=no root@c023 "/bin/sh /home/abhilash/checklists/disk_check_mailer_custom.sh {0}" '.format(
        email)
    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)
    print("Email sent, Check your inbox(Spam too)")
else:
    print("{} choosed, Printing on terminal instead").format(a)
    a = ['app1', 'db1', 'cs11', 'cs12', 'cs2', 'c011.ameyoj.com', 'cs3', 'db3',
         'cs4', 'db4', 'cs5', 'cs6', 'ncc', 'oa', 'idex', 'rich', 'c030', 'c035']
    print("===================now printing HDD space status=====================================")
    for i in a:
        print("Status for %s: ") % i
        os.system("ssh" + " " + i + " df -h")
        print("....................................................................................")
        time.sleep(2)
