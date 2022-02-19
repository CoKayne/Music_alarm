import datetime
import json
from time import sleep
from pygame import mixer

with open("data.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)
    
alarm_time = jdata["TIME"] #setting up alarm time
song = jdata["SONG"] #setting up song to play
which_day = jdata["DAY_NUM"]

def is_week_day(week_number): #judge whether it is weekdays
    if week_number < 5:
        return True
    else:
        return False

cmd = input("What settings do you want to change? :\n" "1. alarm time\n" "2. song\n" "3. alarm day\n" "4. exit\n")

if cmd == str(1):

    change_time = input(str("Please enter the time you want to change to ex.10:27 : "))
    with open("data.json", "r", encoding="utf8") as jfile:
        jdata = json.load(jfile)
    jdata["TIME"] = change_time
    with open("data.json", "w", encoding="utf8") as jfile:
        json.dump(jdata, jfile, indent=4)
    alarm_time = jdata["TIME"]

elif cmd == str(2):

    change_song = input(str("Please enter the song you want to change to ex.high_on_life.mp3 : "))
    with open("data.json", "r", encoding="utf8") as jfile:
        jdata = json.load(jfile)
    jdata["SONG"] = change_song
    with open("data.json", "w", encoding="utf8") as jfile:
        json.dump(jdata, jfile, indent=4)
    song = jdata["SONG"]

elif cmd == str(3):

    change_day_cmd = input(str("1. weekdays\n" "2. weekends\n" "Please enter the day you want the alarm to be activate : \n"))

    if change_day_cmd == str(1):

        with open("data.json", "r", encoding="utf8") as jfile:
            jdata = json.load(jfile)
        jdata["DAY_NUM"] = True
        with open("data.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4)
        which_day = jdata["DAY_NUM"]

    elif change_day_cmd == str(2):

        with open("data.json", "r", encoding="utf8") as jfile:
            jdata = json.load(jfile)
        jdata["DAY_NUM"] = False
        with open("data.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4)
        which_day = jdata["DAY_NUM"]

elif cmd == str(4):

    while True:

        now_time = datetime.datetime.now().strftime("%H:%M") #the time now
        now_day = datetime.datetime.today().weekday() #the number of day now

        if(now_time == alarm_time and is_week_day(now_day) == which_day):
            mixer.init()
            mixer.music.load(song)
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                sleep(1)
            break

        else:
            print("not yet")
            sleep(10)