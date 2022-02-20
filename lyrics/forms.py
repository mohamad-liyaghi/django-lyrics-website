from django import forms

class LyricsForm(forms.Form):
    song_name = forms.CharField(label='Songs name', max_length=20)
    artist_name = forms.CharField(label='Artists name', max_length=20)

