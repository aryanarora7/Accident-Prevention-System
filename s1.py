import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is ready to receive connections.')

# Accept a client connection
client_socket, client_address = server_socket.accept()
print('Connected by:', client_address)

while True:
    # Receive data from the client
    data = client_socket.recv(1024)

    if not data:
        # If no data is received, the client has disconnected
        print('Client has disconnected.')
        break

    # Print the received data
    print('Received:', data.decode())

    # Send a response back to the client
    response = 'Message received: ' + data.decode()
    client_socket.send(response.encode())

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
