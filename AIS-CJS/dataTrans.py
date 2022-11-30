import socket

#연결할 Host, Port 정보
HOST = '175.200.108.201'
PORT = 5000

#소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#서버에 접속
client_socket.connect((HOST, PORT))

#서버에 "Hello world"메세지 전송
client_socket.sendall("Hello world".encode()); 
print("데이터 전송")
#서버에게서 메시지를 수신(에코)
data = client_socket.recv(1024)
print('Received', repr(data.decode()))

#클라이언트 소켓을 닫는다.
client_socket.close()