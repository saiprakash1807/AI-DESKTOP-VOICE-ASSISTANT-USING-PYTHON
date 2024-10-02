import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init('sapi5') #sapi5 is a MS API for voice recognition 
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "H6Q49R-AE6WJQ4U38"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try :
        answer = next(requested.results).text
        return answer
    except:
        speak("cannot calculate the values")

def Calc(query):
    Term = str(query)
    Term = Term.replace("into","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("by","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)
    except:
        speak("cannot calculate the values")






