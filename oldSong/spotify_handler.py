import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "6e02a0d1c3ec4e27b4e19543e7ef6ade"
Client_Secret = "c8be7fef252b4c939502871a821e2f5a"
Redirect_URL = "http://example.com"

red_URL = "http://example.com/?code=AQD19p27iK4Vj91pirtujxno0tjzmtrKDjyicqdOHgbzdPINepHMkYG_Z4BuFn9D7njfybxKVLQZ3d71slwNnxdgPIUhCba_QOM88UqYDkdhe9y2t1hEdpL8zowDWlOz2H5--AEkms-a3wfaqVO54Mc-tdIe-6bR8BjduP1jVikzdDi1fGDsdcU"

class SpotifyHandler:
    def __init__(self):
        scope = "playlist-modify-private"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=Client_ID, client_secret=Client_Secret, redirect_uri=Redirect_URL))
        self.playlist = self.sp.playlist("2TFrSdbcSHvZuRvXTu13Vp")

    def search(self, query='track:Doxy'):
        result = self.sp.search(q=query, limit=1)
        return result["tracks"]["items"][0]['uri']

    def add_item_to_playlist(self, item):
        self.remove_item_from_playlist(item)
        self.sp.playlist_add_items(self.playlist['id'], [item])

    def remove_item_from_playlist(self, item):
        self.sp.playlist_remove_all_occurrences_of_items(self.playlist['id'], [item])


