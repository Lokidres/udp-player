# sender.py
import socket
import sys

if len(sys.argv) < 2:
    print("Usage: python sender.py <filename> [port]")
    print("Example: python sender.py song.mp3")
    sys.exit(1)

filename = sys.argv[1]
port = int(sys.argv[2]) if len(sys.argv) > 2 else 5555
ENC = "utf-8"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(filename.encode(ENC), ("127.0.0.1", port))
print(f"Sent play command: {filename} -> 127.0.0.1:{port}")
sock.close()
