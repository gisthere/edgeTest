import socket

TCP_IP = '0.0.0.0'
TCP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print('manipulator started')
conn, addr = s.accept()
print('Connection address:')
print(addr)
while 1:
    try:
        try:
            data = conn.recv(1024)
            if data == b'':
                raise ConnectionResetError()
            print("received data:", data)
        except ConnectionResetError:
            conn.close()
            print('reconnect')
            conn, addr = s.accept()
            print('Connection address:')
            print(addr)
    except Exception as e:
        print(e)
        break
