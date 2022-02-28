import pafy
from pydub import AudioSegment
import re
import requests
import subprocess
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

class Yt:

    def __init__(self, music_name):
        self.music_name = music_name

    def find_youtube_video(self):
        query_string = urllib.parse.urlencode({"search_query": self.music_name})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
        inspect = BeautifulSoup(clip.content, "html.parser")
        yt_title = inspect.find_all("meta", property="og:title")

        for concatMusic1 in yt_title:
            pass

        self.song_name = concatMusic1['content']
        self.song_url = clip2

        print("\n")
        print(concatMusic1['content'])
        print("--------------------------------------")

    def youtube_dl(self): 
        video = pafy.new(self.song_url)
        bestaudio = video.getbestaudio()
        print(video.title)
        bestaudio.download()

    def convert_file(self):
        # song_name = input(str("Please enter the name of your song ex.The Chainsmokers - High (Official Lyric Video) : "))
        song = AudioSegment.from_file(self.song_name + ".webm")
        print("Loaded")
        song.export(self.song_name + ".mp3", format="mp3", bitrate="320k")
        print("Converted and saved")
 
keep_searching = bool(True)

while keep_searching == True:
    music_to_search = input(str("Please enter the song you want to search : "))
    youtube = Yt(music_to_search)
    youtube.find_youtube_video()
    cmd = input(str("Is this the song you want to search ? [y/n] : "))
    if cmd == "y":
        keep_searching = False
        break
    elif cmd == "n":
        keep_searching = True

if keep_searching == False:
    youtube.youtube_dl()
    youtube.convert_file()   