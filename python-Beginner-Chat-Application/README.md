# Python Chat Application

## Internship
Oasis Infobyte – Python Programming Internship

## Task
Task 5 – Chat Application

## Objective
To create a real-time chat application that allows multiple clients to communicate with each other using Python sockets and threading.

## Features
- Real-time messaging between connected clients
- Supports multiple clients
- Displays timestamps with messages
- Shows when users join or leave the chat
- Graceful disconnection using /quit
- Uses localhost for communication
- Uses Python socket and threading modules

## Technologies Used
- Python
- Socket Programming
- Threading
- DateTime Module

## Project Files
- `server.py` – Handles client connections and message broadcasting.
- `client.py` – Connects users to the server and sends and receives messages.
- `screenshots/` – Contains screenshots demonstrating the application.

## How to Run

### Step 1: Start the Server
Open a terminal in the project folder and run:

    python server.py

### Step 2: Start the First Client
Open another terminal and run:

    python client.py

Enter a username when prompted.

### Step 3: Start the Second Client
Open a third terminal and run:

    python client.py

Enter a different username.

### Step 4: Exchange Messages
Send messages between the connected clients.

To leave the chat, type:

    /quit

## Conclusion
This project demonstrates real-time communication between multiple clients using Python socket programming and threading.