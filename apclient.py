import socket

# Define the server's IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))
print("Connected to the server.")

# Function to send data to the server
def send_data(data):
    # Send the data to the server
    client_socket.sendall(data.encode())
    print("Data sent to the server.")

# Send data to the server
data = input("Enter data to send: ")
send_data(data)

# Close the socket connection
client_socket.close()
