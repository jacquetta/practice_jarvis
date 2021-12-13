import pyttsx3
from decouple import config


# using decouple helps me to get value from environment variables
USERNAME = config('USER')
BOTNAME =config('BOTNAME')


# sapi5 is a Microsoft Speech API
engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Text to Speech Conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()