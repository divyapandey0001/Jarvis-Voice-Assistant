import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
import gtts 
import pygame
import os

engine = pyttsx3.init()
recognizer = sr.Recognizer()

newsapi = ("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")

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

from gtts import gTTS
import pygame
import os

def speak(text):
    # Create audio
    tts = gTTS(text=text, lang="en")
    tts.save("temp.mp3")

    # Play using pygame
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    # Wait until audio finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Delete temp audio
    
    

def aiprocess(command):
  client = OpenAI(api_key="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")

  completion= client.chat.completions.create(
      odel="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."},
        {"role": "user", "content": "command"}
    ]
    )
  return completion.choices[0].message.content
def processCommand(c):
    c = c.lower()
    print("Processing command:", c)

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open whatsapp" in c:
        webbrowser.open("https://web.whatsapp.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        if song in musiclibrary.music:
            webbrowser.open(musiclibrary.music[song])
        else:
            speak("Song not found")

    elif "news" in c:
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
        r = requests.get(url)

        if r.status_code == 200:
            articles = r.json().get("articles", [])
            for article in articles[:5]:
                speak(article["title"])
        else:
            speak("Unable to fetch news")

    else:
        output =aiprocess(c)
        speak =(output)
        
# ---------------------- MAIN LOOP ------------------------

speak("Initializing Jarvis...")

while True:
    try:
        with sr.Microphone() as source:
            print("listening")
            audio = recognizer.listen(source)

        word = recognizer.recognize_google(audio).lower()
        print("You said:", word)

        if word == "jarvis":
            speak("Yes, how can I help?")
            with sr.Microphone() as source:
                print("Listening for command...")
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)
            print("Command received:", command)

            processCommand(command)

    except Exception as e:
        print("Error:", e)
