import asyncio
import websockets

async def handle_connection(websocket, path):
    while True:
        # Receive data from the client
        data = await websocket.recv()
        print(f"Received data from client:\n{data}")

async def main():
    server = await websockets.serve(handle_connection, "0.0.0.0", 8765)
    print("WebSocket server started on ws://0.0.0.0:8765")

    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
