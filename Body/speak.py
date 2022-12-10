import pyttsx3

def speak(Text):
    engine = pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    print("")
    print(f"you : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()


