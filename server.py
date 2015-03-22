import tornado.ioloop
import tornado.web
import sys
import api.nextVid
import api.add
import wsHandlerHost
import modules.password

class ClientHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("client.html")
        
class HostHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("host.html")

application = tornado.web.Application([
    (r"/", ClientHandler),
    (r"/host", HostHandler),
    (r"/api/next", api.nextVid.NextVid),
    (r"/api/add", api.add.Add),
    (r"/host/websocket", wsHandlerHost.HostWebSocket),
    (r'/resources/client/(.*)', tornado.web.StaticFileHandler, {'path': "resources/client"}),
    (r'/resources/host/(.*)', tornado.web.StaticFileHandler, {'path': "resources/host"})
])

if __name__ == "__main__":
    port = sys.argv[1]
    application.listen(port, '0.0.0.0')
    passwordLoop = tornado.ioloop.PeriodicCallback(modules.password.generate_new_password, 600000)
    passwordLoop.start()
    tornado.ioloop.IOLoop.instance().start()