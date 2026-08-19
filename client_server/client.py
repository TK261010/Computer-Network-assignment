import socket

HOST = "127.0.0.1"
PORT = 5000

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((HOST, PORT))

print("===================================")
print("          CLIENT PROGRAM")
print("===================================")

# Take message from user
message = input("Enter message to send to server: ")

# Send message
client_socket.send(message.encode())

print("Message sent to server.")

# Receive response
response = client_socket.recv(1024).decode()

print("Response from server:", response)

# Close connection
client_socket.close()

print("Client connection closed.")
