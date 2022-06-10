import pyttsx3 #texttovoicemodule 
import speech_recognition as sr 
import wikipedia 
import webbrowser 
import datetime 
import os 
import smtplib 

engine = pyttsx3.init('sapi5') #MicrosoftspeakAPI 
voices = engine.getProperty('voices') #print(voices[0].id)check voices available in code 
engine.setProperty('voice', voices[0].id) 

#           XXXXXXXXXXXXXXXXXXXXX  BASIC FUNCTIONALITY  XXXXXXXXXXXXXXXXXXXXX 

def speak(audio): #speakfunctionof  Sort 
    engine.say(audio) 
    engine.runAndWait() 

def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<=12: 
        speak("good morning!") 
    elif hour>=12 and hour<18: 
        speak("good afternoon!") 
    else: 
        speak("good evening!") 
    speak("Welcome to the Mini-project ") 
    speak("My name is Sort ") 
    speak("I will assist you here ") 

def takeCommand(): #it takes microphone voice as input and convert it into string output 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening.........") 
        r.pause_threshold = 1  
        audio = r.listen(source) 
    try: 
        print("Recognizing.........") 
        query = r.recognize_google(audio, language='en-in') 
        print("User said: ", query)
    except Exception as e: 
        print(e) #don't print the error  
        print("Can you say that again, Please.........") 
        return "None" 
    return query 

def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() 
    server.starttls() 
    server.login('guptaiti2311@gmail.com','gupta@123') 
    server.sendmail('guptaiti2311@gmail.com',to,content) 
    server.close() 

if __name__ == "__main__": 
    wishMe()  
    while True: 
        query = takeCommand().lower()  
        #        XXXXXXXXXXXXXXXXXXXXX  ONLINE SEARCHING  XXXXXXXXXXXXXXXXXXXXX  
        if  'wikipedia' in query: 
             speak('Searching Wikipedia...') 
             query = query.replace("wikipedia", "") 
             results = wikipedia.summary(query, sentences=1) 
             speak("According to wikipedia") 
             print(results) 
             speak(results) 
        elif 'open youtube' in query: 
             webbrowser.open("https://www.youtube.com") 
        elif 'open google' in query: 
             webbrowser.open("https://www.google.com") 
        elif 'open facebook' in query: 
             webbrowser.open("https://www.facebook.com") 
        elif 'open twitter' in query: 
             webbrowser.open("https://www.twitter.com") 
        elif 'open instagram' in query: 
              webbrowser.open("https://www.instagram.com") 
        elif 'open music' in query: 
              webbrowser.open("https://music.youtube.com/watch?v=wdEl9h4dAKo&list=RDAMVMwdEl9h4dAKo")
        elif 'open song' in query: 
              webbrowser.open("https://music.youtube.com/watch?v=wdEl9h4dAKo&list=RDAMVMwdEl9h4dAKo") 
        elif 'sing a song' in query: 
              webbrowser.open("https://music.youtube.com/watch?v=wdEl9h4dAKo&list=RDAMVMwdEl9h4dAKo") 
        elif 'the time' in query: 
              strTime = datetime.datetime.now().strftime("%H:%M:%S") 
              speak("The Time is") 
              speak(strTime) 
              print(strTime) 
        #        XXXXXXXXXXXXXXXXXXXXX  DESKTOP FUNCTIONS  XXXXXXXXXXXXXXXXXXXXX  
        elif 'open virtual studio' in query: 
            path = "D:\Microsoft VS Code\Code.exe" 
            os.startfile(path)
        #        XXXXXXXXXXXXXXXXXXXXX  EMAIL  XXXXXXXXXXXXXXXXXXXXX  
        elif 'send email to mam' in query: 
            try: 
                speak("What should I mail her?") 
                content= takeCommand() 
                to = "itig8224@gmail.com" 
                sendEmail(to,content) 
                speak("Email has been successfully send to her!") 
            except Exception as e: 
                print(e) 
                speak("Sorry Email is not send please check and let me know") 

        elif 'send mail to me' in query: 
            try: 
                speak("What should I mail her?") 
                content= takeCommand() 
                to = "" 
                sendEmail(to,content) 
                speak("Email has been successfully send to her!") 

            except Exception as e: 
                print(e) 
                speak("Sorry Email is not send please check and let me know") 
