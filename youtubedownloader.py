# Pitfalls of Modern Daawa - https://www.youtube.com/watch?v=cX0_lNTF8zg&list=PLhQYGg7P8kb3vVLiIaCyUGB-nc49GyNJc
from pytube import Playlist
from pytube import YouTube
from ffmpy import FFmpeg
import glob
import os.path
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
# import eyed3


downloadDir = "C:/Users/omahmed/Desktop/POMD/"
outputDir = downloadDir + "/output/"
playlistURL = "https://www.youtube.com/watch?v=cX0_lNTF8zg&list=PLhQYGg7P8kb3vVLiIaCyUGB-nc49GyNJc"
tagInfo = {
    "album": "Unlock your Heart",
    "artist": "Mirza Yawar Baig",
    "year": "2018",
    "comment": "www.mhmic.org",
    "copyright": "Mahmood Habib Masjid and Islamic Center",
    "genre": "Religion"
}

pl = Playlist(playlistURL)
pl.populate_video_urls()
videos = pl.video_urls
i = 0
for video in videos:
    yvid = YouTube(video)
    stream = yvid.streams.first()
    currfile = stream.default_filename
    i+=1
    print ("starting:",yvid.title)
    # stream.download(downloadDir)
    outputfile = outputDir+currfile[0:-4].replace(" ", "-") + '.mp3'
    if os.path.isfile(downloadDir+currfile):
        ff = FFmpeg(
            inputs={ downloadDir+currfile: None},
            outputs={outputfile: '-c:a libmp3lame'}
        )
        print (ff.cmd)
        # ff.run()
        
        mp3 = MP3File(outputfile)
        mp3.set_version(VERSION_2)
        mp3.album = tagInfo["album"]
        mp3.url = str(yvid.watch_url)
        mp3.song = str(yvid.title)
        mp3.year = str(tagInfo["year"])
        mp3.artist = tagInfo["artist"]
        mp3.comment = tagInfo["comment"]
        mp3.genre = tagInfo["genre"]
        mp3.track = str(i)
        print(mp3.get_tags())
        mp3.save()
        # mp3 = eyed3.load("song.mp3")
        # mp3.tag.album = tagInfo["album"]
        # mp3.tag.album_artist = tagInfo["artist"]
        # mp3.tag.title = yvid.title
        # mp3.tag.track_num = i
        # mp3.tag.release_date = 2018
        # mp3.tag.save()

