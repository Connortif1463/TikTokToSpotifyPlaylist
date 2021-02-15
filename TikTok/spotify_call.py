import spotipy
from spotipy.oauth2 import SpotifyPKCE
import requests
import secrets

sp = spotipy.Spotify(auth_manager=SpotifyPKCE(client_id=secrets.YOUR_APP_CLIENT_ID,redirect_uri=secrets.YOUR_APP_REDIRECT_URI))
requests.get('https://accounts.spotify.com/authorize?client_id='+secrets.YOUR_APP_CLIENT_ID+'&redirect_uri='+secrets.YOUR_APP_REDIRECT_URI+'&scope=user-read-private%20user-read-email&response_type=token&state=123')