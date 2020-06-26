import pyttsx3

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


if __name__ == '__main__':
    if 1:
        wishMom()