from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "       A friendly reminder",
            message = "Go to hell, You are shit, your life is a shit",
            app_icon = "cbt.ico",
            timeout = 3)
        time.sleep(7200)    