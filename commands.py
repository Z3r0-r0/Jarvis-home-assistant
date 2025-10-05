import webbrowser
import datetime
import os
from voice_engine import speak

def execute_command(command):
    # Timp și dată
    if "ora" in command or "cât e ceasul" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Este ora {now}")
    elif "dată" in command or "ce zi e azi" in command:
        today = datetime.date.today().strftime("%d %B %Y")
        speak(f"Astăzi este {today}")
    elif "ziua" in command or "ce zi e mâine" in command:
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d %B %Y")
        speak(f"Mâine va fi {tomorrow}")
    elif "ziua trecută" in command or "ce zi a fost ieri" in command:
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d %B %Y")
        speak(f"Ieri a fost {yesterday}")
    elif "anul" in command or "ce an e" in command:
        year = datetime.date.today().year
        speak(f"Suntem în anul {year}")
    elif "luna" in command or "ce lună e" in command:
        month = datetime.date.today().strftime("%B")
        speak(f"Suntem în luna {month}")
    elif "ziua săptămânii" in command or "ce zi a săptămânii e" in command:
        weekday = datetime.date.today().strftime("%A")
        speak(f"Astăzi este {weekday}")
    elif "data și ora" in command or "data și timpul" in command:
        now = datetime.datetime.now().strftime("%d %B %Y, %H:%M")
        speak(f"Data și ora curentă este {now}")
    elif "timpul" in command or "cât e timpul" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Timpul curent este {now}")
    
    # Deschidere site-uri
    elif "youtube" in command or "deschide youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Deschid YouTube.")
    elif "google" in command or "deschide google" in command:
        webbrowser.open("https://www.google.com")
        speak("Deschid Google.")
    elif "browser" in command or "deschide browserul" in command:
        webbrowser.open("https://www.google.com")
        speak("Deschid browserul.")
    elif "facebook" in command or "deschide facebook" in command:
        webbrowser.open("https://www.facebook.com/?locale=de_DE")
        speak("Deschid Facebook.")
    elif "instagram" in command or "deschide instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Deschid Instagram.")
    elif "twitter" in command or "deschide twitter" in command:
        webbrowser.open("https://www.twitter.com")
        speak("Deschid Twitter.")
    elif "linkedin" in command or "deschide linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        speak("Deschid LinkedIn.")
    elif "github" in command or "deschide github" in command:
        webbrowser.open("https://www.github.com")
        speak("Deschid GitHub.")
    elif "gmail" in command or "deschide gmail" in command:
        webbrowser.open("https://mail.google.com")
        speak("Deschid Gmail.")
    elif "whatsapp" in command or "deschide whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        speak("Deschid WhatsApp Web.")
    elif "telegram" in command or "deschide telegram" in command:
        webbrowser.open("https://web.telegram.org")
        speak("Deschid Telegram Web.")
    # Aplicații locale
    elif "muzică" in command or "pornește muzica" in command or "spotify" in command:
        try:
            os.startfile("https://open.spotify.com/")
            speak("Pornesc Spotify.")
        except:
            speak("Nu am găsit Spotify pe calculator.")
    elif "notează" in command or "notiță" in command:
        os.system("notepad.exe")
        speak("Deschid Notepad.")
    elif "cmd" in command or "command prompt" in command:
        os.system("start cmd")
        speak("Deschid Command Prompt.")
    elif "calculator" in command or "deschide calculatorul" in command:
        os.system("calc.exe")
        speak("Deschid Calculator.")
    elif "setări" in command or "deschide setările" in command:
        os.system("start ms-settings:")
        speak("Deschid Setările.")
    elif "explorer" in command or "deschide explorerul" in command or "file explorer" in command:
        os.system("explorer.exe")
        speak("Deschid File Explorer.")
    elif "calendar" in command or "deschide calendarul" in command:
        os.system("start outlookcal:")
        speak("Deschid Calendarul.")
    elif "hărți" in command or "deschide hărțile" in command or "maps" in command:
        os.system("start bingmaps:")
        speak("Deschid Hărțile.")
    elif "mail" in command or "deschide mailul" in command or "email" in command:
        os.system("start outlookmail:")
        speak("Deschid Mailul.")
    elif "camera foto" in command or "deschide camera foto" in command or "camera" in command:
        os.system("start microsoft.windows.camera:")
        speak("Deschid Camera Foto.")
    elif "ceas" in command or "deschide ceasul" in command or "alarmă" in command:
        os.system("start ms-clock:")
        speak("Deschid Ceasul.")
    elif "calculator de buzunar" in command or "deschide calculatorul de buzunar" in command or "calculator simplu" in command:
        os.system("start calculator:")
        speak("Deschid Calculatorul de Buzunar.")
    elif "vremea" in command or "deschide vremea" in command or "weather" in command:
        os.system("start bingweather:")
        speak("Deschid Vremea.")
    elif "știri" in command or "deschide știrile" in command or "news" in command:
        os.system("start msnews:")
        speak("Deschid Știrile.")
    elif "măsurător" in command or "deschide măsurătorul" in command or "measure" in command:
        os.system("start windowsmeasure:")
        speak("Deschid Măsurătorul.")
    elif "voice recorder" in command or "deschide voice recorder" in command or "înregistrare audio" in command:
        os.system("start soundrecorder:")
        speak("Deschid Voice Recorder.")
    elif "paint" in command or "deschide paint" in command or "deschide pictorul" in command:
        os.system("mspaint.exe")
        speak("Deschid Paint.")
    elif "word" in command or "deschide word" in command or "documente word" in command:
        try:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            speak("Deschid Microsoft Word.")
        except:
            speak("Nu am găsit Microsoft Word pe calculator.")
    elif "excel" in command or "deschide excel" in command or "foi de calcul excel" in command:
        try:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
            speak("Deschid Microsoft Excel.")
        except:
            speak("Nu am găsit Microsoft Excel pe calculator.") 

    # Oprire/repornire/deconectare
    elif "oprește" in command or "închide jarvis" in command or "stop" in command:
        speak("Oprire sistem. La revedere!")
        exit()
    elif "închide calculatorul" in command:
        speak("Închid calculatorul.")
        os.system("shutdown /s /t 1")
    elif "repornește calculatorul" in command:
        speak("Repornesc calculatorul.")
        os.system("shutdown /r /t 1")
    elif "deconectează" in command or "log out" in command:
        speak("Mă deconectez.")
        os.system("shutdown /l")
    # Căutare pe internet
    elif "caută" in command or "căutare" in command:
        query = command.replace("caută", "").replace("căutare", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Caut {query} pe Google.")
        else:
            speak("Te rog să specifici ce vrei să caut.")
    elif "găsește" in command or "caută pe internet" in command:
        query = command.replace("găsește", "").replace("caută pe internet", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Găsesc {query} pe internet.")
    elif "ajută-mă" in command or "cum să fac" in command:
        query = command.replace("ajută-mă", "").replace("cum să fac", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Încerc să te ajut cu {query}.")
        else:
            speak("Te rog să specifici ce ai nevoie.")            
    else:
        speak("Încerc să caut un răspuns...")
        webbrowser.open(f"https://www.google.com/search?q={command}")   