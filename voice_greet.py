#Program to voice greeting hello 

import win32com.client

l = ["Boris", "Mark", "John"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for name in l:
    speaker.Speak(f"Hello {name}")
    speaker.Speak("How are you?")
