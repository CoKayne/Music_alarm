import os
import datetime
import json
from time import sleep
from pygame import mixer

with open("settings.json", "r", encoding = "utf8") as jfile: #open json for init
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
now_time_cpy = datetime.datetime.now().strftime("%H:%M") #the time now copy for testing use 

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
        song_index = int(1)
        song_list = {}
        keep_choosing = bool(True)

        with open("settings.json", "r", encoding="utf8") as jfile:
            jdata = json.load(jfile)

        for file_name in os.listdir("./"):
            if file_name.endswith(".mp3"):
                print("(" + str(song_index) + ")", str(file_name))
                song_list.update({song_index:file_name})
                song_index += 1 

        while keep_choosing == True:

            song_cmd = int(input("Please enter the song you want to change to : "))        

            try:
                jdata["SONG"] = song_list[song_cmd]
                keep_choosing = False
            except KeyError: 
                print("Song not found, please try again !")
                keep_choosing = True 

        with open("settings.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4)

        song = jdata["SONG"]
        print("Setting complete!")

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
        print(is_week_day(now_day_cpy))
        print(now_day_cpy)
        print(which_day)
        print(now_time_cpy)
        print(alarm_time)

    elif cmd == str(8): #testing use
        mixer.init()
        mixer.music.load(song)
        mixer.music.play()
        while mixer.music.get_busy():
            sleep(1)
        break