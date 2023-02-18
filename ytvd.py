from pytube import YouTube
link = "https://youtu.be/EAYlckSaviI?list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl"
yt = YouTube(link)
# print(yt.title)
# print(yt.thumbnail_url)
va = yt.streams.all()
a = yt.streams.filter(only_audio=True)
v = yt.streams.filter(only_video=True)
vlist = list(enumerate(a))
for i in vlist:
    if "160kbps" in i:
        print("h",i)
    else:    
     print(i)
dvn = int(input("enter:  "))
video[dvn].download()
print("Downloded")
