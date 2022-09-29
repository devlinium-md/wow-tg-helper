import time

import pyautogui

file = "images/disconect_fhd.jpeg"
while True:
    result = pyautogui.locateOnScreen(file, confidence=0.2)
    if result is not None:
        print("ok")
        time.sleep(0.5)
    result = None
