from Body.listen import Listen
from Body.speak import speak
from Features.clap import Tester

Tester()

# speak("Welcome Sohal i am MARK 2.0 ")

import speech_recognition as sr
import os
from mark import MainExe
def Listen():

    r = sr.Recognizer()
    
    with sr.Microphone() as source :
        print("Listning...")
        r.pause_threshold=1
        audio= r.listen(source,0,8) 
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en")
    except:
        return ""
    
    query=str(query).lower()
    print(query)

    return query

def WakeupDetected():
    queery =Listen().lower()

    if "Wake up" is queery:
        print("DOne ")
      
        MainExe()
    else:
        pass

while True:
    WakeupDetected()