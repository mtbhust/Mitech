
import socket               # Import socket module
class client:
    def check_connection(host, port,password):
        s = socket.socket() #Initiate the socket name s
        host = socket.gethostname()
        try:
            s.connect((host, int(port)))
            s.send(("password" +password).encode('utf-8'))
            res = s.recv(2048).decode('utf-8')
            s.close()
            print(res)
            return res
        except:
            return "Failed"
    def response(text,host,port,password):
        if client.check_connection(host, port, password) == "Successful":
                s = socket.socket()
                host = socket.gethostname()
                s.connect((host, int(port)))
                s.send(text.encode('utf-8'))
                try:
                    s.settimeout(5)
                    msg = s.recv(2048).decode('utf-8')
                except:
                    msg = "TimeOut Error"
                print(msg)
                return msg
                s.close()
        return "Please enter correct host and port"