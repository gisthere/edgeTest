import json
import socket

TCP_IP = '0.0.0.0'
TCP_PORT = 5005


def proceed_data(bytes):
    data = json.loads(bytes.decode('utf-8'))
    print(data)


if __name__ == '__main__':

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
                proceed_data(data)
            except ConnectionResetError:
                conn.close()
                print('reconnect')
                conn, addr = s.accept()
                print('Connection address:')
                print(addr)
        except Exception as e:
            print(e)
            break  # если возникнет исключение, то манипулятор сдохнет( А в докер композе не прописано, чтобы он автоматически перезапускался.
                   # в продакшн коде это нужно учитывать.

    # Наверное хотелось сделать обработку любых исключений, которые не являются  ConnectionResetError? Если да, то можно было сделать примерно так:
    # while True:
    #     try:
    #         data = conn.recv(1024)
    #         if data == b'':
    #             raise ConnectionResetError()
    #         proceed_data(data)
    #     except ConnectionResetError:
    #         conn.close()
    #         print('reconnect')
    #         conn, addr = s.accept()
    #         print('Connection address:')
    #         print(addr)
    #     except Exception as e:
    #         print(e)
    #         break
