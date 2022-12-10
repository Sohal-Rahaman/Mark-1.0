from Body.listen import Listen
from Body.speak import speak


def MainExe():
    while True:
        
        query = Listen()
        
        if "hello" in query:
            speak("hello! i am MARK!")
        elif "bye" in query :
              speak("Have a good day!")

