from pytube import YouTube

link = input("İndireceğiniz Video Linki:  ")

yt = YouTube(link)
ys = yt.streams.get_highest_resolution()

print("Indiriliyor")
ys.download()
print("Indirildi")