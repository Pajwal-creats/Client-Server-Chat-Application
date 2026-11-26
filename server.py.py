"""
TCP Chat Server - OS Mini Project (with colours)
Concepts: sockets, threads (concurrency), mutex lock (synchronization)
"""
import socket
import threading
import datetime

HOST = "0.0.0.0"   # listen on all network interfaces
PORT = 5000

# ANSI colour codes (terminal colours)
RESET = "\033[0m"
COLORS = [
    "\033[91m",  # red
    "\033[92m",  # green
    "\033[94m",  # blue
    "\033[95m",  # magenta
    "\033[96m",  # cyan
    "\033[93m",  # yellow
]
NOTICE = "\033[96m"  # grey, for join/leave notices

clients = {}                    # socket -> (username, colour) : shared resource
clients_lock = threading.Lock() # mutex: protects the shared dictionary
color_counter = 0               # used to give each client a different colour


def log(msg):
    print(f"[{datetime.datetime.now():%H:%M:%S}] {msg}")


def broadcast(message, sender=None):
    """Send a message to every connected client except the sender."""
    with clients_lock:
        for sock in list(clients):
            if sock is not sender:
                try:
                    sock.sendall(message.encode())
                except OSError:
                    pass  # client gone; its own thread will clean up


def handle_client(conn, addr):
    """Runs in its own thread: one thread per connected client."""
    global color_counter
    try:
        conn.sendall(b"Enter your name: ")
        name = conn.recv(1024).decode().strip() or f"{addr[0]}:{addr[1]}"
        with clients_lock:
            color = COLORS[color_counter % len(COLORS)]
            color_counter += 1
            clients[conn] = (name, color)
        log(f"{name} joined from {addr}")
        broadcast(f"{NOTICE}*** {name} joined the chat ***{RESET}\n", sender=conn)
        conn.sendall(f"Connected! You are {color}{name}{RESET}. "
                     f"Commands: /list, /quit\n".encode())

        while True:
            data = conn.recv(1024)
            if not data:            # empty = client closed connection
                break
            text = data.decode().strip()
            if text == "/quit":
                break
            elif text == "/list":
                with clients_lock:
                    users = ", ".join(f"{c}{n}{RESET}" for n, c in clients.values())
                conn.sendall(f"Online: {users}\n".encode())
            elif text:
                log(f"{name}: {text}")
                broadcast(f"{color}{name}{RESET}: {text}\n", sender=conn)
    except ConnectionError:
        pass
    finally:
        with clients_lock:
            name, _ = clients.pop(conn, ("Unknown", ""))
        conn.close()
        log(f"{name} left")
        broadcast(f"{NOTICE}*** {name} left the chat ***{RESET}\n")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    log(f"Server listening on port {PORT} (Ctrl+C to stop)")
    try:
        while True:
            conn, addr = server.accept()   # blocks until a client connects
            threading.Thread(target=handle_client, args=(conn, addr),
                             daemon=True).start()
    except KeyboardInterrupt:
        log("Shutting down")
    finally:
        server.close()


if __name__ == "__main__":
    main()