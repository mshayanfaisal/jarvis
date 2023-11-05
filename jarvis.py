import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour

    if 6 <= hour < 12:
        speak("Good morning sir!")
    elif 12 <= hour < 18:
        speak("Good afternoon sir!")
    elif 18 <= hour < 24:
        speak("Good evening sir")
    else:
        speak("Good night sir")

    speak("Jarvis at your service, Please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "NONE"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com", "123")
    server.sendmail('abc@gmail.com', to, content)
    server.close()

def search_in_chrome(query):
    speak("What should I search?")
    search_query = takeCommand().lower()
    url = f"https://www.google.com/search?q={search_query}"
    wb.open_new_tab(url)

def screenshot():
    img = pyautogui.screenshot()
    img.save(r"C:\Users\shaya\Downloads\ss.png")

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif 'search in chrome' in query:
            search_in_chrome(query)

        elif 'play naats' in query:
            songs_dir = r'C:\Users\shaya\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remeber" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
            
        elif 'Do you know anything?' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that" + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            quit()
