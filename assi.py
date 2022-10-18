import pyttsx3       #text to speech
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')       #initialising engine 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour<=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("Good afternoon")

    else:
        speak("good evening")

    speak(" hi I am your assistant  how can i help you?")

#takes command from thr user and returns string op
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening,kindly speak..... ")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognising....")
        query = r.recognize_google(audio, language ='en-in')
        print(f'user said :{query}\n')    

    except Exception as e:
        print(e,"Say that again please...")
        return "none"

    return query


if __name__== "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching in wikipedia..")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 2)
            speak("accordind to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")    

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")


        elif "open python " in query:
            codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe"
            os.startfile(codepath)
     
        elif 'play' in query:
            song = query.replace('play', '')
            speak(f"playing {song}")
            pywhatkit.playonyt(song)

        elif "joke" in query:
            speak(pyjokes.get_jokes())
            break()

            
