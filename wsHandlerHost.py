import tornado.websocket
import modules.password


class HostWebSocket(tornado.websocket.WebSocketHandler):
    hosts = []

    def open(self):
        self.hosts.append(self)
        self.write_message(modules.password.currentPassword)
        print "WebSocket opened"

    def on_message(self, message):
        pass

    def on_close(self):
        self.hosts.remove(self)
        print "WebSocket closed"

    @classmethod
    def broadcast(cls, message):
        for host in HostWebSocket.hosts:
            host.write_message(message)