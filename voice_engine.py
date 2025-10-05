import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
