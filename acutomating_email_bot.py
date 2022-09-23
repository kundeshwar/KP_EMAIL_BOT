from email import message
from email.message import EmailMessage
import smtplib
import speech_recognition as sr
import pyaudio as py
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):#this is used to speak asking question
    engine.say(text)
    engine.runAndWait()


def get_info():#this is converting your voice to text 
    try:
        with sr.Microphone() as source:
            print("listenig")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        print("please speak in loud voice")


def sending(reciver, subject, message):#this is used to sending mail auto maticaly 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('kundeshwar15000@gmail.com', "Kundeshwar15@")
    email = EmailMessage()
    email["From"]= 'kundeshwar15000@gmail.com'
    email['To']= reciver
    email['Subject']= subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    "kundeshwar" : "kundeshwar15000@gmail.com",
    "adresh": "adresh@gmail.com"
}

def get_emsil_info():#this one asq you question 
    talk("to whom you want to send email")
    name = get_info()
    reciver = email_list[name]
    print(reciver)
    talk("what is the subject of your email?")
    subject = get_info()
    talk("tell me the text in your email")
    message = get_info()
    talk("thanks ")

    sending(reciver, subject, message)
    talk("HEY lazy ass. Your email is sended")
    talk("do you want to sent more email")
    sending = get_info()
    if "yes" in sending:
        get_emsil_info()
    else:
        print("thanks, good by. take care")



get_emsil_info()