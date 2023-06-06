import os, json
from googleapiclient.discovery import build

import isodate

class Channel:
    """Класс для ютуб-канала"""

    api_key: str = "AIzaSyBIE1Zoz-q-0QXM1H8hp3e_N9xnuT_9xfI"
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        try:
            channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

            self.title = channel['items'][0]['snippet']['title']
            self.description = channel['items'][0]['snippet']['description']
            self.url = 'https://www.youtube.com/channel/' + self.__channel_id
            self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
            self.video_count = channel['items'][0]['statistics']['videoCount']
            self.view_count = channel['items'][0]['statistics']['viewCount']
        except Exception as e:
            print("Error", str(e))

    @property
    def channel_id(self):
        return self.__channel_id


    def __str__(self):
        return f"{self.title}({self.url})"


    def __add__(self, other):
        if isinstance(other, Channel):
            return int(self.subscriber_count) + int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for +")


    def __sub__(self, other):
        if isinstance(other, Channel):
            return int(self.subscriber_count) - int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for -")


    def __lt__(self, other):
        if isinstance(other, Channel):
            return int(self.subscriber_count) < int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for <")


    def __le__(self, other):
        if isinstance(other, Channel):
            return int(self.subscriber_count) <= int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for <=")


    def __gt__(self, other):
        if isinstance(other, Channel):
            return int(self.subscriber_count) > int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for >")


    def __ge__(self, other):
        if isinstance(other, Channel):
            return int(self.subscriber_count) >= int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for >=")


    def __eq__(self, other):
        if isinstance(other, Channel):
            return int(self.subscriber_count) == int(other.subscriber_count)
        else:
            raise TypeError("Unsupported operand type for ==")


    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""


        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        print(json.dumps(channel, indent=2, ensure_ascii=False))


    def to_json(self, file_name):
        """Сохраняет в файл значения атрибутов экземпляра `Channel`"""


        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.__dict__, file, ensure_ascii=False)


