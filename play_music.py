from subprocess import call
import os
import operator
import time

path = "./music_files"

while True:

   music_files = os.listdir(path)

   if len(music_files) == 0:
      print "No songs found - Sleeping for 5 seconds"
      time.sleep(5)

   song_infos = []

   for music_file in music_files:
      full_path = os.path.join(path, music_file)
      song_infos.append([full_path, os.path.getmtime(full_path)])

   song_infos = sorted(song_infos, key=operator.itemgetter(1))

   print song_infos

   for song_info in song_infos:
      song = song_info[0]
      call(["mpg123", song])
      call(["rm", song])
      print "Done playing"
