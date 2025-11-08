
import socket
import pygame
import os

UDP_IP = "127.0.0.1"
UDP_PORT = 5555
ENC = "utf-8"
BUFFER = 2048


MUSIC_DIR = os.path.abspath(".")  

pygame.mixer.init()
pygame.mixer.music.set_volume(0.8)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"[+] UDP listener running on {UDP_IP}:{UDP_PORT}")
print("[+] Send single filename (e.g. song.mp3) to play")

while True:
    data, addr = sock.recvfrom(BUFFER)
    if not data:
        continue
    try:
        filename = data.decode(ENC).strip()
    except Exception:
        continue

    if filename == "":
        continue

   
    if os.path.isabs(filename):
        path = filename
    else:
        path = os.path.join(MUSIC_DIR, filename)

    if not os.path.isfile(path):
        print(f"[!] File not found: {path}")
        continue

    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()  
    except Exception:
        pass

    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        print(f"[+] Playing: {path}")
    except Exception as e:
        print(f"[!] Error playing {path}: {e}")
