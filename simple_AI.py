import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
print(voices[1].id)
engin.setProperty('voices', voices[1].id)


def speak(audio):
    engin.say(audio)
    engin.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning!')

    elif 12 <= hour < 18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')

    speak("I am a simple AI. How may I help you")


def takeCommand():
    # It take microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said:{query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        speak('Say that again please...')
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")

            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dr = 'D:\\1.space\\song'   # type the directry in which you store song
            song = os.listdir(music_dr)
            print(song)
            os.startfile(os.path.join(music_dr, song[1]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {strtime}")

        elif 'open python' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'email to friend' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "friendemail@email.com"
                sendEmail(to, content)
                speak('Email has been send!')

            except Exception as e:
                print(e)
                speak('Sorry,I am not able to send this email.')

        elif 'bye' in query:
            exit()