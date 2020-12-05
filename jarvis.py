import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 165
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def weather(info):
    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+info+'&appid=849c4e086d8bbb9ba88c0cb3494a8c6d')
    return res.json()
def print_weather(result,city):
    speak("{}'s temperature is {}".format(city,result['main']['temp']))
    speak("{}".format(result['weather'][0]['description']))
    speak("{}".format(result['weather'][0]['main']))
def main():
    try:
        info='q=jalpaiguri'
        w_data=weather(info)
        print_weather(w_data,info)
    except:
        speak('sorry Boss city name not found...')
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")

    speak("I am Friday, Please tell me how may i help you?")


def takeCommand():
    """
    it takes microphone input from user and returns string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        r.energy_threshold = 250
        audio = r.listen(source)

    try:
        print("Recognizing...")
        querry = r.recognize_google(audio, language='en-in')
        print(f"Boss, you said {querry}\n")
    except Exception as e:
        print(e)
        print("Say that again...")
        return "none"
    return querry

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('01shadowmaster@gmail.com','password')
    server.sendmail("01shadowmaster@gmail.com",to,content)
    server.close()


if __name__ == '__main__':

    wishMe()
    while True:
        querry = takeCommand().lower()
        x = random.randint(0, 20)
        if 'wikipedia' in querry:
            speak('Searching wikipedia...')
            querry = querry.replace("wikipedia", "")
            results = wikipedia.summary(querry, sentences=2)
            speak(" boss, here is what i found")
            speak(results)

        elif 'what about today' in querry:
            t=main()
            speak(f"boss today''s weather is {t}")


        elif 'open youtube' in querry:
            webbrowser.open("youtube.com")

        elif 'open google' in querry:
            webbrowser.open("google.com")

        elif 'play music' in querry:
            music_dir ='D:\\music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[x]))
            if 'play next' in querry:
                os.startfile(os.path.join(music_dir,songs[x]))
            elif 'stop music' in querry:
                speak(" Yes Boss")
                takeCommand().lower()

        elif 'tell me time' in querry:
            strTime= datetime.datetime.now().strftime("%H:%M")
            speak(f"Boss, time is {strTime}")

        elif 'open pycharm' in querry:
            path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'play movie' in querry:
            movie_file="D:\\movie"
            movie = os.listdir(movie_file)
            os.startfile(os.path.join(movie_file, movie[x]))
            if 'play next' in querry:
                os.startfile(os.path.join(movie_file,movie[x]))
            elif 'stop music' in querry:
                os.kill()

        elif 'send email' in querry:
            try:
                speak("What do you want to send?")
                content = takeCommand()
                to ="arup1098sarkar@gmail.com"
                sendEmail(to,content)
                speak("boss email has been sent")

            except Exception as e:
                print(e)
                print("Sorry Boss,i failed to send this email")









