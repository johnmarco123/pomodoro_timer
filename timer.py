import math
from playsound import playsound
import time
work_length = int(input("Work session length in minutes: ")) * 60
break_length = int(input("Break session length in minutes: ")) * 60
count_down = work_length
timer_type = "Work"


def format_time(time):
    seconds = str(time % 60)
    minutes = str(math.floor(time / 60))
    if len(seconds) < 2:
        seconds = "0" + seconds

    if len(minutes) < 2:
        minutes = "0" + minutes

    return minutes + ":" + seconds


while True:
    print("Time left: " + format_time(count_down), end="\r")
    time.sleep(0.1)
    count_down -= 1

    if count_down == 0:
        if timer_type == "Work":
            timer_type = "Break"
            count_down = break_length
            playsound("bell1.mp3")
        else:
            timer_type = "Work"
            count_down = work_length
            playsound("bell2.mp3")
