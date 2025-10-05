import speech_recognition as sr
from voice_engine import speak

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ascult...")
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio, language="ro-RO")
            print(f"Tu ai spus: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Nu am înțeles. Poți repeta, te rog?")
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            print(f"Eroare la recunoaștere: {e}")
        return ""
