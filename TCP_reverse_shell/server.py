import socket

def connect():

    s = socket.socket()
    s.bind(("127.0.0.1", 8888))  #change this ip of server and port
    s.listen(1) 
    conn, addr = s.accept() 
    print ('[+] We got a connection from', addr)

    while True:

        command = input("Shell> ")

        if 'terminate' in command: 
            conn.send('terminate'.encode())
            conn.close()
            break

        else:
            conn.send(command.encode())
            print( conn.recv(1024).decode())

def main():
    connect()
main()
