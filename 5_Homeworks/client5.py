import socket, sys

if len(sys.argv) != 3:
    sys.exit(0)
if len(sys.argv) > 1:
    host = sys.argv[1]
    parts = host.split(".")
    if len(parts) != 4:
        print("Invalid IP address")
    if(int(sys.argv[2])) < 5000:
        print("Invalid port number: Should be more than 5000")
        sys.exit(0)
    port = int(sys.argv[2])

print("Connected")

 
#-----GET Function---------
def GET(commandName):
    sock = socket.socket()
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
    print("PUT <space> inputfile <space> outputfile: ")
    print("GET <space> inputfile <space> outputfile: ")
    inputCommand = str(input("\n"))
    if (inputCommand == 'x'):
        break
    else:
        string = inputCommand.split(' ', 2)
        if (string[0] == 'PUT'):
            PUT(inputCommand)
        elif (string[0] == 'GET'):
            GET(inputCommand)
        else:
            print("Enter valid command please..")