import socket, re, sys, os


if len(sys.argv) != 3:
    sys.exit(0)
if len(sys.argv) > 1:
    host = sys.argv[1]
    parts = host.split(".")
    if len(parts) != 4:
        print("Invalid IP address")
    if(int(sys.argv[2])) < 5000:
        print("Invalid port number")
        sys.exit(0)
    port = int(sys.argv[2])

print("Connected")

 
#-----GET Function---------
def GET(commandName):
    sock = socket.socket()
    #host = '127.0.0.1'
    #port = 5000
    sock.connect((host, port))
    sock.send(commandName.encode('utf-8'))
    string = commandName.split(' ', 2)
    inputFile = string[1]
    savFile = string[2]
    print(savFile)
    with open(savFile, 'wb') as file_to_write:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            file_to_write.write(data)
    file_to_write.close()
    print('GET Successful')
    sock.close()
    return


#-----PUT Function---------
def PUT(commandName):
    sock = socket.socket()
    #host = '127.0.0.1'
    #port = 5000
    sock.connect((host, port))
    sock.send(commandName.encode('utf-8'))
    string = commandName.split(' ', 2)
    inputFile = string[1]
    with open(inputFile, 'rb') as file_to_send:
        data=file_to_send.read(1024)
        while(data):
            sock.send(data)
            data=file_to_send.read(1024)
            file_to_send.close()
    print('PUT Successful')
    sock.close()
    return

#-------intro portion-------------
while(1):
    print("PUT [filename] to send the file the server:")
    print("GET [filename] to download the file from the server:")
    inputCommand = str(input("\n"))
    if (inputCommand == 'x'):
        break
    else:
        string = inputCommand.split(' ',2)
        if (string[0] == 'PUT'):
            print(string[0])
            PUT(inputCommand)
        elif (string[0] == 'GET'):
            print(string[0])
            GET(inputCommand)

