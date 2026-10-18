import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12345


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if not message:
                break

            print(message, end="" if message.endswith("\n") else "\n")

        except (ConnectionError, OSError):
            break

    print("\nDisconnected from the chat server.")


def main():
    username = input("Enter your username: ").strip()

    if not username:
        username = "Guest"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        client.send(username.encode("utf-8"))

        print(f"\nWelcome, {username}!")
        print("You are connected to the chat.")
        print("Type your messages and press Enter.")
        print("Type /quit to leave the chat.\n")

        receiver = threading.Thread(
            target=receive_messages,
            args=(client,),
            daemon=True
        )
        receiver.start()

        while True:
            message = input()

            if message.strip().lower() == "/quit":
                break

            if message.strip():
                timestamp = datetime.now().strftime("%H:%M")
                print(f"[{timestamp}] You: {message}")
                client.send(message.encode("utf-8"))

    except ConnectionRefusedError:
        print("Error: Server is not running. Start server.py first.")

    except (ConnectionError, OSError) as error:
        print(f"Connection error: {error}")

    finally:
        client.close()
        print("Chat client closed.")


if __name__ == "__main__":
    main()