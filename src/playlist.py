import datetime
from googleapiclient.discovery import build
import isodate


class PlayList:
    """
    Класс, представляющий плейлист YouTube.

    Attributes:
        api_key (str): Ключ API для доступа к YouTube Data API.
        youtube: Объект YouTube API.
        playlist_id (str): Идентификатор плейлиста.
        title (str): Заголовок плейлиста.
        url (str): URL плейлиста.
        videos (list): Список объектов видео плейлиста.
    """
    api_key: str = "AIzaSyBIE1Zoz-q-0QXM1H8hp3e_N9xnuT_9xfI"
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        """
        Инициализирует объект PlayList.

        Args:
            playlist_id (str): Идентификатор плейлиста.
        """
        self.playlist_id = playlist_id
        playlist_info = self.youtube.playlists().list(
            part='snippet',
            id=self.playlist_id
        ).execute()
        self.title = playlist_info['items'][0]['snippet']['localized']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.playlist_id
        self.videos = []
        self.populate_videos()

    @classmethod
    def parse_duration(cls, duration):
        """
       Преобразует строковое значение продолжительности видео в объект timedelta.

       Args:
           duration (str): Строковое значение продолжительности видео.

       Returns:
           datetime.timedelta: Объект timedelta, представляющий продолжительность видео.
       """
        try:
            duration_iso8601 = isodate.parse_duration(duration)
            duration_timedelta = datetime.timedelta(seconds=duration_iso8601.total_seconds())
            return duration_timedelta
        except (TypeError, ValueError):
            return datetime.timedelta()

    def populate_videos(self):
        """
        Получает список видео плейлиста с использованием YouTube API.
        Заполняет список videos объектами видео плейлиста.
        """
        next_page_token = None
        while True:
            playlist_items = self.youtube.playlistItems().list(
                part="snippet,contentDetails",
                playlistId=self.playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            video_ids = [item['contentDetails']['videoId'] for item in playlist_items['items']]
            video_response = self.youtube.videos().list(
                part='contentDetails',
                id=','.join(video_ids)
            ).execute()

            self.videos.extend(video_response["items"])

            next_page_token = playlist_items.get("nextPageToken")
            if not next_page_token:
                break

    @property
    def total_duration(self):
        """
        Вычисляет общую длительность всех видео в плейлисте.

        Returns:
            datetime.timedelta: Общая длительность видео.
        """
        total_time = datetime.timedelta()
        for video in self.videos:
            iso_8601_duration = video['contentDetails']['duration']
            duration = self.parse_duration(iso_8601_duration)
            total_time += duration
        return total_time

    def show_best_video(self):
        """
        Возвращает URL видео с наибольшим количеством лайков.

        Returns:
            str: URL видео с наибольшим количеством лайков.
        """
        video_ids = [video['id'] for video in self.videos]
        statistics = self.youtube.videos().list(
            part='statistics',
            id=','.join(video_ids)
        ).execute()

        best_video = max(statistics['items'], key=lambda video: int(video['statistics']['likeCount']))
        best_video_id = best_video['id']
        return f"https://youtu.be/{best_video_id}"
