import unittest
import asyncio
from tcp_protocol import TCPProtocolHandler

class TestTCPProtocolHandler(unittest.TestCase):
    def setUp(self):
        self.handler = TCPProtocolHandler()

    async def async_test_connection(self):
        await self.handler.connect("127.0.0.1", 8888)
        await self.handler.write("Hello")
        await self.handler.read()

    def test_connection(self):
        asyncio.run(self.async_test_connection())

if __name__ == "__main__":
    unittest.main()
