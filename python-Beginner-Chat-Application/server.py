import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12345

clients = []
usernames = []


def broadcast(message, sender=None):
    for client in clients[:]:
        if client != sender:
            try:
                client.send(message.encode("utf-8"))
            except OSError:
                remove_client(client)


def remove_client(client):
    if client in clients:
        index = clients.index(client)
        username = usernames[index]

        clients.remove(client)
        usernames.remove(username)

        timestamp = datetime.now().strftime("%H:%M")
        broadcast(f"[{timestamp}] {username} disconnected.\n")

        try:
            client.close()
        except OSError:
            pass


def handle_client(client):
    try:
        username = client.recv(1024).decode("utf-8").strip()

        if not username:
            username = "Guest"

        clients.append(client)
        usernames.append(username)

        timestamp = datetime.now().strftime("%H:%M")
        print(f"[{timestamp}] {username} joined the chat.")

        broadcast(f"[{timestamp}] {username} joined the chat.\n", client)

        while True:
            message = client.recv(1024).decode("utf-8")

            if not message:
                break

            timestamp = datetime.now().strftime("%H:%M")
            formatted_message = f"[{timestamp}] {username}: {message}"

            print(formatted_message)
            broadcast(formatted_message, client)

    except (ConnectionError, OSError):
        pass

    finally:
        remove_client(client)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Chat server is running...")
print(f"Waiting for connections on {HOST}:{PORT}")

try:
    while True:
        client, address = server.accept()
        print(f"Connection established: {address}")

        thread = threading.Thread(
            target=handle_client,
            args=(client,),
            daemon=True
        )
        thread.start()

except KeyboardInterrupt:
    print("\nServer shutting down...")

finally:
    for client in clients[:]:
        try:
            client.close()
        except OSError:
            pass

    server.close()