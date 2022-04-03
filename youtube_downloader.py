from pytube.cli import on_progress
from pytube import YouTube
from pytube import Playlist
from os import mkdir,listdir,rename,system
from os.path import splitext
from sys import platform
from renamefile import rename_file

def finish():
  print("\tVideo downloaded.")

def finished():
  print("Video downloaded.")

def altagec():
  print()

def download(option,sesvar=0):
  if "playlist" in option:
    playlist = Playlist(option)
    if "Downloaded Videos" not in listdir():
        mkdir("Downloaded Videos")
    if playlist.title not in listdir("Downloaded Videos"):
      mkdir("Downloaded Videos" +"\\"+ str(playlist.title))
    downloadpath = "Downloaded Videos" +"\\"+ playlist.title
    i = 0
    if sesvar == 0:
      for yt in playlist.videos:
        vid = yt.streams.get_highest_resolution().download(output_path=downloadpath)
        i += 1
        if len(yt.title) <= 35:
          yazi = str(i) + ". \t" + yt.title
          print(yazi + "." * (45 - len(yazi)),end="")
        elif len(yt.title) > 35:
          yazi = str(i) + ". \t" + yt.title[:35]
          print(yazi + "." * (45 - len(yazi)),end="")
        b,e = path.splitext(vid)
        rename(vid,rename_file(b) + ".mp4")
        yt.register_on_complete_callback(finish())
    elif sesvar == 1:
      for yt in playlist.videos:
        vid = yt.streams.filter(only_audio=True).first().download(output_path=downloadpath)
        i += 1
        if len(yt.title) <= 35:
          yazi = str(i) + ". \t" + yt.title
          print(yazi + "." * (45 - len(yazi)),end="")
        elif len(yt.title) > 35:
          yazi = str(i) + ". \t" + yt.title[:35]
          print(yazi + "." * (45 - len(yazi)),end="")
        b,e = path.splitext(vid)
        rename(vid,rename_file(b) + ".mp3")
        yt.register_on_complete_callback(finish())
    
  elif "watch?v" in option and "playlist" not in option:
    yt = YouTube(option, on_progress_callback=on_progress)
    if "Downloaded Videos" not in listdir():
      mkdir("Downloaded Videos")
    downloadpath = "Downloaded Videos"
    if sesvar == 0:
      vid = yt.streams.get_highest_resolution().download(output_path=downloadpath)
      b,e = path.splitext(vid)
      rename(vid,rename_file(b) + ".mp4")
      yt.register_on_complete_callback(altagec())
      finished() 
    elif sesvar == 1:
      vid = yt.streams.filter(only_audio=True).first().download(output_path=downloadpath)
      b,e = path.splitext(vid)
      rename(vid,rename_file(b) + ".mp3")
      yt.register_on_complete_callback(altagec())
      finished()
  else:
    print("Try a YouTube URL")

if __name__ == '__main__':
  while True:
    isitafile = input("Is there a file I should take care of ? y/n:")
    if isitafile.lower() == "y":
      urls = []
      wherethefile = input("Where is the file: ")
      with open(wherethefile,"r",encoding="utf8") as f:
        urls = [str(x).strip() for x in f.readlines() if "youtube.com/watch" in str(x) or "youtube.com/playlist" in str(x)]
      sesvar   = input("Do you want to download only audio? y/n: ")
      if sesvar.lower() == "y":
        for x in urls:
          download(x,1)
      elif sesvar.lower() == "n":
        for x in urls:
          download(x,0)
      else:
        print("Please enter a legit answer!!!  y or n")
        continue
    elif isitafile.lower() == "n":
      option   = input("Please Enter URL: ")
      sesvar   = input("Do you want to download only audio? y/n: ")
      if sesvar.lower() == "y":
        download(option,1)
      elif sesvar.lower() == "n":
        download(option,0)
      else:
        print("Please enter a legit answer!!!  y or n")
        continue
    else:
      print("Come onn mannn type a letter what I want!!")
      continue
    while True:
      ask = input("Do you want to download sth else?(y/n): ")
      if ask.lower() == "y":
        break
      elif ask.lower() == "n":
        exit()
      else:
        print("Wrong Answer Please Use Only y or n")
        if platform == "win32":
          system("cls")
        else:
          system("clear")
        continue
  if platform == "win32":
    system("cls")
    system("exit")
  else:
    system("clear")
    system("exit")