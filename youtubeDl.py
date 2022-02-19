import pafy

url = input(str("Enter url : "))
video = pafy.new(url)
bestaudio = video.getbestaudio()
print(video.title)
bestaudio.download()