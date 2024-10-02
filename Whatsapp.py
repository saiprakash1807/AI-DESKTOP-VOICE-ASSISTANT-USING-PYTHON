import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init('sapi5') #sapi5 is a MS API for voice recognition 
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait() 

def takeInput():#take user input and returns string o/p
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)


    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User: {query}\n")

    except Exception as e:
        # print(e)
        print("Please say that again")
        return "None"
    return query

str_time = int(datetime.now().strftime("%H"))
update  = int((datetime.now()+timedelta(minutes=1)).strftime("%M"))

def sendMessage():
    message  = str(input("enter the message: "))
    pywhatkit.sendwhatmsg("+918660551441",message,time_hour=str_time,time_min=update)

    