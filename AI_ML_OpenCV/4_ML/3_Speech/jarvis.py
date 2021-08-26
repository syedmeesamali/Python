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

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("The current date is: ")
    speak("Year " + str(year))
    speak("Month" + str(month))
    speak("Day" + str(day))

def greetme():
    speak("Hello Sir how are you doing?")
    #time_()
    #date_()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir")
    else:
        speak("Good night to you. ")
    speak("I am a female robot at your service. What can i do for you today?")


#Run the greetme function
#greetme()

#pip install pipwin
#pipwin install pyaudio

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
        return "None"
    return query

if __name__ == "__main__":
    greetme()
    while True:
        query = TakeCommand().lower()       #Store all commands in lower letters
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'bye' in query:
            speak("Bye sir. Take care. ")
            break