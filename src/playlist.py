import datetime
from googleapiclient.discovery import build


class PlayList:
    api_key: str = "AIzaSyBIE1Zoz-q-0QXM1H8hp3e_N9xnuT_9xfI"
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        playlist_info = self.youtube.playlists().list(
            part='snippet',
            id=self.playlist_id
        ).execute()
        self.title = playlist_info['items'][0]['snippet']['localized']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.playlist_id
        self.videos = []

    @property
    def total_duration(self):
        duration = datetime.timedelta()
        for video in self.videos:
            duration += video["duration"]
        return duration

    def show_best_video(self):
        best_video = max(self.videos, key=lambda video: video["likes"])
        return best_video["url"]

