import pyttsx3

import datetime

import speech_recognition as sr

import wikipedia

import webbrowser

import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMom():
    speak('Happy mothers day mom! love you ')
    speak('roses are red,sky is blue,my dear mother,i love you!')
    speak('thanks for everything you have given to me')
    print('Happy mothers day mom! love you')
    print('roses are red,sky is blue,my dear mother,i love you!')
    print('thanks for everything you have given to me')



def wishMe():
    speak('How may i help you,sir')

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
            print('listening...')
            r.pause_threshold = 1
            audio =r.listen(source)
    try:
        print('recognizing...')
        query=r.recognize_google(audio,language='en-us')
        print(f'user said:{query}\n')
    except Exception as e:
        print(e)
        pass
        return "None"
    return query

if __name__ == '__main__':

    while True:
        query=takeCommand().lower()
        # logic
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query ,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube')
            break

        elif'what can you do'in query:
            speak("i can open google,youtue,search wikipedia and open certain apps on Your pc")


        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening google')
            break

        elif"what I did for mum" in query:
            speak("you have made this program and you have made a card for mother's day")
            speak('i am sure mom will be happy with this')


        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'sir,The time is {strTime}')


        elif 'how are you'in query:
            speak("i am fine sir,thanks")


        elif 'who are you'in query:
            speak("I am Harry,a PDAI or Python developed artificial intelligence made by the master  programmer yovi")


        elif 'open code'in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak('opening code')
            break

        elif 'open whatsapp'in query:
            whatPath="C:\\Users\\NITJ\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatPath)
            speak ('opening whatsapp')
            break

        elif 'open office'in query:
            oPath='"C:\\Program Files (x86)\\OpenOffice 4\\program\\soffice.exe"'
            os.startfile(oPath)
            speak("opening office")
            break

        elif 'open zoom'in query:
            tPath="C:\\Users\\NITJ\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(tPath)
            speak('opening zoom')
            break
        elif'open chrome'in query:
            cPath='C:\\Users\\NITJ\\AppData\\Local\\chromium\\Application\\chrome.exe'
            os.startfile(cPath)
            speak('opening Chromium')
            break

        elif 'wish mum'in query:
            wishMom()


        elif 'are you a friend'in query:
            speak("yes,i am trying to be and i want to make many friends")


        elif 'love you'in query:
            speak('love you too')


        elif 'hi'in query:
            speak("hello sir")
            wishMe()


        elif 'apologize'in query:
            speak("sorry sir")


        elif 'thanks'in query:
            speak("Your welcome")


        elif'very good' in query:
            speak("thank you,sir")


        elif 'are you there'in query:
            speak("yes i am here")

        elif 'it is a special day'in query:
            speak("congratulations ,sir")


        elif 'close' in query:
            speak('you can access me just by running the program')
            speak("thanks for making me")
            speak("bye,sir")
            speak("good night")
            break