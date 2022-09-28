import threading

stopper_clicker = 1


def hello():
    while True:
        print('Hello')
        if stopper_clicker == 0:
            break


event = threading.Thread(target=hello)


def start():
    event.start()


def end():
    event.join()


a = input()
while True:
    m = input()
    match m:
        case '1':
            start()
        case '2':
            stopper_clicker = 0
            end()
