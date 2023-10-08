from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(secs):
    time_passed = 0
    print(time_passed)

    print(CLEAR)

    while time_passed < secs:
        time.sleep(1)
        time_passed += 1

        time_left = secs - time_passed
        mins_left = time_left // 60
        secs_left = time_left % 60

        print(f"{CLEAR_AND_RETURN} Alarm will ring in {mins_left:02d}:{secs_left:02d}")

    playsound("alarm.mp3")

minutes = int(input("How many minutes to wait ? : "))
seconds = int(input("How many seconds to wait ? : "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds) 