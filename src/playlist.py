from src.channel import Channel
import datetime


class PlayList(Channel):
    tracks = []

    def __init__(self, title, url, playlist_id):
        super().__init__(url, title)
        self.playlist_id = playlist_id

    def add_track(self, track_duration):
        self.tracks.append(track_duration)

    @property
    def total_duration(self):
        total = datetime.timedelta()
        for track in self.tracks:
            total += track
        return total

    def show_best_videos(self):
        if not self.videos:
            return None

        best_video = max(self.videos, key=lambda video: video.likes)
        return best_video.url
