from django.shortcuts import render
from extensions.lyrics import find_lyrics
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response("Use it in this way : api/lyrics/lose yourself/eminem/")
@api_view(['GET'])
def lyrics(request,song_name,artist_name):
    return Response(find_lyrics(song_name,artist_name))