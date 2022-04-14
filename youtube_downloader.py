from pytube.cli import on_progress
from pytube import YouTube
from pytube import Playlist
from os import mkdir,listdir,rename,system
from os.path import splitext
from sys import platform

def finish():
  print("\tVideo downloaded.")

def finished():
  print("Video downloaded.")

def takedownline():
  print()

def download(option,voice_on=0):
  if "playlist" in option:
    playlist = Playlist(option)
    if "Downloaded Videos" not in listdir():
        mkdir("Downloaded Videos")
    if playlist.title not in listdir("Downloaded Videos"):
        mkdir("Downloaded Videos" +"\\"+ str(playlist.title))
    downloadpath = "Downloaded Videos" +"\\"+ playlist.title
    i = 0
    if voice_on == 0:
      for yt in playlist.videos:
        try:
          vid = yt.streams.get_highest_resolution().download(output_path=downloadpath)
          yt_title = yt.title
          i += 1
          if len(yt_title) <= 35:
            print(option)
            yt_title = str(i) + ". \t" + yt_title
            print(yt_title + "." * (45 - len(yt_title)))
          elif len(yt_title) > 35:
            print(option)
            yt_title = str(i) + ". \t" + yt_title[:35]
            print(yt_title + "." * (45 - len(yt_title)))
          b,e = splitext(vid)
          rename(vid,b + ".mp4")
          yt.register_on_complete_callback(finish())
          print("-"*50)
        except:
          pass
    elif voice_on == 1:
      for yt in playlist.videos:
        try:
          vid = yt.streams.filter(only_audio=True).first().download(output_path=downloadpath)
          yt_title = yt.title
          i += 1
          if len(yt_title) <= 35:
            print(option)
            yt_title = str(i) + ". \t" + yt_title
            print(yt_title + "." * (45 - len(yt_title)))
          elif len(yt_title) > 35:
            print(option)
            yt_title = str(i) + ". \t" + yt_title[:35]
            print(yt_title + "." * (45 - len(yt_title)))
          b,e = splitext(vid)
          rename(vid,b + ".mp3")
          yt.register_on_complete_callback(finish())
          print("-"*50)
        except:
          pass
    
  elif "watch?v" in option and "playlist" not in option:
    yt = YouTube(option, on_progress_callback=on_progress)
    yt_title = yt.title
    if "Downloaded Videos" not in listdir():
      mkdir("Downloaded Videos")
    downloadpath = "Downloaded Videos"
    if voice_on == 0:
      vid = yt.streams.get_highest_resolution().download(output_path=downloadpath)
      if len(yt_title) <= 35:
        print(option)
        print(yt_title + "." * (45 - len(yt)))
      elif len(yt_title) > 35:
        print(option)
        print(yt_title[:35] + "." * (45 - len(yt_title)))
      b,e = splitext(vid)
      rename(vid,b + ".mp4")
      yt.register_on_complete_callback(takedownline())
      finished()
    elif voice_on == 1:
      vid = yt.streams.filter(only_audio=True).first().download(output_path=downloadpath)
      if len(yt_title) <= 35:
        print(option)
        print(yt_title + "." * (45 - len(yt_title)))
      elif len(yt_title) > 35:
        print(option)
        print(yt_title[:35] + "." * (45 - len(yt_title)))
      b,e = splitext(vid)
      rename(vid,b + ".mp3")
      yt.register_on_complete_callback(takedownline())
      finished()
  else:
    print("Try a YouTube URL")

if __name__ == '__main__':
  while True:
    isitafile = input("Is there a file I should take care of ? y/n: ").strip()
    if isitafile.lower() == "y":
      urls = []
      wherethefile = input("Where is the file: ").strip()
      with open(wherethefile,"r",encoding="utf8") as f:
        urls = [str(x).strip() for x in f.readlines() if "youtube.com/watch" in str(x) or "youtube.com/playlist" in str(x)]
      voice_on   = input("Do you want to download only audio? y/n: ").strip()
      print("-"*50)
      if voice_on.lower() == "y":
        for x in urls:
          try:
            download(x,1)
            print("-"*50)
          except:
            pass
      elif voice_on.lower() == "n":
        for x in urls:
          try:
            download(x,0)
            print("-"*50)
          except:
            pass
      else:
        print("Please enter a legit answer!!!  y or n")
        continue
    elif isitafile.lower() == "n":
      option   = input("Please Enter URL: ")
      voice_on   = input("Do you want to download only audio? y/n: ")
      print("-"*50)
      if voice_on.lower() == "y":
        download(option,1)
      elif voice_on.lower() == "n":
        download(option,0)
      else:
        print("Please enter a legit answer!!!  y or n")
        continue
    else:
      print("Come on man type a letter what I want!!")
      continue
    while True:
      ask = input("Do you want to download sth else?(y/n): ")
      if ask.lower() == "y":
        print("-"*50)
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
    exit()
  else:
    system("clear")
    exit()
