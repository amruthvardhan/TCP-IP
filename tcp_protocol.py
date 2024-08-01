import asyncio

class TCPProtocolHandler:
    def __init__(self):
        self.reader = None
        self.writer = None

    async def connect(self, ip, port):
        """
        Establish a TCP connection to the specified IP address and port.
        
        :param ip: The IP address to connect to.
        :param port: The port number to connect to.
        """
        self.reader, self.writer = await asyncio.open_connection(ip, port)
    
    async def read(self):
        """
        Read up to 100 bytes of data from the connected socket.
        """
        data = await self.reader.read(100)
        print(f"Received: {data.decode()}")
    
    async def write(self, message):
        """
        Write a message to the connected socket.
        
        :param message: The message to send. It will be encoded to bytes.
        """
        self.writer.write(message.encode())
        await self.writer.drain()
        self.writer.close()
        await self.writer.wait_closed()
