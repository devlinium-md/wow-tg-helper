import datetime
import os
import threading
import time

import keyboard
import pyautogui

import move_patterns as mv

stopper_clicker = 1


def start_wow():
    import os
    try:
        os.system("ECHO OFF")
        os.system("taskkill /im WowClassic.exe")
    except Exception:
        pass
    start_time = datetime.datetime.now() + datetime.timedelta(0, 20)
    try:
        os.startfile("C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe")
    except Exception:
        pass
    while True:
        btn = pyautogui.locateOnScreen('images/wotlk_button.png', confidence=0.5)
        if btn is not None:
            btn_position = pyautogui.center(btn)
            time.sleep(2)
            pyautogui.click(btn_position)
            btn = pyautogui.locateOnScreen('images/wow_button_ru.png', confidence=0.5)
            if btn is not None:
                btn_position = pyautogui.center(btn)
                time.sleep(2)
                pyautogui.click(btn_position)
                return "WoW is starting"
        elif datetime.datetime.now() > start_time:
            return "Something went wrong"


def screenshot():
    try:
        img = pyautogui.screenshot()
    except Exception:
        img = open("images/error.png", "rb")
    return img



# def screenshots_auto_on():




def no_afk_mode():
    while True:
        if stopper_clicker == 0:
            break
        time.sleep(mv.randrange(0, 120))
        if stopper_clicker == 0:
            break
        mv.afk()


event = threading.Thread(target=no_afk_mode)


def start_afk():
    event.start()
    return "No AFK mode is ON"


def stop_afk():
    global stopper_clicker
    stopper_clicker = 0
    event.join()
    return "No AFK mode is OFF"


def enter():
    keyboard.press_and_release("Enter")
