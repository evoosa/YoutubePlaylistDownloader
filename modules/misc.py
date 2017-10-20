def prompt():
    """"prompts for user input"""
    artist = raw_input("Artist: ")
    album = raw_input("Album: ")
    to_hd = raw_input("Move To HD Afterwards? (y/n): ")
    playlist_url = raw_input("Playlist URL: ")
    return artist, album, playlist_url, to_hd
