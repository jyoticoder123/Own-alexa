import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import cv2
import random
import pywhatkit as kit
import sys
import pyjokes
import pyautogui
import time
import email_to
import instaloader
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am dorothy Mam. Please tell me how may I help you")       
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        data1 = r.recognize_google(audio, language='en-in')
        print(f"User said: {data1}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return data1
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
    
        data1 = takeCommand().lower()

        if 'wikipedia' in data1:
            speak('Searching Wikipedia...')
            data1 = data1.replace("wikipedia", "")
            results = wikipedia.summary(data1, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in data1:
            webbrowser.open("youtube.com")
        elif 'open camera' in data1:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif 'wikipedia' in data1:
            speak("searching wikipedia....")
            data1 = data1.replace("wikipedia","")
            results = wikipedia.summary(data1, sentence = 10 )
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif 'open vs code' in data1:
            path = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'open notepad' in data1:
            path = "C:\\Users\\Hp\\OneDrive\\Desktop\\notepad - Shortcut.lnk"
            os.startfile(path) 
        elif 'close notepad' in data1:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")       
        elif 'open Powerpoint' in data1:
            path ="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path)
        elif 'tell me a joke' in data1:
            joke = pyjokes.get_joke()
            speak(joke)  
            print(joke)       
        elif 'open command prompt' in data1:
            os.system("start cmd") 
        elif "ip address" in data1:
            ip = get("https://api.ipify.org").text
            speak(f"your IP address is {ip}")
            print("your IP address is: ",ip)       
        elif 'open google' in data1:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif 'i love you' in data1:
            speak("i love you too sir, but please focus your study")
        elif 'i miss you' in data1:
            speak("i miss you too sir, we will meet again soon ")     
        elif 'send message' in data1:
            kit.sendwhatmsg("+919616566281", "this is testing protocol",2,25)   
        elif 'open linkedin' in data1:
            webbrowser.open("https://www.linkedin.com/login")    
        elif 'open instagram' in data1:
            webbrowser.open("https://www.instagram.com/accounts/login/")
        elif 'tell me about my friends' in data1:
            speak("sir, you have mainly three friends in your college ")
            time.sleep(1)
            speak("sir, do you want to know your friend's name ")
            condition = takeCommand().lower()
            if 'yes' in condition:
                speak("sir, your friend's name is Khushi chouhan, Muskan Rajoria, and Arya sharma")
                time.sleep(1)
                speak("sir, do you want to know about any particular person in your main friend list ")
                condition = takeCommand().lower()
                if 'yes' in condition:            
                    speak('sir, please tell me name what do you want to know about')
                    condition = takeCommand().lower()
                    if 'khushi chouhan' in condition or 'khusi chouhan' in condition or 'khushi' in condition or 'khusi' in condition:
                        speak("sir, khushi chouhan is your college friend , her branch is  Artificial Intelligence and Machine Learning  khushi is a chutiyaa friend, Enrollment number is 0 1 3 3 C L 2 1 1 0 2 3 , she is currently 4th semester ,she is belong to Bhopal ")
                    elif 'muskan rajoriya' in condition or 'muskan' in condition:
                        speak("sir, muskan rajoriya is your college friend , her branch is  Artificial Intelligence and Machine Learning , she is a chhhupa rustum women Enrollment number is 0 1 3 3 C L 2 1 1 0 2 8 , she is currently 4th semester ,she is belong to ganj bhasoda but lived in bhopal ") 
                    elif 'Arya sharma' in condition or 'arya' in condition:
                        speak("sir, Arya sharma is your college friend , her branch is  Artificial Intelligence and Machine Learning , your agarbatti friend Enrollment number is 0 1 3 3 C L 2 1 1 0 1 3 , she is currently 4th semester ,she is belong to Narsinghpur but lived in bhopal ")
                    elif ' no thanks' in condition:
                        speak('its my pleasure sir, have a good day')
                #elif 'no' in condition:
                else:
                    speak("okay sir, it's your choice")               
            #elif 'no' in condition:
            else:
                speak("okay sir")       
        elif 'hide all file' in data1 or 'hide this folder' in data1 or 'visible for everyone' in data1:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = takeCommand().lower()
            if 'hide' in condition:
                os.system("attrib +h /s /d")
                speak("sir, all the file in this folder are now visible to everyone. i wish you are taking")
            elif 'leave it' in condition or 'leave for me' in condition:
                speak("ok sir")    
        elif 'instagram profile' in data1 or 'profile on instagram' in data1:
            speak("sir Please Enter the user name correctly..")
            name = input("Enter username here :")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(2)
            speak("sir would you like to download profile picture of this account.")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder. now i am ready")
                if 'ok thanks' in condition:
                    speak("welcome sir it's not mention")    
            elif "no" in condition:
                speak("okay sir, as you wish")   
            else:
                pass 
        elif 'take screenshot' in data1 or "take a screenshot" in data1:
            speak("sir, please tell me the for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the scree for few second, i am taking screenshort")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next comman, sir")
        elif 'tell me about something me' in data1 or "tell me about me" in data1:
            speak("sir, your name is JYOTI DWIVEDI, you are from Madhya pradesh in Sidhi District ")
        elif 'who is my roommate' in data1:
            speak('sir, your room mate is Diya jain')
        elif 'tell me my enrollment number' in data1 or 'Enrollment' in data1:
            speak('sir, your enrollment number is 1 1 3 3 C L 2 1 1 0 2 1')
        elif 'what is my name' in data1:
            speak('sir, your name is JYOTI DWIVEDI')
        elif  'tell me my branch' in data1:
            speak('sir, your branch is Artificial Intelligence and Machine Learning')
            time.sleep(5)
            speak(" i can't believe it sir, your branch is related to me, congratulation sir, nice to meet you sir , have a good day")
        elif 'my current semester' in data1 or 'tell me my current semester' in data1:
            speak("sir, you are currently in fourth semester") 
            time.sleep(5)
            speak("oh my god sir, please don't scroll instagram reel your semester exam is near , so please focus your study")
        elif 'first semester result'in data1:
            speak("sir, you are pass in 1st semester , your 1st semester SGPA is 9 point 7 1 ")
        elif 'second semester result'in data1 or '2nd semester result'in data1:
            speak("sir, you are pass in 2nd semester , your 2nd semester SGPA is 7 point 6 7 ")
        elif 'third semester result'in data1 or '3rd semester result' in data1:
            speak("sir, you are pass in 3rd semester , your 3rd semester SGPA is 8 point 0 0 ")
            time.sleep(3)
            speak("congratulation sir, you are topper in 3rd semester")
        elif 'overall result' in data1:
            speak("sir, your current CGPA is 8 point 4 4")    

        elif 'open whatsapp web' in data1:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'switch the window' in data1:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)  
            pyautogui.keyUp("alt")      
        elif 'open my favourite song' in data1:
            webbrowser.open("https://www.youtube.com/watch?v=VCqWjVJxp2s")           
        elif 'play music' in data1:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in data1:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'where i am' in data1 or 'where we are' in data1:
            speak("wait sir, let me check")
            try:
                ipAdd =get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests =get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                print(f'{city} {country}')
            except Exception as e:
                speak("sorry mam , due to network issue i am not able to find where we are..")
                pass        
        elif 'email to jyoti' in data1:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "jyotidwivedi1445@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend jyoti . I am not able to send this email")
        elif 'shutdown the system' in data1:
            os.system("shutdown /s /t 5") 
        elif 'restart the system' in data1:
            os.system("shutdown /r /t 5")
        elif 'sleep the system' in data1:
            os.system("rundll32.exe powerporf.dll,SetSuspendState 0,1,0")                   
        elif 'no thanks' in data1:
            speak("thanks for using me sir , have a good day")
            sys.exit()
        # speak("sir do you have any other work ")