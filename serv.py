import socket
import os.path

sock = socket.socket()
sock.bind(("localhost", 8000))
sock.listen(10)
print ('Listening')

while True:
    connection, address = sock.accept()
    print('...connected from:', address)
    data = connection.recv(2048)
    res = data.split('\n')[0].split(' ')[1]
    path=''
    path = './' + res 
    
    if not os.path.isfile(path):
        path ='./index.html'

    print(path)
            
    file = open(path, 'rb')
    connection.send("""HTTP/1.1 200 OK\nContent-Type: text/html\n\n\n""" + file.read())
    file.close()
    connection.close()    
sock.close()
