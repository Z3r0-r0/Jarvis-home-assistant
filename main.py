from voice_engine import speak
from listener import listen
from commands import execute_command
from gpt_module import ask_gpt
import utils

speak("Hello sir, i am Jarvis. How can i assist you today?")

while True:
    command = listen()
    if not command:
        continue

    if "gpt" in command or "explică" in command or "ce este" in command:
        response = ask_gpt(command)
        speak(response)
    else:
        execute_command(command)
