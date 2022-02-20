from pydub import AudioSegment

song_name = input(str("Please enter the name of your song ex.The Chainsmokers - High (Official Lyric Video) : "))
song = AudioSegment.from_file(song_name + ".webm")
# TODO fix not only webm file format problem
print("Loaded")
song.export("neco.mp3", format="mp3", bitrate="320k")
print("Converted and saved")
