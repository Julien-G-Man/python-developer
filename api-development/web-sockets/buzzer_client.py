import asyncio
import keyboard
import websockets

async def start_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        done = False
        while not done:
            if keyboard.is_pressed("space"):
                await websocket.send("buzz")
                message = await websocket.recv()
                print(message)
                done=True
                
if __name__ == "__main__":
    asyncio.run(start_client())