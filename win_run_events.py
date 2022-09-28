import datetime
import os
import threading
import time

import keyboard
import pyautogui

import move_patterns as mv


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
            return "WoW is starting"
        elif datetime.datetime.now() > start_time:
            return "Something went wrong"


def screenshot():
    try:
        return pyautogui.screenshot()
    except Exception:
        img = open("images/error.png", "r")
        return img


l = 1


def no_afk_mode():
    while True:
        if l == 0:
            break
        time.sleep(mv.randrange(0, 120))
        mv.afk()


event = threading.Thread(target=no_afk_mode)


def start_afk():
    event.start()
    return "No AFK mode is ON"


def stop_afk():
    global l
    l = 0
    event.join()
    return "No AFK mode is OFF"


def enter():
    keyboard.press_and_release("Enter")
