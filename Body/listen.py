import speech_recognition as sr
from googletrans import Translator

def Listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source :
        print("Listning...")
        r.pause_threshold=1
        audio= r.listen(source,0,8) 
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="hi")
    except:
        return ""
    
    query=str(query).lower()
    return query
Listen()          
#print(Listen())      

#translator<----------------------------------------->>>
def TranslationHinToEng(Text):
    line=str(Text)
    translate=Translator()
    result=translate.translate(line)
    data=result.text
    print(f"you : {data}.")
    return data

#connect------------------------------------------->>>
def MicExecution():
    query=Listen()
    data=TranslationHinToEng(query)
    return data
#MicExecution()

import pyttsx3

def speak(Text):
    engine = pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    #print("")
    print(f"you : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()


