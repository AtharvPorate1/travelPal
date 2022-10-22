from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.http import HttpResponse
# request.POST.get('uri')
# Create your views here.
def index(request):
    if request.method=='POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='5f95e5320f634e4eb9135054fa9f86aa',client_secret='30c35d01e8c3402082494cedfea85857',))
        results = spotify.artist_top_tracks(artist_uri)
        final_result=results['tracks']
        return render(request,'music/hello.html',{"results":final_result})
    else:
      return render(request,'music/hello.html')


    # def options(request):
    #     self.

