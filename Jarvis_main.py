import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import Dictapp
import os
import pyautogui
import pyvolume

from plyer import notification
import screen_brightness_control as sbc

pwd = "password"
adm = "admin name"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        if "jarvis" in query:
            if query!="":    
                print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

for i in range(3):
        a = input("Enter Password to open Jarvis :- ")
        if (a==pwd):
            print(f"WELCOME {adm} SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
            speak(f"WELCOME {adm} SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
            break
        elif (i==2 and a!=pwd):
            exit()
        elif (a!=pwd):
            print("Try Again")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            while True:
                query = takeCommand().lower()
                if "jarvis" in query:
                    query = query.replace("jarvis ","")
                    if "go to sleep" in query:
                        speak("Ok sir , You can me call anytime")
                        break 
                    elif "message on whatsapp" in query:
                        from MsgWhatsApp import sendMessageWp
                        sendMessageWp(query)
                    elif "google" in query:
                        from SearchNow import searchGoogle
                        searchGoogle(query)
                    elif "youtube" in query:
                        from SearchNow import searchYoutube
                        searchYoutube(query)
                    elif "wikipedia" in query:
                        from SearchNow import searchWikipedia
                        searchWikipedia(query)
                    elif "time" in query:
                        from TimeNow  import time_converter
                        strTime = datetime.datetime.now().strftime("%H:%M")    
                        strTime = time_converter(strTime)
                        speak(f"Sir, the time is {strTime}")
                    elif "open" in query:  
                        query = query.replace("open","")
                        query = query.replace("jarvis","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.press("enter")   
                    elif "brightness" in query:
                        import screen_brightness_control as sbc
                        if "increase" in query:
                            current_brightness = sbc.get_brightness()[0]
                            new_brightness = current_brightness + 5
                            sbc.fade_brightness(new_brightness)
                        elif "decrease" in query:
                            current_brightness = sbc.get_brightness()[0]
                            if(current_brightness > 5):
                                new_brightness = current_brightness - 5
                            sbc.fade_brightness(new_brightness)
                        query = query.replace("brightness ","")
                        query = query.replace("%","")
                        try:
                            brightness_value = int(query)
                        except ValueError:
                            brightness_value = 50
                        sbc.set_brightness(brightness_value) 
                    elif "screenshot" in query:
                        import pyautogui #pip install pyautogui
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")
                    elif "calculate" in query:
                        from Calculatenumbers import WolfRamAlpha
                        from Calculatenumbers import Calc
                        query = query.replace("calculate","")
                        query = query.replace("jarvis","")
                        Calc(query)
                    elif "temperature" in query:
                        search = query
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")
                    elif "weather" in query:
                        search = query
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")
                    elif "finally sleep" in query:
                        speak("Going to sleep,sir")
                        exit()
                    elif "click my photo" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")
                    elif "slide" in query:
                        if "next" in query:
                            pyautogui.press("right")
                        elif "previous" in query:
                            pyautogui.press("left")
                    elif "volume up" in query:
                        from Keyboard import volumeup
                        speak("Turning volume up,sir")
                        volumeup()
                    elif "volume down" in query:
                        from Keyboard import volumedown
                        speak("Turning volume down, sir")
                        volumedown()
                    elif "volume" in query:
                        query=query.replace("volume ","")
                        query=query.replace("%","")
                        try:
                            volume_value = int(query)
                        except ValueError:
                            volume_value = 50
                        pyvolume.custom(percent=volume_value)
                    elif "open" in query:  
                        query = query.replace("open","")
                        query = query.replace("jarvis","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.press("enter")   
                    elif "hello" in query:
                        speak("Hello sir, how are you ?")
                    elif "i am fine" in query:
                        speak("that's great, sir")
                    elif "how are you" in query:
                        speak("Perfect, sir")
                    elif "thank you" in query:
                        speak("you are welcome, sir")
                    elif "pause" in query or "pose" in query or "play" in query:
                        pyautogui.press("space")
                    elif "mute" in query:
                        pyautogui.press("m")
                        speak("video muted")
                    elif "cut" in query:
                        pyautogui.hotkey('ctrl','x')
                    elif "cut all" in query:
                        pyautogui.hotkey('ctrl','a')
                        pyautogui.hotkey('ctrl','x')   
                    elif "copy" in query:
                        pyautogui.hotkey('ctrl','c')
                    elif "copy all" in query:
                        pyautogui.hotkey('ctrl','a')
                        pyautogui.hotkey('ctrl','c')
                    elif "paste all" in query:
                        pyautogui.hotkey('ctrl','v')
                    elif "full screen" in query or "fullscreen" in query:
                        pyautogui.hotkey('f11')
                    elif "slideshow" in query or "slide show" in query:
                        pyautogui.hotkey('f5')
                    elif "page search" in query:
                        pyautogui.hotkey('ctrl','f')
                        query = query.replace("page search","")
                        pyautogui.typewrite(query)

                    elif "close current app" in query:
                        pyautogui.hotkey('alt','f4')

                    elif "open" in query or "launch" in query:
                        from Dictapp import openappweb
                        openappweb(query)
                    elif "close" in query and "tab" in query:
                        from Dictapp import closeappweb
                        closeappweb(query)
                    elif "shutdown the system" in query:
                        speak("Are You sure you want to shutdown")
                        shutdown = ""
                        while(shutdown != "no" or  shutdown != "yes"):
                            shutdown = takeCommand().lower
                            if shutdown == "yes":
                                os.system("shutdown /s /t 1")

                            elif shutdown == "no":
                                break
                    elif query == "none":
                        pass
                    else:
                        speak("Sorry, I am not able to understand")
                        speak("Is anything else I can do?")
                        
                    



