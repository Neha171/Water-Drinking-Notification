import pyttsx3
import time
from plyer import notification
import os

class Main:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.message = "1. Water Helps to Maximize Physical Performance" \
                       "2. Hydration Has a Major Effect on Energy Levels and Brain Function" \
                       "3. Drinking Water May Help to Prevent and Treat Headaches" \
                        "4. Drinking More Water Can Help With Weight Loss"

        self.icon_path = os.path.join(os.getcwd(), "icon.ico")
        self.sleep_duration = 1800
        self.main_loop()

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def notifyme(self):
        self.speak("Abhinav Sir, Please Drink Water")


    def main_loop(self):
        while True:
            self.notifyme()
            notification.notify(title="Please Drink Water Now",
                message=self.message, app_icon=self.icon_path,
                timeout=10)

            time.sleep(self.sleep_duration)

main = Main()
