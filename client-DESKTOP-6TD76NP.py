from twisted.internet import reactor, protocol

class MyClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hello, Server!".encode())
        
    def dataReceived(self, data):
        print("Server sent:", data.decode())
        self.transport.loseConnection()
        
    def connectionLost(self, reason):
        print("Connection lost.")

class MyClientFactory(protocol.ClientFactory):
    protocol = MyClient
    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")
        reactor.stop()
        
    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()
        
reactor.connectTCP("192.168.8.10", 8000, MyClientFactory())
reactor.run()
