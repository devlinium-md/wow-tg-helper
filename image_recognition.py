import pyautogui
import time

while True:
    btn = pyautogui.locateOnScreen('images/wow_button_ru.png', confidence=0.5)
    if btn is not None:
        btn_position = pyautogui.center(btn)
        time.sleep(1)
        pyautogui.click(btn_position)
        break
