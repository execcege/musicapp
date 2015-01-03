import tornado.ioloop
import tornado.web
import tornado.websocket
import sys

class ClientHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("client.html")
        
class HostHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("host.html")
        
class HostWebSocket(tornado.websocket.WebSocketHandler):
    hosts = []
    
    def open(self):
        self.hosts.append(self)
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        self.hosts.remove(self)
        print "WebSocket closed"
    
    @staticmethod    
    def write(message):
        for host in self.hosts:
            host.write_message(message)

application = tornado.web.Application([
    (r"/", ClientHandler),
    (r"/host", HostHandler),
    (r"/host/websocket", HostWebSocket),
    (r'/resources/client/(.*)', tornado.web.StaticFileHandler, {'path': "resources/client"}),
    (r'/resources/host/(.*)', tornado.web.StaticFileHandler, {'path': "resources/host"}),


])

if __name__ == "__main__":
    port = sys.argv[1]
    application.listen(port, '0.0.0.0') 
    tornado.ioloop.IOLoop.instance().start()