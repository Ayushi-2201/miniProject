from soundplay import playsound

import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def is_a_valid_number(alarm):
    while True:
        if alarm.isdigit():
            alarm = int(alarm)
            return alarm
        else :
            print("Enter a number")
       
            
            

def alarm(set_off_time):
    print(CLEAR)
    while set_off_time >= 0:
        minutes = int(set_off_time // 60)
        seconds = int(set_off_time % 60)
        print(f"{CLEAR_AND_RETURN}{minutes:02d}:{seconds:02d}")
        set_off_time -= 1
        time.sleep(1)
    print(CLEAR_AND_RETURN)
    playsound('Python Mini Projects\Alarm Clock\sound.mp3')


minutes = input("Enter the number of minutes after which you want the alarm to go off : ")
minutes = is_a_valid_number(minutes)
seconds = input("Enter the number of seconds after which you want the alarm to go off : ")
seconds = is_a_valid_number(seconds)

set_off_time = (60 * minutes) + seconds

alarm(set_off_time)
