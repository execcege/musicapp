import tornado.web
import data.Video
import modules.password


class Add(tornado.web.RequestHandler):
    def post(self):
        video_id = self.get_argument("videoId")
        password = self.get_argument("password")

        if not modules.password.password_ok_p(password):
            self.set_status(401)
            return

        data.Video.Video.create(video_id)