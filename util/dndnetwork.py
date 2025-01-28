# dndnetwork.py
"""
This module contains the DungeonMasterServer class, which is a server that
manages a turn-based game for multiple connected clients. The server will
accept connections from clients, broadcast messages to all clients, and
manage the turn-based game loop. Each client is expected to send a message
to the server every turn to participate in the game. They are allowed to send
empty messages.

Players can also send '/quit' to gracefully exit the game. The server will
remove them from the game and close their connection. But it will continue
running the game loop until all players have left.
"""

import socket
import threading
import time

class DungeonMasterServer:
    def __init__(self, game_log, dm_hook=lambda : '', host="127.0.0.1", port=5555, countdown=10):
        self.host = host
        self.port = port
        self.countdown = countdown
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        # Track connected clients in a dict: {client_socket: addr}
        self.clients = {}
        self.game_started = False
        self.running = True

        # Concurrency helpers for turn-based logic
        self.turn_number = 1

        self.dm_hook = dm_hook
        self.update_log = lambda msg: game_log.append(msg+'\n')

    def start_server(self):
        print(f"[DM] Listening on {self.host}:{self.port}")

        # Accept clients on a background thread
        threading.Thread(target=self.accept_clients, daemon=True).start()
        # Do the countdown here in the main thread to block until done
        self.start_countdown()
        # Once countdown finishes, start the turn-based game
        threading.Thread(target=self.game_loop, daemon=True).start()

    def accept_clients(self):
        while True:
            client_sock, addr = self.server_socket.accept()
            self.clients[client_sock] = addr
            print(f"[DM] New connection from {addr}")
            # Notify them if the game started or not
            if self.game_started:
                client_sock.sendall(b"The game has already started!\n")
            else:
                client_sock.sendall(b"You joined before the countdown ended!\n")

            # Each connected client is handled in its own thread

    def handle_client(self, client_sock):
        while True:
            try:
                data = client_sock.recv(1024)
                if not data:
                    continue
                msg = data.decode().strip()

                if msg.lower() == "/quit":
                    self.remove_client(client_sock, reason="Player quit.")
                else:
                    # The player is submitting their turn action
                    self.broadcast_action(client_sock, msg)
                break
            except ConnectionResetError:
                self.remove_client(client_sock, reason="Connection reset.")
                break


    def remove_client(self, client_sock, reason=""):
        if client_sock in self.clients:
            addr = self.clients[client_sock]
            print(f"[DM] Removing client {addr}: {reason}")
            del self.clients[client_sock]
        client_sock.close()


    def start_countdown(self):
        for i in range(self.countdown, 0, -1):
            msg = f"Countdown: {i} seconds left...\n".encode()
            self.broadcast(msg)
            time.sleep(1)
        print("[DM] Countdown ended.")
        self.game_started = True

    def game_loop(self):
        print("[DM] Game loop started! Each player must respond every turn.")
        self.broadcast(b"Game has started!\n")

        while self.running:
            if not self.clients:
                print("[DM] No players left. Stopping game.")
                self.running = False
                break

            # Broadcast that a new turn has started
            turn_msg = f"\n--- TURN {self.turn_number} STARTED ---\n".encode()
            self.broadcast(turn_msg)

            dm_message = self.dm_hook()
            self.broadcast(dm_message.encode())

            self.broadcast(b"Please enter your action (or '/quit' to leave)\n")

            # Wait for all players to respond
            client_threads = []
            for client_sock, _ in self.clients.items():
                thread = threading.Thread(target=self.handle_client, args=(client_sock,), daemon=True)
                thread.start()
                client_threads.append(thread)
            
            for thread in client_threads:
                thread.join()   

            # Announce that the turn is complete
            self.broadcast(f"--- TURN {self.turn_number} COMPLETE ---\n".encode())
            self.turn_number += 1
            time.sleep(1)  # Just a short pause before next turn

        self.server_socket.close()
        print("[DM] Game loop ended. Server closed.")

    def broadcast_action(self, client_sock, msg):
        """Record the player's action, broadcast it, and signal that they've responded."""
        if client_sock not in self.clients:
            return
        addr  = self.clients[client_sock]

        out_msg = f"[{addr}] -> {msg}\n".encode()
        self.broadcast(out_msg)

    def broadcast(self, message: bytes):
        """Send a message to all connected players."""
        print(f"[DM] Broadcasting: {message.decode().strip()}")
        for client_sock in list(self.clients.keys()):
            try:
                client_sock.sendall(message)
            except OSError:
                self.remove_client(client_sock, reason="Send failed.")


# player.py

import socket
import threading

class PlayerClient:
    def __init__(self, name, host="127.0.0.1", port=5555):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.host, self.port))
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def receive_messages(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if not data:
                    break
                print(data.decode().strip())
            except ConnectionResetError:
                print("[Player] Connection closed by server.")
                break

    def send_message(self, msg: str):
        """Send a message to the DM (e.g. the player's action)."""
        self.sock.sendall(msg.encode())

    def unjoin(self):
        """Send '/quit' to gracefully exit."""
        self.send_message("/quit")
        self.sock.close()