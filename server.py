import socket
import asyncio
from aioconsole import ainput

HOST = '127.0.0.1'  # 标准的回环地址 (localhost)
PORT = 65432        # 监听的端口 (非系统级的端口: 大于 1023)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    # server.setblocking(False)
    conn,_ = server.accept()

    loop = asyncio.get_event_loop()
    loop.create_task(handle_receive(conn))
    loop.create_task(handle_send(conn))
    loop.run_forever()

async def handle_receive(conn):
    print('started')
    while True:
        data = await loop.sock_recv(conn, 1024)
        if not data:
            print('prepare break')
            break
        print('you: ' + data.decode('utf-8'))
    print('done')

async def handle_send(conn):
    print('started')
    while True:
        str = await ainput("me: ")
        await loop.sock_sendall(conn,str.encode('utf-8'))
    print('done')

main()