import time
import sys

def hack_nasa():
    print("Bypassing Firewall...")
    time.sleep(1)
    
    for i in range(101):
        print(f"\rHacking Nasa: {i}%", end="", flush=True)
        time.sleep(0.1)

    print()
    message = "Nasa hacked successfully! System access granted..."
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

if __name__ == "__main__":
    hack_nasa()