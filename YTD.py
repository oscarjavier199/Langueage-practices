#program downloads a youtube video in highest resolution to local folder

from pytube import YouTube
from sys import argv

link = ("link here")
video  = YouTube(link)

print(f"Title: {video.title}")

download = video.streams.get_highest_resolution()

download.download('/mnt/o/videos')
