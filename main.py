import asyncio
from tcp_protocol import TCPProtocolHandler

async def handle_device(ip, port):
    handler = TCPProtocolHandler()
    await handler.connect(ip, port)
    await handler.write("Hello from main")
    await handler.read()

async def main():
    tasks = [
        handle_device("127.0.0.1", 8888),
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
