from twisted.internet import reactor, protocol


class MyProtocol(protocol.Protocol):
    def connectionMade(self):
        print("A client connected.")
        
    def dataReceived(self, data):
        self.transport.write(data)
        
    def connectionLost(self, reason):
        print("A client disconnected.")

factory = protocol.Factory()
factory.protocol = MyProtocol
reactor.listenTCP(8000, factory, interface='0.0.0.0')
reactor.run()
