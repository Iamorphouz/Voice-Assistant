import pyautogui
import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import pyautogui
from plyer import notification

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendMessageWp(query):
    query = query.replace("message on ","")
    query = query.replace("jarvis","")
    pyautogui.press("super")
    pyautogui.typewrite(query)
    pyautogui.press("enter")
    speak("contact name")
    pyautogui.hotkey('ctrl','n')
    speak("speak")
    name = "none"
    msg = "none"
    while name == "none":
        name = takeCommand().lower()
        pyautogui.hotkey('ctrl','a')
        pyautogui.typewrite("")

    print(name)
    if name!="none" :
        pyautogui.typewrite(name)
        pyautogui.press('tab')
        pyautogui.press("enter")
        speak("whats the message")
        while msg == "none":
            msg = takeCommand().lower()
            if msg != "none":
                print(msg)
                pyautogui.sleep(3)
                pyautogui.typewrite(msg)
                pyautogui.sleep(2)
                pyautogui.press("enter")
                pyautogui.press("enter")
            notification.notify(
                title = "WhatsApp message sent :- ",
                message = f"message sent to {name}"
            )