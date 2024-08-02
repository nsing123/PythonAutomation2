import gspread
import DatabaseConnection as db
import pandas as pd
import gspread_dataframe
import smtplib as s
from  email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time

gc=gspread.service_account("/home/neelanshuni.singh@nineleaps.com/Downloads/gsheetautomation-431208-0e2305e2db36.json")
wk=gc.open_by_key("1CoO_O3eBOOgXc9bPtXuTCRxOIfyXSHocir3prX7fCtA")
current_sheet=wk.worksheet("Sheet1")
print(current_sheet.get_values())

print(wk.worksheets())
print(wk.url)
try:
    conn=db.database_connection()
    select_query="""
    select att.attendance_date,cls.class_name,mem.name from fitness.Attendance_details att
join fitness.Classes_details cls on att.class_id=cls.class_id 
join fitness.Members_joined as mem on att.member_id=mem.UUID
where  attendance_date=(select max(attendance_date) from fitness.Attendance_details)
    """
    cur=conn.cursor()
    cur.execute(select_query)
    result=cur.fetchall()
    print(result)
except Exception as e:
    print("error",e)
data=pd.DataFrame(result)
print(data)
current_sheet.clear()
gspread_dataframe.set_with_dataframe(current_sheet,data)
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

filename=wk.url
body=f"""
Here is the latest attendance details.
Please read through attachment : {filename}
"""
msg=MIMEMultipart()
msg['From']=email_from
msg['To']=email_to
msg['subject']=subject

#f=open(filename,'rb')

#attachment_package=MIMEBase('application','octet-stream')
#attachment_package.set_payload(f.read())
#encoders.encode_base64(attachment_package)
#attachment_package.add_header('Content-Disposition','attachment; filename='+filename)

msg.attach(MIMEText(body, 'plain'))
#msg = MIMEText(body ,'html')
#msg.attach(attachment_package)
text=msg.as_string()
def job():
    ob.sendmail(email_from, email_to, text)

schedule.every().day.at("11:47").do(job)
ob.quit()



