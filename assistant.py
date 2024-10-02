import pyttsx3 #text-to-speech conversion library
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5') #sapi5 is a MS API for voice recognition 
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = (datetime.datetime.now().hour)
    if (hour>=0 and hour<=12):
        speak("Good Morning")
    elif (hour>12 and hour<=17):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("How may I help you ?")

def takeInput():#take user input and returns string o/p
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User: {query}\n")

    except Exception as e:
        print("Please say that again")
        return "None"
    return query

if __name__=="__main__": #main function
    wish()
    if 1:
        query = takeInput().lower()
        #logic for executing tasks 
        #1. Searching through Wiki

        if 'wikipedia' in query:
            speak("Searching Wiki...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print (results)
            speak(results)
        
        #2. Opens sites

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")

        #3. play music
        elif 'play music' in query:
            songsdir = 'C:\\Users\\okwar\\Music\\lil peep'
            songs = os.listdir(songsdir)
            print(songs)
            os.startfile(os.path.join(songsdir,songs[1]))

        #4. tell current time
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H %M %S")
            speak(f"The time is {time}")
            print (time)

        #5. open VS Code
        elif 'open vs code' in query:
            path = "C:\\Users\\okwar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        #6. send Whatsapp Message
        elif 'whatsapp' in query:
            from Whatsapp import sendMessage
            sendMessage()

        #7. calculate
        elif 'calculate' in query:
            from CalculateNo import WolfRamAlpha
            from CalculateNo import Calc
            query = query.replace("calculate","")
            Calc(query)
            
        