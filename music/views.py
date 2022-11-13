from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.http import HttpResponse
import requests
# request.POST.get('uri')
# Create your views here.
def index(request):
    if request.method=='POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='enter your client id',client_secret='enter your client secret',))
        results = spotify.artist_top_tracks(artist_uri)
        final_result=results['tracks']
        return render(request,'music/hello.html',{"results":final_result})
    else:
      return render(request,'music/hello.html')


    # def options(request):
    #     self.



