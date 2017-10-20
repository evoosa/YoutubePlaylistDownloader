from imports import *


def get_url_list(playlist_url):
    """gets a list of the URLs in a youtube playlist"""
    print "getting the needed URLs..."
    p = subprocess.Popen(['youtube-dl', '--get-id', playlist_url, "-i"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    id_list = output.split("\n")[:-1]
    url_list = []
    for ID in id_list:
        url = "https://www.youtube.com/watch?v=" + ID
        url_list.append(url)
    print "OK Done with that."
    return url_list


def download_m4a(url, full_file_path, song_name):
    """downloads a .m4a file from the given url, to the exact given path"""
    ydl_opts = {
        'outtmpl': full_file_path,
        'format': 'bestaudio/best'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print "downloading: " + song_name
        ydl.download([url])
        print "Finished downloading: " + song_name + "\n"


def m4a_to_mp3(working_dir, album, song):
    """converts the .m4a file to .mp3 file"""
    filename = song + ".m4a"
    print "Converting to mp3..."
    subprocess.call([
        "ffmpeg", "-i",
        os.path.join(working_dir, album, filename),
        "-acodec", "libmp3lame", "-ab", "256k",
        os.path.join(working_dir, album, '%s.mp3' % song),
        "-loglevel", "quiet"
    ])
    os.remove(os.path.join(working_dir, album, filename))
    print "Done!\n"
    return 0
