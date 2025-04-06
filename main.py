import speech_recognition as sr 
import webbrowser
import pyttsx3
import music_lib
import requests
from openai import OpenAI

engine = pyttsx3.init()
API_KEY = "b9a0e7c9e4f644438dcd6b3e05d9369b"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source,timeout=2)
    return r.recognize_google(audio)

def ai_process(command):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    )

    completion = client.chat.completions.create(
    model="google/gemma-3-27b-it:free",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content
    
def processcommand(c):
    if 'open google' in c.lower():
        webbrowser.open("https://google.com")
    elif 'open facebook' in c.lower():
        webbrowser.open("https://facebook.com")
    elif 'open youtube' in c.lower():
        webbrowser.open("https://youtube.com")
    elif 'open spotify' in c.lower():
        webbrowser.open("https://spotify.com")
    elif 'news' in c.lower():
        URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

        response = requests.get(URL)
        data = response.json()

        for article in data["articles"]:
            print(article["title"])
            speak(article["title"])
    elif c.lower().startswith('play'):
        song=c.lower().split(" ")[1]
        link = music_lib.music[song]
        webbrowser.open(link)
    else:
        output = ai_process(c)
        print(output)
        speak(output)

if __name__ == "__main__":
    speak("Initiallising Jarvis....")
    while True:
        r = sr.Recognizer()
        try:
            command=listen()
            if command.lower()=='jarvis':
                speak('Hey,Karan! How can I help you today?')

            command = listen()
            processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
