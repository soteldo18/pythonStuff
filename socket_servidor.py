import socket

HOST="127.0.0.1"
PORT=59999
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
	server.bind((HOST,PORT))
	server.listen(1)
	conn,addr=server.accept()
	with conn:
		print("Connected by",addr)
		salir=True
		while salir:
			data=conn.recv(1024)
			reenviar="Escribistes: "+str(data.decode("utf-8"))
			print("Dato recibido:",str(data.decode("utf-8")))
			if data=="salir":
				salir=False
			else:
				conn.sendall(reenviar.encode("utf-8"))
			
print("programa terminado")






