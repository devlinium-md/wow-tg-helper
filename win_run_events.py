import pyautogui
import time
import os
import datetime
import cv2


def start_wow():
    start_time = datetime.datetime.now() + datetime.timedelta(0, 20)
    try:
        os.startfile("C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe")
    except Exception:
        pass
    while True:
        btn = pyautogui.locateOnScreen('images/wow_button_ru.png', confidence=0.5)
        if btn is not None:
            btn_position = pyautogui.center(btn)
            time.sleep(1)
            pyautogui.click(btn_position)
            return "ok"
        elif datetime.datetime.now() > start_time:
            return "not ok"


def screenshot():
    return pyautogui.screenshot()

