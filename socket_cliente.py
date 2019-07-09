import socket

HOST= "127.0.0.1"
PORT= 59999
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
	client.connect((HOST,PORT))
	salir=True
	while salir:
		entrada=input(">")
		client.sendall(entrada.encode("utf-8"))
		data=client.recv(1024)
		print("Received",repr(data.decode("utf-8")))
		if entrada=="salir": 
			salir=False
		
print("Programa terminado")
