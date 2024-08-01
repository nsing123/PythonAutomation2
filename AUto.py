import smtplib as s
print("Hi")
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('neelpythonpython@gmail.com','akke umkx uhyr qvja')

subject="test python 2 mail"
body="Just a test file"

msg="subject:{}\n\n{}".format(subject,body)
list_add=['neelpythonpython@gmail.com']
ob.sendmail('neelpythonpython@gmail.com',list_add,msg)
print("send mail")
ob.quit()