import pyttsx3
import datetime

engine = pyttsx3.init()         #Main speech engine


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("Hello ali how are you?")

def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")     #24-hour time format
    speak("The current time is: ")
    speak(Time)

#time_()

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("The current date is: ")
    speak("Year " + str(year))
    speak("Month" + str(month))
    speak("Day" + str(day))

date_()