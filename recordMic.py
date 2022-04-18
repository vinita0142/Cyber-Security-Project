#libraries
import socket
import platform
import time 
import os
from scipy.io.wavfile import write
import sounddevice as sd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
audio_information="audio.wav"
michrophone_time=10

def microphone():
    fs=44100
    seconds=michrophone_time

    myrecording = sd.rec(int(seconds*fs),samplerate=fs,channels=2)
    sd.wait()
    write(audio_information, fs, myrecording)
 
microphone()
print("Audio file created successfully")
fromaddr = "vinitavaswani24@gmail.com"
toaddr = "vinitavaswani24@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Mic audio recording"

body = "Audio file"

msg.attach(MIMEText(body, 'plain'))

filename = "audio.wav"
attachment = open("C:\\Users\\Vinita Vaswani\\Desktop\\csPro\\audio.wav", "rb")
print("attachment added")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Enter your app password here")
print("login successful")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("Mail send successfully")
server.quit()