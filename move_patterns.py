from keyboard import press, release
from random import randrange
from time import sleep


# Jump
def jump():
    press("Space")
    sleep(randrange(0, 600) / 600)
    release("Space")
