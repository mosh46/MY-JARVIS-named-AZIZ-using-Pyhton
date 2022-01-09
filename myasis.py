import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice", voices[0].id)

def speak(string):
    engine.say(string)
    engine.runAndWait()

def wishMe():
    now = datetime.datetime.now()
    hour = int(now.strftime("%I"))
    print(hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am AZIZ Sir. Please tell me how may I help you")   

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)
        
    try:
        print("Rcognizing......")
        query = r.recognize_google(audio,language="en-pk")
        print(f"user said : {query}")
        speak(query)
    except Exception as e:
        print("Say that again please...")
        print(e)  
        return "None"
        

    return query
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    speak("Hi! mister uzair")
    wishMe()
    while True:
        query = take_command().lower()

        if query == "what is your name":
            speak(f"my name is AZIZ")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        
        #elif 'what is the time' or "time" in query:
        #    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        #    speak(f"Sir, the time is {strTime}")

        elif "wikipedia" in query:
            speak('Searching Wikipedia...')
            query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'email to' in query:
                try:
                    speak("Whome should I send?email id please")
                    mail = take_command()
                    to = "quratulainbhurgri@gmail.com"  
                    speak("What should I say?")
                    content = take_command()+"from AZIZ Uzair ASIF"   
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend .I am not able to send this email")  
        
        elif "quit" in query:
            exit()
        else:
            print("please say it again")