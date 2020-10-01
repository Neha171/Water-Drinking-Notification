import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = """Please Drink Water Now""",
            message = "1. Water Helps to Maximize Physical Performance" \
                  " 2. Hydration Has a Major Effect on Energy Levels and Brain Function"\
                  "3. Drinking Water May Help to Prevent and Treat Headaches" \
                  "4. Drinking More Water Can Help With Weight Loss" ,
                  app_icon = "E:\\Notification\\icon.ico",
                  timeout = 10
        )
        time.sleep(1800)