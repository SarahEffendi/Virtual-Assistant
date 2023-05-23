from time import sleep
from googletrans import Translator
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition as sr
import os
import datetime
from playsound import playsound
import time


engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices) 
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 200)

def speak(audio): #audio is variable that has text
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# def wish():
#     hour= int(datetime.datetime.now().hour)
#     tt= datetime.datetime.now().strftime('%I:%M %p')
#     if hour >= 0 and hour<12:
#         speak(f"good morning sarah. I am virtual assistant isis. Its {tt}. How may i help you")
#     elif hour>=12 and hour<18:
#         speak(f"good afternoon sarah. I am virtual assistant isis. Its {tt}. How may i help you")
#     else:
#         speak(f"good evening sarah. I am virtual assistant isis. Its {tt}. How may i help you")

#audio to text
def takecom():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio= r.listen(source)
        
    try:
        print("Recognising...")
        text= r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:
        print("Network connection error")
        return 'none'
    return text


def translategl(query):
    speak("Sure maam")
    print(googletrans.LANGUAGES)
    translater = Translator()
    speak("choose the language in which you want to translate")
    d= input("To lang: ")
    text_to_translate= translater.translate(query,src="auto",dest=d)
    text= text_to_translate.text
    try:
        speakgl= gTTS(text=text,lang=d,slow= False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("Unable to translate")

