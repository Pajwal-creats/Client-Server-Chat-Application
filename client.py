"""
TCP Chat Client - OS Mini Project
One thread receives messages, the main thread sends them.
"""
import os
import socket
import sys
import threading

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 5000


def receive(sock):
    while True:
        try:
            data = sock.recv(1024)
        except OSError:
            break
        if not data:
            print("\nDisconnected from server.")
            break
        print(data.decode(), end="", flush=True)


def main():
    os.system("")  # enables colour codes in Windows consoles
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect. Is the server running?")
        return
    threading.Thread(target=receive, args=(sock,), daemon=True).start()
    try:
        while True:
            msg = input()
            sock.sendall(msg.encode())
            if msg == "/quit":
                break
    except (KeyboardInterrupt, EOFError, OSError):
        pass
    finally:
        sock.close()


if __name__ == "__main__":
    main()
