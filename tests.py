import datetime
import time

start = datetime.datetime.now() + datetime.timedelta(0, 20)
time.sleep(2)
end = datetime.datetime.now()

print(str(start) + '\n' + str(end))