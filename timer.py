import math
from playsound import playsound
import time
import os

work_length = int(input("Work session length in minutes: ")) * 60
break_length = int(input("Break session length in minutes: ")) * 60
count_down = work_length
timer_type = "Work"


os.system('cls')
current_path = os.path.dirname(os.path.abspath(__file__))


def format_time(time):
    seconds = str(time % 60)
    minutes = str(math.floor(time / 60))
    if len(seconds) < 2:
        seconds = "0" + seconds

    if len(minutes) < 2:
        minutes = "0" + minutes

    return minutes + ":" + seconds


while True:
    print(f'{timer_type} time left: {format_time(count_down)}', end="\r")
    time.sleep(1)
    count_down -= 1

    if count_down == 0:
        if timer_type == "Work":
            timer_type = "Break"
            count_down = break_length
            playsound(os.path.join(current_path, "bell2.mp3"))
            os.system('cls')
        else:
            timer_type = "Work"
            count_down = work_length
            playsound(os.path.join(current_path, "bell1.mp3"))
            os.system('cls')
