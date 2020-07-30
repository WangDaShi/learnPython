import socket
import asyncio
from aioconsole import ainput

HOST = '127.0.0.1'  # 服务器的主机名或者 IP 地址
PORT = 65432        # 服务器使用的端口

async def handle_receive(conn):
    print('started')
    while True:
        data = await loop.sock_recv(conn, 1024)
        if not data:
            print('prepare break')
            break
        print('you:' + data.decode('utf-8'))
    print('done')

async def handle_send(conn):
    print('started')
    while True:
        str = await ainput("me: ")
        await loop.sock_sendall(conn,str.encode('utf-8'))
    print('done')


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print('连接已建立')
loop = asyncio.get_event_loop()
#loop.create_task(asyncio.start_server(handle_receive, HOST, PORT))
loop.create_task(handle_receive(client))
loop.create_task(handle_send(client))
loop.run_forever()



# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     print('开始发送数据')
#     while(True):
#         print('me:')
#         str = input()
#         s.sendall(str.encode('utf-8'))
#         data = s.recv(1024)
#         print('you:')
#         print(data.decode('utf-8'))

# print('退出')
