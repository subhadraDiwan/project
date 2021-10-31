import pyttsx3
import speech_recognition as sr
import datetime
import os 
import cv2
import random
import webbrowser
import pywhatkit as kit
import sys
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1,phrase_time_limit=44)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en.in')
        print(f"user said: {query}")


    except Exception as e:
        speak("say that again plz...")
        return "none"
    return query    
    
      
#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    speak("Hello")

    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<16:
        speak("good afternoon")
    elif hour<=17 and hour<20:
        speak("good evening")    
    else:
        speak("good night")    
    strTime = datetime.datetime.now().strftime("%H:%M:%S") 
    speak(f"mam,the time is{strTime}")
    speak("I am alexa. please tell me how can i help you")

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?source=techcrunch&apiKey=2cbc3edcb67040b5bf49f5cc4aaaacf0'    
    main_page = request.get(main_url).json()
    articles = main_page["articles"]
    head = []
    for i in range(len(day)):
        speak(f"today's {day[i]} news is {head[i]}")


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        #logic building for task

        if "open notepad" in query:
            path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories"
            os.startfile(path)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "Alexa play marathi old songs" in query:
            webbrowser.open("https://www.youtube.com/watch?v=-ceyEAuKIbg")

        elif "Alexa open new hindi songs" in query:
            webbrowser.open("https://www.youtube.com/watch?v=v51Ij0h9msM")      

        elif "Alexa play cartoon" in query:
            webbrowser.open("https://www.youtube.com/watch?v=7A_ovYw6pYk")    

        elif "play my favorite songs" in query:
            webbrowser.open("https://www.youtube.com/watch?v=VZkMDMewnUM")

        elif "Alexa play deshbhakti songs" in query:
            webbrowser.open("https://www.youtube.com/watch?v=XC-sm0gMWTk")   

        elif "open google" in query:
            speak("mam, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")    

        elif "play music" in query:  
            music_dir = 'E:\\My Songs\\Vedio'
            Songs = os.listdir(music_dir)
            rd = random.choice(Songs)
            print(Songs)
            os.startfile(os.path.join(music_dir,rd))  

        elif "time" in query:
            strfTime = datetime.datetime.now().strtime("%H:%M:%S") 
            speak(f"mam,the time is{strTime}")

        elif "what is Today's date" in query:
            datet = date.date.now().datet("%d:")    

        elif "open the engineering file" in query:
            codePath = "D:\Engg files"
            os.startfile(codePath)

        elif "open visual code" in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open Android code" in query:
            codePath = "C:\\Program Files\\Android\\Android Studio\bin\\studio64.exe"   
            os.startfile(codePath)    

        elif  "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read() 
                cv2.imshow('webcam', img)
                k= cv2.waitKey(2)
                if k==2:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "you are a mad" in query:
            speak("shut up")    

        elif "close notepad" in query:
            speak("Okay mam, closing notepad") 
            os.system("taskkill /f /im notepad.exe")   

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = 'E:\\alarm'
                Songs = os.listdir(music_dir)  
                os.startfile(os.path.join(music_dir, alarm))  

        elif  "send message" in query: 
            kit.sendwhatmsg("+919567488524", "I happy very happy... ", 16, 39)  


        elif "no thanks" in query:
            speak("Thanks for using me mam, have good day..")
            sys.exit()   

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")        

        elif "sleep the system" in query:
            os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")    

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyup("alt")

        elif "tell me the news" in query:
            speak("please wait mam, feteching the latest news")       


        elif "temperature" in query:
            from pywikihow import search_wikihow
            search = "temperature in detail"
            url = f"https://www.google.com/search?q={search}"     
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current{search} is {temp}")

        elif "activate how to do mode" in query:
            speak("How to do mode is activated please tell me what you want to know")
            while True:
                speak("please tell me what you want to know")
                how = takecommand() 
                try:
                    if "exit" in how or "close" in how:
                        speak("okay mam, how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)   
                except Exception as e:
                    speak("sorry mam, i am not able to find this")        

#------------------------To find my location using ip Address
        
        elif "where i am" in query or "where we are" in query:
            speak("wait mam, let me cheack")
            try:
                ipAdd = request.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_date = geo_requests.json()
                city = geo_date['city']
                country = geo_date['country']
                speak(f"mam, i am not sure but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry mam, Due to network issue i am not able to find where we are.")
                pass    

        
                     
        speak("mam, do you have any other work")    



        


    