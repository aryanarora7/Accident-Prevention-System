import tkinter as tk
import socket

class TCPClientGUI:
    def __init__(self):
        self.server_ip = '172.20.10.2'
        self.server_port = 12345
        self.client_socket = None
       
        self.window = tk.Tk()
        self.window.title("TCP Client GUI")
       
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = int(screen_width / 2)
        window_height = int(screen_height / 2)
        window_x = int((screen_width - window_width) / 2)
        window_y = int((screen_height - window_height) / 2)
        self.window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")  # Set window size and position
       
        self.create_widgets()
       
    def create_widgets(self):
        self.label = tk.Label(self.window, text="Enter command:", font=("Arial", 24), fg="white", bg="blue")
        self.label.pack(pady=50)
       
        self.entry = tk.Entry(self.window, width=50, font=("Arial", 18))
        self.entry.pack(pady=10)
       
        self.send_button = tk.Button(self.window, text="Send", command=self.send_data, font=("Arial", 18), fg="white", bg="green")
        self.send_button.pack(pady=20)
       
        self.close_button = tk.Button(self.window, text="Close Connection", command=self.close_connection, font=("Arial", 18), fg="white", bg="red")
        self.close_button.pack(pady=20)
       
    def send_data(self):
        data = self.entry.get()
       
        if data:
            if self.client_socket is None:
                self.create_socket()
               
            try:
                self.client_socket.sendall(data.encode())
                print("Data sent:", data)

            except Exception as e:
                print("An error occurred:", str(e))
                self.close_connection()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            print("Connected to server:", self.server_ip)

        except Exception as e:
            print("An error occurred:", str(e))
            self.close_connection()
       
    def close_connection(self):
        if self.client_socket is not None:
            self.client_socket.close()
            print("Client socket closed.")
            self.client_socket = None
           
    def run(self):
        self.window.mainloop()

# Create and run the TCPClientGUI
gui = TCPClientGUI()
gui.run()
