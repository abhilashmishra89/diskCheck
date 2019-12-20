import os
from my_config import fromEmail, toEmail, smtp_id, smtp_password, myServers
import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def generateHtml():

    os.system("> /tmp/disk_check.html")
    os.system("echo '<html>'>> /tmp/disk_check.html")
    os.system("echo '<pre>'>> /tmp/disk_check.html")
    os.system("echo '<h2> ==== HDD space status ==== </h2> '> /tmp/disk_check.html")
    op1 = 'ssh '
    op2 = ' df -h '
    op3 = '>> /tmp/disk_check.html'
    html_file = '/tmp/disk_check.html'
    a = myServers
    for i in a:
        os.system("echo '<pre>'>> /tmp/disk_check.html")
        message = 'echo "<h3>Below is status of : {0} </h3>" >> {1}'.format(i, html_file)
        os.system(message)
        os.system(op1 + i + op2 + op3)
        os.system(
            "echo '========================================================' >> /tmp/disk_check.html")
        os.system("echo '</pre>'>> /tmp/disk_check.html")
    os.system("echo '</pre>'>> /tmp/disk_check.html")
    os.system("echo '</html>'>> /tmp/disk_check.html")

    report_file = open('/tmp/disk_check.html')
    html = report_file.read()
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Disk Space Utilization Summary"
    msg['From'] = fromEmail
    msg['To'] = ", ".join(toEmail)
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('{0}'.format(smtp_id), '{0}'.format(smtp_password))
    s.sendmail(fromEmail, toEmail, msg.as_string())
    s.quit()
