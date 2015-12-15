import socket

#Clase que contiene los metodos para comunicarme con el servidor
class Socket():
    
    def __init__(self,host,puerto):
        self.host=host
        self.puerto=puerto
    
    def conectar(self):        
        self.sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sc.connect((self.host,self.puerto))

    def leer(self):
        try:
            bufSize=1024
            datos_recibidos=self.sc.recv(bufSize)
            return datos_recibidos.decode('utf-8')        
        except socket.error as msg:
            print("Socket Error: %s" % msg)
    
    def escribir(self, mensaje):
        #enviar mensaje en formato utf8
        self.sc.send(mensaje.encode('utf8'))
    
    def desconectar(self):
        #terminar socket
        self.sc.close()
    
    #imprime la informacion de conexion con el cliente
    def imprimir(self):
        print(self.datos_cliente)

