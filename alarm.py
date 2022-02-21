import datetime
import json
from time import sleep
from pygame import mixer

with open("settings.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)
    
def is_week_day(week_number): #judge whether it is weekdays
    if week_number < 5:
        return True
    else:
        return False
        
alarm_time = jdata["TIME"] #setting up alarm time
song = jdata["SONG"] #setting up song to play
which_day = jdata["DAY_NUM"] #the key to check what day should the alarm be on

now_day_cpy = datetime.datetime.today().weekday() #the number of day now copy to make everyday alarm work

while True:

    cmd = input("What settings do you want to change? :\n" "(1) time  " "(2) song  " "(3) day\n" "(4) alarm on  " "(5) alarm off  " "(6) check settings\n")

    if cmd == str(1):

        print("---------------------------")
        change_time = input(str("Please enter the time you want to change to ex.10:27 : "))
        with open("settings.json", "r", encoding="utf8") as jfile:
            jdata = json.load(jfile)
        jdata["TIME"] = change_time
        with open("settings.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4)
        alarm_time = jdata["TIME"]
        print("setting complete!")

    elif cmd == str(2):

        print("---------------------------")
        change_song = input(str("Please enter the song you want to change to ex.high_on_life.mp3 : "))
        with open("settings.json", "r", encoding="utf8") as jfile:
            jdata = json.load(jfile)
        jdata["SONG"] = change_song
        with open("settings.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4)
        song = jdata["SONG"]
        print("setting complete!")

    elif cmd == str(3):

        print("---------------------------")
        change_day_cmd = input(str("(1) weekdays\n" "(2) weekends\n" "(3) everyday\n" "Please enter the day you want the alarm to be activate : \n"))

        if change_day_cmd == str(1):

            with open("settings.json", "r", encoding="utf8") as jfile:
                jdata = json.load(jfile)
            jdata["DAY_NUM"] = True
            with open("settings.json", "w", encoding="utf8") as jfile:
                json.dump(jdata, jfile, indent=4)
            which_day = jdata["DAY_NUM"]
            print("setting complete!")

        elif change_day_cmd == str(2):

            with open("settings.json", "r", encoding="utf8") as jfile:
                jdata = json.load(jfile)
            jdata["DAY_NUM"] = False
            with open("settings.json", "w", encoding="utf8") as jfile:
                json.dump(jdata, jfile, indent=4)
            which_day = jdata["DAY_NUM"]

        elif change_day_cmd == str(3):

            with open("settings.json", "r", encoding="utf8") as jfile:
                jdata = json.load(jfile)
            jdata["DAY_NUM"] = is_week_day(now_day_cpy)
            with open("settings.json", "w", encoding="utf8") as jfile:
                json.dump(jdata, jfile, indent=4)
            which_day = jdata["DAY_NUM"]
            print("setting complete!")
            
    elif cmd == str(4):

        print("---------------------------")
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

    elif cmd == str(5):
        print("---------------------------")
        break

    elif cmd == str(6):

        print("---------------------------")
        with open("settings.json", "r", encoding="utf8") as jfile:
            jdata = json.load(jfile)
        for key in jdata:
            print(jdata[key])

    # testing use
    elif cmd == str(7):
        
        print("---------------------------")
        print(is_week_day(now_day))
        print(now_day)
        print(which_day)
        print(now_time)
        print(alarm_time)
        print(can_play)