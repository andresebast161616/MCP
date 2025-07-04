import socket
import time

HOST = 'localhost'
PORT = 9001

mcp_messages = ["PING", "HELLO", "STATUS", "INFO", "TEST", "UNKNOWN", "EXIT"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    welcome = client.recv(1024)
    print("[SERVER]:", welcome.decode().strip())
    for msg in mcp_messages:
        print(f"[CLIENT]: {msg}")
        client.sendall((msg + "\n").encode())
        reply = client.recv(1024)
        print("[SERVER]:", reply.decode().strip())
        time.sleep(0.5)
