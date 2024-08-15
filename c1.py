import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

# Send data to the server
message = 'Hello, server!'
client_socket.send(message.encode())

# Receive a response from the server
response = client_socket.recv(1024)

# Print the response
print('Response:', response.decode())

# Close the socket
client_socket.close()
