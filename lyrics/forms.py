from django import forms
#--------------------------------Forms---------------------------------
class LyricsForm(forms.Form):
    song_name = forms.CharField(label='Songs name', max_length=40,widget=forms.TextInput(attrs={'placeholder': 'Songs Name'}))
    artist_name = forms.CharField(label='Artists name', max_length=40,widget=forms.TextInput(attrs={'placeholder': 'Artists Name'}))
#----------------------------------------------------------------------

