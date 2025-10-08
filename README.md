A simple command-line chat application built in Python, using sockets and multi-threading.
You can run multiple clients on the same network and chat in real time.

🚀 Features

Multi-client chat server using TCP sockets

Broadcast messages to all connected clients

Threaded server for handling multiple users simultaneously

Clean and modular project structure

🧩 Project Structure
chat_app/
│
├── server/
│   └── server.py         # Chat server
│
├── client/
│   └── client.py         # Chat client
│
├── utils/
│   └── helpers.py        # Helper functions (future use)
│
├── config.py             # Configuration (IP, PORT, BUFFER)
├── LICENSE               # MIT License
└── README.md             # Project description

⚙️ Requirements

Python 3.8+

No external libraries required (uses only Python’s built-in modules)

💻 How to Run
1️⃣ Start the server:
python3 -m server.server

2️⃣ Start a client (in another terminal):
python3 -m client.client


You can open multiple client terminals — any message you send from one will appear in all others.

🧠 Commands (Client)

Type any message → send to all clients

Type exit → disconnect from server

📄 License

This project is licensed under the MIT License
.
Copyright © 2025 takkpii

⭐ Future Improvements

Add usernames and timestamps to messages

Support private messaging

Optional GUI (Tkinter or PyQt)

Message encryption
