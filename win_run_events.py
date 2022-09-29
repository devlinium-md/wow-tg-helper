import datetime
import os
import threading
import time
import images
import keyboard
import pyautogui
import os
import move_patterns as mv
import telebot

stopper_clicker = 1
disconnected = False
bot = telebot.TeleBot(str(open("api.key", "r").readline()))
user = str(open("users.conf", "r").readline())


def start_wow_simple():
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
        btn = pyautogui.locateOnScreen(images.wotlk_button, confidence=0.5)
        if btn is not None:
            btn_position = pyautogui.center(btn)
            time.sleep(2)
            pyautogui.click(btn_position)
            btn = pyautogui.locateOnScreen(images.wow_button, confidence=0.5)
            if btn is not None:
                btn_position = pyautogui.center(btn)
                time.sleep(2)
                pyautogui.click(btn_position)
                return "WoW is starting"
        elif datetime.datetime.now() > start_time:
            return "Something went wrong"


def checker_agent():
    global disconnected
    while True:
        disconnected = is_disconnected()
        if disconnected is True:
            start_wow_simple()
            disconnected = False
            bot.send_message(chat_id=user, text="You've been disconnected. Restarting WoW!!!!")


def is_disconnected():
    while True:
        result = pyautogui.locateOnScreen(images.disconect, confidence=0.5)
        if result is not None:
            return True
        time.sleep(1)
        result = None


wow_client_check = threading.Thread(target=checker_agent)


# def start_wow_auto():
#     try:
#         os.system("ECHO OFF")
#         os.system("taskkill /im WowClassic.exe")
#     except Exception:
#         pass
#     start_time = datetime.datetime.now() + datetime.timedelta(0, 20)
#     try:
#         os.startfile("C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe")
#     except Exception:
#         pass
#     while True:
#         btn = pyautogui.locateOnScreen(images.wotlk_button, confidence=0.5)
#         if btn is not None:
#             btn_position = pyautogui.center(btn)
#             time.sleep(2)
#             pyautogui.click(btn_position)
#             btn = pyautogui.locateOnScreen(images.wow_button, confidence=0.5)
#             if btn is not None:
#                 btn_position = pyautogui.center(btn)
#                 time.sleep(2)
#                 pyautogui.click(btn_position)
#                 wow_client_check.start()
#                 return "WoW is starting"
#         elif datetime.datetime.now() > start_time:
#             return "Something went wrong"


def start_wow_auto():
    wow_client_check.start()
    return "WoW is starting"


def screenshot():
    try:
        img = pyautogui.screenshot()
    except Exception:
        img = open(images.error, "rb")
    return img


def do_screenshots():
    while True:
        pass


screenshot_event = threading.Thread(target=do_screenshots)


def screenshots_auto_on():
    screenshot_event.start()


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
