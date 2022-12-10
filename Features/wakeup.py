import speech_recognition as sr
import os
def Listen():

    r = sr.Recognizer()
    
    with sr.Microphone() as source :
        print("Listning...")
        r.pause_threshold=1
        audio= r.listen(source,0,8) 
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="hen")
    except:
        return ""
    
    query=str(query).lower()
    print(query)

    return query

def WakeupDetected():
    queery =Listen().lower()

    if "Wake up" is queery:
       pass
    else:
        pass
