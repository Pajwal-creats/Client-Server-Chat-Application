# 💬 Client-Server Chat Application Using TCP Sockets

### Operating Systems Mini Project

A multi-client chat application developed using Python that enables multiple users to communicate through a central server using TCP socket programming.

This project demonstrates important Operating System concepts such as **Socket Communication, Multithreading, Concurrency, Synchronization, and Mutex Locks.**

---

## 🚀 Features

- Multiple clients can connect to a single server.
- Real-time message broadcasting.
- TCP-based communication.
- Separate thread for handling each connected client.
- Mutex lock for protecting shared client data.
- Online users list.
- Client join and leave notifications.
- Different terminal colours for different users.
- Simple commands to manage chat sessions.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Socket Programming | Client-Server Communication |
| TCP/IP | Reliable Data Transmission |
| Multithreading | Handling Multiple Clients |
| Mutex Lock | Synchronization |
| Threading Module | Concurrent Execution |

---

## 📂 Project Structure

```text
Client-Server-Chat-Application/
│
├── client.py
├── server.py
├── connection_server.pdf
├── OS_ppt_final.pdf
└── README.md
```

---

## 🧠 Operating System Concepts Implemented

### 1. Socket Programming
Sockets establish communication between the server and multiple clients using TCP/IP.

### 2. Multithreading
The server creates a separate thread for each connected client, allowing multiple users to communicate simultaneously.

### 3. Synchronization
A mutex lock prevents multiple threads from modifying shared client data simultaneously.

Implementation:

```python
clients_lock = threading.Lock()
```

### 4. Shared Resources
The client dictionary is a shared resource containing information about all connected clients.

### 5. Concurrency
Multiple client threads execute concurrently, allowing the server to handle several users at the same time.

---

## ⚙️ How to Run the Project

### Requirements
- Python 3.x
- Two or more terminal windows
- Local network connection (for multiple computers)

### Step 1: Start the Server

Open a terminal in the project directory and execute:

```bash
python server.py
```

The server starts listening on port `5000`.

### Step 2: Start the Client

Open another terminal and execute:

```bash
python client.py
```

To connect from another computer:

```bash
python client.py SERVER_IP
```

Replace `SERVER_IP` with the IP address of the computer running the server.

### Step 3: Start Chatting

Enter your username when prompted and start communicating with other connected clients.

---

## ⌨️ Available Commands

| Command | Function |
|---|---|
| `/list` | Displays all connected users |
| `/quit` | Disconnects from the chat server |

---

## 📄 Project Documentation

The repository also contains:

- Project report/documentation (`connection_server.pdf`)
- Project presentation (`OS_ppt_final.pdf`)

---

## 🎯 Project Objective

The main objective of this project is to understand how Operating System concepts such as process concurrency, multithreading, synchronization, and mutual exclusion are applied in a real-world client-server communication system.

---

**Project Domain:** Operating Systems  
**Programming Language:** Python  
**Communication Protocol:** TCP  
**Project Type:** Academic Mini Project
