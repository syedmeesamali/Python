import socket, os, sys

if len(sys.argv) != 2:
    sys.exit(0)
if len(sys.argv) > 1:
    port = int(sys.argv[1])
    
host = '127.0.0.1'

socket = socket.socket()
socket.bind((host, port))

socket.listen(1)
print("Listening...")
while (1):
    conn, addr = socket.accept()
    print('New client connected ..')
    reqCommand = conn.recv(1024).decode('utf_8')
    print(reqCommand)
    if (reqCommand == 'x'):
        break
    else:
        string = reqCommand.split(' ', 2)   #in case of 'put' and 'get' method
        reqFile = string[1]
        savFile = string[2]
        if (string[0] == 'PUT'):
            with open(savFile, 'wb') as file_to_write:
                data=conn.recv(1024)
                while True:
                    if not data:
                        break
                    else:
                        file_to_write.write(data)
                        data=conn.recv(1024)
                    file_to_write.close()
                    break
            print('Received & Saved Successfully')
        elif (string[0] == 'GET'):
            with open(reqFile, 'rb') as file_to_send:
                for data in file_to_send:
                    conn.sendall(data)
            print('Sent by Server Successfully')
    conn.close()

socket.close()
