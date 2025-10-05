import datetime
from voice_engine import speak

def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Bună dimineața!")
    elif hour < 18:
        speak("Bună ziua!")
    else:
        speak("Bună seara!")
