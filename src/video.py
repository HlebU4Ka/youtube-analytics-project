
class Video:

    def __init__(self, id_video, name_video, link_video, view_count, view_likes ):
        self.id_video = id_video
        self.name_video = name_video
        self.link_video = link_video
        self.view_count = int(view_count)
        self.view_likes = int(view_likes)



class PLVideo:
    def __init__(self, video_id, title, video_link, views, likes, playlist_id):
        super().__init__(video_id, title, video_link, views, likes)
        self.playlist_id = playlist_id
