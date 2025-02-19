#import the libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import matplotlib.pyplot as plt

SPOTIPY_CLIENT_ID = "4989571fddd74e60ab2a52e2244b70f3"
SPOTIPY_CLIENT_SECRET = "83bbadbcc14545f6a8bf1438f9d67b5a"
APP_REDIRECT_URI = "https://localhost:8080/"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="SPOTIPY_CLIENT_ID",
                                               client_secret="SPOTIPY_CLIENT_SECRET",
                                               redirect_uri="APP_REDIRECT_URI",
                                               scope="user-library-read"))

user_data = sp.current_user()
print('My data:')
print('Name:', user_data['display_name'])
print('Followers:', user_data['followers']['total'])
print('Link:', user_data['external_urls']['spotify'])