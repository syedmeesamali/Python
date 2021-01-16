import pyttsx3                          #pip install pyttsx3
import datetime
import speech_recognition as sr         #pip install speechRecognition



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

def greetme():
    speak("Hello Sir Ali how are you doing?")
    time_()
    date_()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("Nice robot at your service. What can i do for you today?")

greetme()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please.....")
