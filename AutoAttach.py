import smtplib as s
from  email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

print("Hi")
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
email_from='neelpythonpython@gmail.com'
email_to='neelpythonpython@gmail.com'
subject="Python Email"
try:
    ob.login('neelpythonpython@gmail.com','akke umkx uhyr qvja')
except Exception as e:
    print("Something went wrong",e)

body="""
Please read throuh attahment
"""
msg=MIMEMultipart()
msg['From']=email_from
msg['To']=email_to
msg['subject']=subject
filename="/home/neelanshuni.singh@nineleaps.com/Documents/Auto Mail Attach/Sample_suprstore.csv"
f=open(filename,'rb')

attachment_package=MIMEBase('application','octet-stream')
attachment_package.set_payload(f.read())
encoders.encode_base64(attachment_package)
attachment_package.add_header('Content-Disposition','attachment; filename='+filename)
msg.attach(attachment_package)
text=msg.as_string()
ob.sendmail(email_from,email_to,text)
ob.quit()



