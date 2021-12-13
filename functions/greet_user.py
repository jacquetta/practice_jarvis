from datetime import datetime

def greet_user():
    """ greets user based on time and date """

    hour = datetime.now().hour
    if(hour >= 6) and (hour < 12):
       speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif(hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")