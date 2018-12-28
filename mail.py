import smtplib

try:  
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    
except:  
    print('Something went wrong...')
server.login('singhankit240794@gmail.com', 'raghuveersingh')
body="This is the test code which is written in python just to test mail is working or not  with the help of python"
server.sendmail('singhankit240794@gmail.com','anujrajvansh7.ar@gmail.com',body)
server.quit()