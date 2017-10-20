$artist = $args[0]
$album = $args[1]
$songname = $args[2]
$song_path = $args[3]

## load the assmbly
[Reflection.Assembly]::LoadFrom("taglib-sharp.dll")

## load mp3 file
$mp3 = [TagLib.File]::Create($song_path)

[string]$mp3.Tag.Artists = $artist
[string]$mp3.Tag.AlbumArtists = $artist
[string]$mp3.Tag.Album = $album
[string]$mp3.Tag.Title = $songname

$mp3.save()

#"c:\users\evoosa\desktop\song.mp3"