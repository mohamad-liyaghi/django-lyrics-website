from lyricsgenius import Genius
from .token import key
#----------------------------Convert To lyrics--------------------------------------------
genius = Genius(key,verbose = False,remove_section_headers = True,skip_non_songs = False)
def find_lyrics(song_name,artist_name):
    song = genius.search_song(song_name,artist_name)
    try:
        return song.lyrics.replace("Embed" ,"").replace("Lyrics","")
    except:
        return  "No results were found"
#-----------------------------------------------------------------------------------------
