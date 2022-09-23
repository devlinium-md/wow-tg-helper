import time
from keyboard import press, release
from random import randrange
from time import sleep


def afk():
    jump()


# Jump
def jump():
    press("Space")
    sleep(randrange(0, 600) / 600)
    release("Space")


def test():
    time.sleep(3)
    print("Test")