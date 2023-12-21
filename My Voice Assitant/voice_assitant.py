import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests #pip install requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# Function to get the weather
def get_weather(city):
    #put your Open Weather Map API Key below (1234) -:
    api_key = '1234'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # Make a GET request to the OpenWeatherMap API
    response = requests.get(base_url)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        # Extract temperature information from the response
        temperature = data['main']['temp']
        temperature_celsius = temperature - 273.15  # Convert temperature to Celsius

        # Speak the temperature
        speak(f"The current temperature in {city} is {temperature_celsius:.2f} degrees Celsius.")
        print(f"The current temperature in {city} is {temperature_celsius:.2f} degrees Celsius.")
    else:
        speak("Sorry, I couldn't fetch the weather information at the moment.")
        print("Sorry, I couldn't fetch the weather information at the moment.")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    a = "Good Morning"
    b = "Good Afternoon"
    c = "Good Evening"
    if hour>=0 and hour<12:
        speak(a)

    elif hour>=12 and hour<18:
        speak(b)

    else:
        speak(c)

    print("I am Jarvis Sir. Please tell me how may I help you?")
    speak("I am Jarvis Sir. Please tell me how may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust the dynamic energy threshold based on ambient noise
        r.adjust_for_ambient_noise(source, duration=1)

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        #below here in the place of your_mail_ID@gmail.com and your_password, put your mail ID and its password from which you want to send the message

        server.login('your_mail_ID@gmail.com', 'your_password')
        server.sendmail('your_mail_ID@gmail.com', to, content)
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
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
            print("Opening youtube...")
            speak("Opening youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening youtube...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            print("Opening stackoverflow...")
            speak("Opening stackoverflow...")
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            #in the place of 'Your_Music_Directory_here', please make sure you put your music directory URL
            music_dir = 'Your_Music_Directory_here'
            if os.path.exists(music_dir) and os.path.isdir(music_dir):
                songs = os.listdir(music_dir)

                # Check if the list of songs is not empty before accessing its first element
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    print("No songs found in the specified directory.")
                    speak("No songs found in the specified directory.")
            else:
                print("The specified directory does not exist.")
                speak("The specified directory does not exist.")

        elif 'the current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")


        elif 'open visual studio' in query:
            codePath = "C:\\Users\\dell\\Desktop\\VSCodeUserSetup-x64-1.84.2.exe"
            os.startfile(codePath)

        elif 'close visual studio' in query:
            codePath = "C:\\Users\\dell\\Desktop\\VSCodeUserSetup-x64-1.84.2.exe"
            os.close(codePath)

        elif 'send an email' in query:
            speak("What should I say?")
            print("What should I say?")

            content = takeCommand()
            #put here your mail ID, to whom you want to share your message
            to = "xyz@gmail.com"

            try:
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, I encountered an error while sending the email.")


        elif 'current temperature' in query:
            speak("Sure, please tell me the city name.")
            city_name = takeCommand().lower()
            get_weather(city_name)

        elif 'ok bye' in query:
            speak("Okay, It has been a nice talk with you")
            exit()

#If you are facing any problem in deploying the project, then kindly, visit this article, 'https://dipansutech.com/i-just-developed-a-jarvis/'
#Enjoy! Ba-Bye!
