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
    filename_m4a = (song + ".m4a")#.decode('ISO-8859-1')).encode('ISO-8859-1')
    filename_mp3 = (song + ".mp3")#.decode('ISO-8859-1')).encode('ISO-8859-1')
    #album = album.decode('ISO-8859-1').encode('ISO-8859-1')
    #filename_m4a = unicode(filename_m4a,'ISO-8859-1')
    #filename_mp3 = unicode(filename_mp3, 'ISO-8859-1')
    print "Converting to mp3..."
    subprocess.call([
        "ffmpeg", "-i",
        os.path.join(working_dir, album, filename_m4a),
        "-acodec", "libmp3lame", "-ab", "256k",
        os.path.join(working_dir, album,  filename_mp3),
        "-loglevel", "quiet"
    ])
    os.remove(os.path.join(working_dir, album, filename_m4a))
    print "Done!\n"
    return 0

