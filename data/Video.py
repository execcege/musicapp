import BaseModel

from peewee import *


class Video(BaseModel.BaseModel):
    id = PrimaryKeyField(db_column='id')
    video_id = TextField(db_column='video_id', index=True)
    played_p = BooleanField(db_column='played_p', default=False)

    class Meta:
        db_table = 'Video'

    def set_as_played(self):
        self.played_p = True
        self.save()

    @classmethod
    def get_by_id(cls, song_id):
        try:
            return Video.get(Video.id == song_id)
        except:
            return None

    @classmethod
    def create(cls, video_id):
        song = Video(video_id=video_id)
        song.save()

    @classmethod
    def get_next(cls):
        songs = Video.select().where(Video.played_p == False).order_by(Video.id)
        try:
            return songs[0]
        except:
            return None

Video.create_table(True)