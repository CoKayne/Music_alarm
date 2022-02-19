import re
import requests
import subprocess
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

music_name = input(str("Please enter the song you want to search : "))
query_string = urllib.parse.urlencode({"search_query": music_name})
formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

inspect = BeautifulSoup(clip.content, "html.parser")
yt_title = inspect.find_all("meta", property="og:title")

for concatMusic1 in yt_title:
    pass

print(concatMusic1['content'])
print(clip2)

# Alternatively, you can do this for simplicity sake:
# subprocess.Popen("start /b " + "path\\to\\mpv.exe " + clip2 + "--no-video", shell=True)