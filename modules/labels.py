from imports import *


def change_labels(artist, album, songname, song_path):
    """"runs a PS script that gets the args above as its own args, and changes the label"""
    ps_dir = 'F:\\Scripts\\Python\\mp3_youtube_downloader\\modules\\powershell\\'
    os.chdir(ps_dir)
    artist = artist.encode('ISO-8859-1')
    album = album.encode('ISO-8859-1')
    songname = songname.encode('ISO-8859-1')
    song_path = song_path.encode('ISO-8859-1')
    subprocess.call(['powershell',
                     '-ExecutionPolicy',
                     'Bypass',
                     '.\\change_labels.ps1',
                     "'{0}'".format(artist),
                     "'{0}'".format(album),
                     "'{0}'".format(songname),
                     "'{0}'".format(song_path)],
                    shell=True,
                    stdout=subprocess.PIPE)


def label_only():
    working_dir = raw_input("Working Directory: ")
    artist = raw_input("Artist: ")
    album = raw_input("Album: ")
    song_list = os.listdir(working_dir)
    print "Changing Songs Labels..."
    for song in song_list:
        songname = song.replace("_", " ")[:-4]
        song_path = os.path.join(working_dir, song)
        change_labels(artist, album, songname, song_path)
