from pytube import YouTube
link = input("Enter video`s link: ")
yt = YouTube(link)
video = yt.streams.get_highest_resolution()
video.download()
print('Done')