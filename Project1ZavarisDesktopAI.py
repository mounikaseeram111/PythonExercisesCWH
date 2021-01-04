import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12 :
        speak('Good morning!!')
    elif hour<=12 and hour<18:
        speak('Good Afternoon!!')
    else :
        speak('Good evening!!')
    speak("I am zavaris , Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing.....')
        query = r.recognize_google(audio,language='en-in')
        print(F'User said: {query}\n')

    except Exception as e:
        print(e)
        print('Say that again Please...')
        return 'NONE'
    return query

def sendEmail(content,to):
    server = smtp.SHTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('you-email','your-password')
    server.sendmail('your-email',to,content)
    server.close()




if __name__ == "__main__":
    speak("Hare Krishna Hare Krishna, Krishna Krishna Hare Hare, Hare Rama Hare Rama, Rama Rama Hare")
    wishMe()
    while True :
        query = takeCommand().lower()
        if 'wikipedia' in query :
            speak('Searching Wikipedia')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results) 
            speak(results)

        elif 'open google' in query :
            webbrowser.open('google.com')
        
        elif 'open youtube' in query :
            webbrowser.open('youtube.com')

        elif 'open stack overflow' in query :
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query :
            musicDir = "D:\\MyMusic\\FavSongs"
            songs = os.listdir(musicDir)
            print(songs)
            os.startfile(os.path.join(musicDir,songs[0]))
        elif 'the time' in query:
            starTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Maam the time is {starTime}')

        elif 'open code' in query:
            codePath = "C:\\Users\\se20020039\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'mounikaseeram111@gmail.com'
                sendEmail(content,to)
                speak('Email has been sent Successfully!')
            except Exception as e:
                print(e)
                speak('Sorry my dear firend! I am unable to send your email')
        elif 'quit':
            exit()