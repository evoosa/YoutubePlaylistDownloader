from imports import *


def get_title(url):
    """gets the title of a youtube video"""
    p = subprocess.Popen(['youtube-dl', '--get-title', url], stdout=subprocess.PIPE)
    output, err = p.communicate()
    return output[:-2]


def make_file_name(artist, title):
    """ creates the name in which you would like to save the song in the album directory"""
    title = title.decode("ISO-8859-1")
    title = title.lower()
    artist = artist.lower()
    if "-" in title:
        title = title.split("-")
        for part in title:
            if artist in part:
                title.remove(part)
        for i in range(len(title)):
            if title[i][0] == " ":
                title[i] = title[i][1:]
        song_name = ""
        for i in title:
            song_name += i
    elif artist in title:
        song_name = title.replace(artist, "")
        if song_name[0] == " ":
            song_name = song_name[1:]
    else:
        song_name = title
    song_name = song_name.replace('"', '')
    title_name = song_name.replace(" ", "_")
    return title_name, song_name


def generate_full_path(working_dir, album_name, song_name, ending):
    """generates a full path to a song from the given song name and album name"""
    file_name = song_name + ending
    full_file_path = os.path.join(working_dir, album_name, file_name)
    return full_file_path
