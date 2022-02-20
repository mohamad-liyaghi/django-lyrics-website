from lyricsgenius import Genius
from .token import key
#----------------------------------------------------
genius = Genius(key)
def find_lyrics(song_name,artist_name):
    song = genius.search_song(song_name,artist_name)
    try:
        return song.lyrics
    except:
        return  "No results were found"
#----------------------------------------------------