from django.shortcuts import render
from .forms import  LyricsForm
from extensions.lyrics import find_lyrics
# Create your views here.
def lyrics(request):
    if request.method == "POST":
        song_name =  request.POST.get("song_name",False)
        artist_name =  request.POST.get("artist_name",False)
    else:
        form = LyricsForm()
    return render(request,"lyrics/home.html",{'form':LyricsForm})