from imports import *


def copy_album_dir(hd_music_dir, artist, album, work_dir,):
    """"copies the local album dir in the work_dir to HD"""
    hd_album_dir = os.path.join(hd_music_dir, artist, album)
    if os.path.exists(hd_album_dir) == False:
        os.makedirs(hd_album_dir)
    local_album_dir = os.path.join(work_dir, album)
    song_list = os.listdir(local_album_dir)
    for song in song_list:
        file_local_path = os.path.join(local_album_dir, song)
        shutil.copy2(file_local_path, hd_album_dir)




