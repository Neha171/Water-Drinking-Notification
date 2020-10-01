import pyttsx3
import time
from plyer import notification

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def notifyme():
    speak("Abhinav Sir, Please Drink Water")

if __name__ == '__main__':
    while True:
        notifyme()
        notification.notify(
            title = """Please Drink Water Now""",
            message = "1. Water Helps to Maximize Physical Performance" \
                  " 2. Hydration Has a Major Effect on Energy Levels and Brain Function" \
                  "3. Drinking Water May Help to Prevent and Treat Headaches" \
                  "4. Drinking More Water Can Help With Weight Loss" ,
                  app_icon = "E:\\Notification\\icon.ico",
                  timeout = 10
        )
        time.sleep(1800)
