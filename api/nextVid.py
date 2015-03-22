import tornado.web
import data.Video


class NextVid(tornado.web.RequestHandler):
    def get(self):
        video = data.Video.Video.get_next()
        if video is None:
            self.set_status(404)
            return
        video.set_as_played()
        self.write(video.video_id)