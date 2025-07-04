import socket

HOST = '0.0.0.0'
PORT = 9001

def process_client(conn, address):
    print(f"New client connected from {address}")
    conn.sendall(b"=== MCP SERVER ONLINE ===\nAvailable commands: PING, HELLO, STATUS, INFO, TEST, EXIT\n")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        command = data.decode().strip().upper()
        if command == "PING":
            conn.sendall(b"PONG\n")
        elif command == "HELLO":
            conn.sendall(b"WELCOME TO MCP SERVER\n")
        elif command == "STATUS":
            conn.sendall(b"SERVER STATUS: RUNNING OK\n")
        elif command == "INFO":
            conn.sendall(b"MCP SERVER v1.0 - Python Implementation\n")
        elif command == "TEST":
            conn.sendall(b"TEST SUCCESSFUL - Connection Working\n")
        elif command == "EXIT":
            conn.sendall(b"GOODBYE - Closing Connection\n")
            break
        else:
            conn.sendall(b"ERROR: Unknown Command - Try PING, HELLO, STATUS, INFO, TEST, or EXIT\n")
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"MCP Server running at {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        process_client(conn, addr)
