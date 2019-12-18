import os
from my_config import fromEmail, toEmail, smtp_id, smtp_password, myServers
import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def generateHtml():

    os.system("> disk_check.html")
    os.system("echo '<html>'>> disk_check.html")
    os.system("echo '<pre>'>> disk_check.html")
    os.system("echo '<h2> ==== HDD space status ==== </h2> '> disk_check.html")
    op1 = 'ssh '
    op2 = ' df -h '
    op3 = '>> disk_check.html'
    html_file = 'disk_check.html'
    a = ['C016', 'C019', 'C017', 'C015', 'C010', 'C011', 'C028', 'C027',
         'C032', 'C034', 'C037', 'C020', 'C031', 'C021', 'C046', 'C030', 'C035']
    for i in a:
        os.system("echo '<pre>'>> disk_check.html")
        message = 'echo "<h3>Below is status of : {} </h3>" >> {}'.format(
            i, html_file)
        os.system(message)
        os.system(op1 + i + op2 + op3)
        os.system(
            "echo '========================================================' >> disk_check.html")
        os.system("echo '</pre>'>> disk_check.html")
    os.system("echo '</pre>'>> disk_check.html")
    os.system("echo '</html>'>> disk_check.html")

    report_file = open('disk_check.html')
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
