from googleapiclient.discovery import build


class Video:
    """Класс для ютуб-канала"""

    api_key: str = "AIzaSyBIE1Zoz-q-0QXM1H8hp3e_N9xnuT_9xfI"
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video, ):
        """
        Создайте файл src/video и в нем класс Video
        Реализуйте инициализацию реальными данными следующих атрибутов экземпляра класса Video:
        id видео
        название видео
        ссылка на видео
        количество просмотров
        количество лайков
        """
        self.id_video = id_video
        self.title = None
        self.url = None
        self.view_count = None
        self.view_likes = None

        try:
            response = self.youtube.videos().list(
                part='snippet, statistics',
                id=self.id_video
            ).execute()
            video = response['items'][0]

            self.title = video['snippet']['title']
            self.url = 'https://www.youtube.com/watch?v=' + self.id_video
            self.view_count = video['statistics']['viewCount']
            self.view_likes = video['statistics']['likeCount']
        except Exception as e:
            print("Error", str(e))


    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, id_video, playlist_id):
        super().__init__(id_video)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
