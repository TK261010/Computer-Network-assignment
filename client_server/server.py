import socket

HOST = "127.0.0.1"
PORT = 5000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to IP address and port
server_socket.bind((HOST, PORT))

# Listen for client connection
server_socket.listen(1)

print("===================================")
print("       CLIENT-SERVER PROGRAM")
print("===================================")
print("Server started...")
print("Waiting for client connection...")

# Accept client connection
connection, address = server_socket.accept()

print("Client connected:", address)

# Receive message
message = connection.recv(1024).decode()

print("Message received from client:", message)

# Send response
response = "Hello Client! Your message was received successfully."
connection.send(response.encode())

print("Response sent to client.")

# Close connection
connection.close()
server_socket.close()

print("Server connection closed.")
