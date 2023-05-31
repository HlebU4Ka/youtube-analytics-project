import os, json
from googleapiclient.discovery import build

import isodate


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    @classmethod
    def installer_data(cls, channel_data):
        name = channel_data['name']
        description = channel_data['description']
        subscribers = channel_data['subscribers']
        number_videos = channel_data['number_videos']
        total_number_views = channel_data['total_number_views']
        return cls(name, description, subscribers, number_videos, total_number_views)


    def to_json(self):
        pass

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)

        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        print(json.dumps(channel, indent=2, ensure_ascii=False))


